"""JavaScript example renderer for gen_docs.py (SDK: `whoisfreaks-js` on npm).

Matches the openapi-generator `javascript` (ES6, superagent) client as built to
CommonJS in dist/:
  * examples are CommonJS (`require`) so they run with plain `node file.js`
    after `npm init -y && npm install whoisfreaks-js`
  * auth: ApiClient.instance.authentications["ApiKeyAuth"].apiKey, set once,
    read from WHOISFREAKS_API_KEY
  * required params are positional, in spec order, then the request body;
    optional params go in a trailing `opts` object
  * dates are "yyyy-MM-dd" strings: the SDK sends a Date object as a full
    ISO timestamp (Date#toJSON), which the API does not expect
  * request bodies are built with <Model>.constructFromObject({...})
  * downloads resolve to a Buffer in Node.js, written with fs.writeFileSync
"""
import json

LANG = "javascript"

# Optional params worth showing, beyond the always-shown `date` (database
# downloads) and `page` (paginated lookups). None = use the spec example value.
_SHOW_OPTIONAL = {
    "domainAvailabilityV2": {"sug": True, "count": None},
    "dnsLive": {"domainName": None},
    "typosquatting": {"keyword": None},
}


def _clean(text):
    """One-line text without em/en dashes (house style)."""
    return " ".join(str(text).replace(" — ", ": ").replace("—", ", ")
                    .replace("–", "-").split())


def _shown(op, p):
    n = p["name"]
    if n == "apiKey":
        return False
    if p["required"] or n in ("date", "page"):
        return True
    return n in _SHOW_OPTIONAL.get(op["op_id"], {})


def _value(op, p, ctx):
    override = _SHOW_OPTIONAL.get(op["op_id"], {}).get(p["name"])
    return override if override is not None else ctx.example_value(p)


def _lit(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, list):
        return "[" + ", ".join(_lit(x) for x in v) + "]"
    return json.dumps(str(v))


def _response_kind(op, ctx):
    """binary | model | model_list | string_list | text"""
    if op.get("is_binary"):
        return "binary"
    if op.get("response_schema"):
        return "model_list" if op.get("response_is_array") else "model"
    resp = ctx.deref(((ctx.spec["paths"][op["path"]][op["method"].lower()].get("responses") or {})
                      .get("200")) or {})
    content = resp.get("content") or {}
    if "text/plain" in content:
        return "text"
    sch = ctx.deref((content.get("application/json") or {}).get("schema") or {})
    if sch.get("type") == "array":
        return "string_list"
    return "model"


def download_filename(op, ctx):
    return ctx.download_name(op)


def _type_label(p):
    if p.get("format") == "date":
        return 'string, "yyyy-MM-dd"'
    return {"integer": "number", "boolean": "boolean", "number": "number"}.get(p.get("type"), "string")


def _body_var(model):
    return model[0].lower() + model[1:]


def _params_comment(op, ctx, method):
    req = [p for p in op["params"] if p["name"] != "apiKey" and p["required"]]
    opt = [p for p in op["params"] if p["name"] != "apiKey" and not p["required"]]
    bm = op.get("body_model")
    sig = [p["name"] for p in req] + ([_body_var(bm)] if bm else []) + (["opts"] if opt else [])
    if not sig:
        return [f"// {method}() takes no parameters."]
    lines = [f"// {method}({', '.join(sig)})"]
    def line(p, name, kind):
        extra = []
        if p.get("enum"):
            extra.append("one of " + ", ".join(str(e) for e in p["enum"]))
        if p.get("default") is not None:
            extra.append(f"default {_lit(p['default'])}")
        desc = _clean(p.get("desc") or "").rstrip(".")
        if len(desc) > 80:
            desc = desc[:77] + "..."
        tail = "; ".join(x for x in [desc] + extra if x)
        return f"//   {name} ({_type_label(p)}, {kind})" + (f": {tail}" if tail else "")
    for p in req:
        lines.append(line(p, p["name"], "required"))
    if bm:
        lines.append(f"//   {_body_var(bm)} ({bm}, required): request body")
    for p in opt:
        lines.append(line(p, "opts." + p["name"], "optional"))
    return lines


def _header(op, run_file):
    run = (f"// Run (public endpoint, no API key needed): node {run_file}" if op["public"] else
           f"// Run: WHOISFREAKS_API_KEY=your_api_key node {run_file}")
    return [f"// {_clean(op['summary'] or op['op_id'])}: {op['method']} {op['server']}{op['path']}", run]


