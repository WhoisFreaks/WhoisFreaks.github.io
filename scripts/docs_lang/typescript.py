"""TypeScript example renderer for gen_docs.py (SDK: `whoisfreaks` on npm).

Matches the openapi-generator `typescript-fetch` client:
  * auth: new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY }), set once
  * every operation with parameters takes ONE request object, e.g.
    whoisLive({ domainName }); the body goes in it under the camelCase model
    name (bulkWhois({ bulkWhoisRequest })); operations without parameters take none
  * `format: date` params are typed Date: new Date("2026-10-01") (sent as yyyy-MM-dd);
    other dates (threat feeds) are plain strings
  * request bodies are object literals typed with the model interface
  * downloads resolve to a Blob, written with fs/promises writeFile
  * code runs inside async main(), so it works as CommonJS or ESM with `npx tsx`
    and type-checks under `tsc --strict`
"""
import json

LANG = "typescript"

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


def _lit(v, p=None):
    if p is not None and p.get("format") == "date":
        return f"new Date({json.dumps(str(v))})"
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
        return "Date"
    if p.get("enum"):
        return " | ".join(json.dumps(str(e)) for e in p["enum"])
    return {"integer": "number", "boolean": "boolean", "number": "number"}.get(p.get("type"), "string")


def _body_key(model):
    return model[0].lower() + model[1:]


def _params_comment(op, ctx, method):
    params = [p for p in op["params"] if p["name"] != "apiKey"]
    bm = op.get("body_model")
    if not params and not bm:
        return [f"// {method}() takes no parameters."]
    keys = [p["name"] for p in params if p["required"]]
    keys += [_body_key(bm)] if bm else []
    keys += [p["name"] + "?" for p in params if not p["required"]]
    lines = [f"// {method}({{ {', '.join(keys)} }})"]
    def line(p, kind):
        extra = []
        if p.get("default") is not None:
            extra.append(f"default {_lit(p['default'])}")
        desc = _clean(p.get("desc") or "").rstrip(".")
        if len(desc) > 80:
            desc = desc[:77] + "..."
        tail = "; ".join(x for x in [desc] + extra if x)
        return f"//   {p['name']} ({_type_label(p)}, {kind})" + (f": {tail}" if tail else "")
    for p in params:
        if p["required"]:
            lines.append(line(p, "required"))
    if bm:
        lines.append(f"//   {_body_key(bm)} ({bm}, required): request body")
    for p in params:
        if not p["required"]:
            lines.append(line(p, "optional"))
    return lines


def _header(op, run_file):
    run = (f"// Run (public endpoint, no API key needed): npx tsx {run_file}" if op["public"] else
           f"// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx {run_file}")
    return [f"// {_clean(op['summary'] or op['op_id'])}: {op['method']} {op['server']}{op['path']}", run]


def example(op, ctx):
    cls = ctx.api_class(op["tag"], LANG)
    m = ctx.method_name(op["op_id"], LANG)
    kind = _response_kind(op, ctx)
    bm = op.get("body_model")
    ind = "  "

    fields, pre = [], []
    for p in op["params"]:
        if _shown(op, p) and p["required"]:
            fields.append(f"{p['name']}: {_lit(_value(op, p, ctx), p)}")
    if bm:
        bf = ", ".join(f"{k}: {_lit(v)}" for k, v in ctx.body_example(op).items())
        pre.append(f"{ind}const body: {bm} = {{ {bf} }};")
        fields.append(f"{_body_key(bm)}: body")
    for p in op["params"]:
        if _shown(op, p) and not p["required"]:
            fields.append(f"{p['name']}: {_lit(_value(op, p, ctx), p)}")
    call = f"api.{m}({{ {', '.join(fields)} }})" if fields else f"api.{m}()"

    values = ([] if op["public"] else ["Configuration"]) + [cls, "ResponseError"]
    imp = ", ".join(values + ([f"type {bm}"] if bm else []))
    out = _header(op, f"{ctx.pascal(op['op_id'])}.ts")
    if kind == "binary":
        out += ['import { writeFile } from "node:fs/promises";', 'import { resolve } from "node:path";']
    out.append(f'import {{ {imp} }} from "{ctx.LANGS[LANG]["pkg"]}";')
    out.append("")
    if op["public"]:
        out += ["// Public endpoint: no API key needed.", f"const api = new {cls}();"]
    else:
        out += ["// Set the API key once; the client adds it to every request.",
                "const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });",
                f"const api = new {cls}(config);"]
    out.append("")
    out += _params_comment(op, ctx, m)
    out.append("async function main(): Promise<void> {")
    out += pre
    if kind == "binary":
        fname = download_filename(op, ctx)
        out += [f"{ind}const blob = await {call}; // a Blob with the file's bytes",
                f'{ind}const file = "{fname}";',
                f"{ind}await writeFile(file, new Uint8Array(await blob.arrayBuffer()));",
                f"{ind}console.log(`Saved ${{blob.size}} bytes to ${{resolve(file)}}`);"]
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
            "main().catch(async (err: unknown) => {",
            "  // API errors carry the HTTP response",
            "  if (err instanceof ResponseError) {",
            "    console.error(`HTTP ${err.response.status}: ${await err.response.text()}`);",
            "  } else {",
            "    console.error(err);",
            "  }",
            "  process.exitCode = 1;",
            "});"]
    return "\n".join(out)


def getting_started(ctx):
    pkg = ctx.LANGS[LANG]["pkg"]
    cls = ctx.api_class("WHOIS", LANG)
    m = ctx.method_name("whoisLive", LANG)
    return [
        "1. Create a project and install the SDK (Node.js 18 or later), plus "
        "[tsx](https://tsx.is) to run TypeScript files directly:", "",
        "```bash",
        "mkdir whoisfreaks-test && cd whoisfreaks-test",
        "npm init -y",
        f"npm install {pkg}",
        "npm install -D tsx @types/node",
        "```", "",
        "2. Create `main.ts`:", "",
        "```typescript",
        f'import {{ Configuration, {cls}, ResponseError }} from "{pkg}";',
        "",
        "// Set the API key once; the client adds it to every request.",
        "const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });",
        f"const api = new {cls}(config);",
        "",
        "async function main(): Promise<void> {",
        f'  const record = await api.{m}({{ domainName: "whoisfreaks.com" }});',
        '  console.log("Domain: ", record.domain_name);',
        '  console.log("Created:", record.create_date);',
        '  console.log("Expires:", record.expiry_date);',
        "}",
        "",
        "main().catch(async (err: unknown) => {",
        "  if (err instanceof ResponseError) {",
        "    console.error(`HTTP ${err.response.status}: ${await err.response.text()}`);",
        "  } else {",
        "    console.error(err);",
        "  }",
        "  process.exitCode = 1;",
        "});",
        "```", "",
        "3. Set your API key and run it:", "",
        "```bash",
        'export WHOISFREAKS_API_KEY="your_api_key"   # PowerShell: $env:WHOISFREAKS_API_KEY="your_api_key"',
        "npx tsx main.ts",
        "```", "",
        "`tsx` runs the file without a separate compile step. To type-check as well, "
        "add the compiler and run it in strict mode:", "",
        "```bash",
        "npm install -D typescript",
        "npx tsc --noEmit --strict --module nodenext --types node main.ts",
        "```",
    ]