def example(op, ctx):
    cls = ctx.api_class(op["tag"], LANG)
    m = ctx.method_name(op["op_id"], LANG)
    kind = _response_kind(op, ctx)
    bm = op.get("body_model")
    ind = "  "

    args, opts = [], []
    for p in op["params"]:
        if _shown(op, p) and p["required"]:
            args.append(_lit(_value(op, p, ctx)))
    body_lines = []
    if bm:
        fields = ", ".join(f"{k}: {_lit(v)}" for k, v in ctx.body_example(op).items())
        body_lines.append(f"{ind}const body = {bm}.constructFromObject({{ {fields} }});")
        args.append("body")
    for p in op["params"]:
        if _shown(op, p) and not p["required"]:
            opts.append(f"{p['name']}: {_lit(_value(op, p, ctx))}")
    if opts:
        args.append("{ " + ", ".join(opts) + " }")
    call = f"api.{m}({', '.join(args)})"

    names = ([] if op["public"] else ["ApiClient"]) + [cls] + ([bm] if bm else [])
    out = _header(op, f"{ctx.pascal(op['op_id'])}.js")
    if kind == "binary":
        out += ['const fs = require("node:fs");', 'const path = require("node:path");']
    out.append(f'const {{ {", ".join(names)} }} = require("{ctx.LANGS[LANG]["pkg"]}");')
    out.append("")
    if op["public"]:
        out += ["// Public endpoint: no API key needed.", f"const api = new {cls}();"]
    else:
        out += ["// Set the API key once; the client adds it to every request.",
                "const client = ApiClient.instance;",
                'client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;',
                f"const api = new {cls}(client);"]
    out.append("")
    out += _params_comment(op, ctx, m)
    out.append("async function main() {")
    out += body_lines
    if kind == "binary":
        fname = download_filename(op, ctx)
        out += [f"{ind}const data = await {call}; // a Buffer with the file's bytes",
                f'{ind}const file = "{fname}";',
                f"{ind}fs.writeFileSync(file, data);",
                f"{ind}console.log(`Saved ${{data.length}} bytes to ${{path.resolve(file)}}`);"]
    elif kind == "model_list":
        out += [f"{ind}const results = await {call};",
                f"{ind}console.log(JSON.stringify(results, null, 2));"]
    elif kind == "string_list":
        out += [f"{ind}const domains = await {call};",
                f"{ind}console.log(`${{domains.length}} domains`);",
                f'{ind}console.log(domains.slice(0, 10).join("\\n"));']
    elif kind == "text":
        out += [f"{ind}const newKey = await {call}; // use this key from now on",
                f'{ind}console.log("New API key:", newKey);']
    else:
        out += [f"{ind}const result = await {call};",
                f"{ind}console.log(JSON.stringify(result, null, 2));"]
    out += ["}", "",
            "main().catch((err) => {",
            "  // API errors carry the HTTP status and the parsed error body",
            "  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);",
            "  process.exitCode = 1;",
            "});"]
    return "\n".join(out)


def getting_started(ctx):
    pkg = ctx.LANGS[LANG]["pkg"]
    cls = ctx.api_class("WHOIS", LANG)
    m = ctx.method_name("whoisLive", LANG)
    return [
        "1. Create a project and install the SDK (Node.js 18 or later):", "",
        "```bash",
        "mkdir whoisfreaks-test && cd whoisfreaks-test",
        "npm init -y",
        f"npm install {pkg}",
        "```", "",
        "2. Create `main.js`:", "",
        "```javascript",
        f'const {{ ApiClient, {cls} }} = require("{pkg}");',
        "",
        "// Set the API key once; the client adds it to every request.",
        "const client = ApiClient.instance;",
        'client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;',
        f"const api = new {cls}(client);",
        "",
        "async function main() {",
        f'  const record = await api.{m}("whoisfreaks.com");',
        '  console.log("Domain: ", record.domain_name);',
        '  console.log("Created:", record.create_date);',
        '  console.log("Expires:", record.expiry_date);',
        "}",
        "",
        "main().catch((err) => {",
        "  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);",
        "  process.exitCode = 1;",
        "});",
        "```", "",
        "3. Set your API key and run it:", "",
        "```bash",
        'export WHOISFREAKS_API_KEY="your_api_key"   # PowerShell: $env:WHOISFREAKS_API_KEY="your_api_key"',
        "node main.js",
        "```",
    ]
