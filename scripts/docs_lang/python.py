"""Python example renderer for gen_docs.py (SDK: `whoisfreaks` on PyPI).

Matches the openapi-generator `python` (pydantic v2) client:
  * auth: Configuration().api_key["ApiKeyAuth"], set once, read from WHOISFREAKS_API_KEY
  * required params are positional, in spec order, then the request body;
    optional params are keyword arguments with snake_case names
  * a param that clashes with a Python name gets a `var_` prefix (`date` -> `var_date`);
    `type` and `format` keep their names
  * `format: date` params take a datetime.date; other dates stay strings
  * request bodies are model instances, e.g. BulkWhoisRequest(domain_names=[...])
  * downloads return bytes (a bytearray), written to a file
"""
import json

LANG = "python"

# openapi-generator's Python reserved words: a param with one of these names is
# emitted as var_<name>. `type` and `format` are NOT reserved (checked against the SDK).
_RESERVED = {
    "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del",
    "elif", "else", "except", "exec", "finally", "for", "from", "global", "if", "import",
    "in", "is", "lambda", "nonlocal", "not", "or", "pass", "print", "raise", "return",
    "try", "while", "with", "yield", "self", "none", "true", "false", "property",
    "schema", "base64", "json", "date", "datetime", "float",
}

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


def _py_name(name, ctx):
    s = ctx.py_snake(name)
    return "var_" + s if s in _RESERVED else s


def _is_date(p):
    return p.get("format") == "date"


def _lit(v, p=None):
    """A Python literal for v; format: date params become date(Y, M, D)."""
    if p is not None and _is_date(p):
        y, m, d = (int(x) for x in str(v).split("-"))
        return f"date({y}, {m}, {d})"
    if isinstance(v, bool):
        return "True" if v else "False"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, (list, dict, str)):
        return json.dumps(v)
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
    if _is_date(p):
        return "datetime.date"
    return {"integer": "int", "boolean": "bool", "number": "float"}.get(p.get("type"), "str")


def _params_comment(op, ctx, method, ind):
    lines = [f"{ind}# {method} parameters:"]
    req = [p for p in op["params"] if p["name"] != "apiKey" and p["required"]]
    opt = [p for p in op["params"] if p["name"] != "apiKey" and not p["required"]]
    def line(p, kind):
        t = _type_label(p)
        extra = []
        if p.get("enum"):
            extra.append("one of " + ", ".join(str(e) for e in p["enum"]))
        if p.get("default") is not None:
            extra.append(f"default {_lit(p['default'])}")
        desc = _clean(p.get("desc") or "").rstrip(".")
        if len(desc) > 80:
            desc = desc[:77] + "..."
        tail = "; ".join(x for x in [desc] + extra if x)
        return f"{ind}#   {_py_name(p['name'], ctx)} ({t}, {kind})" + (f": {tail}" if tail else "")
    for p in req:
        lines.append(line(p, "required"))
    if op.get("body_model"):
        lines.append(f"{ind}#   {ctx.py_snake(op['body_model'])} ({op['body_model']}, required): request body")
    for p in opt:
        lines.append(line(p, "optional, keyword"))
    if len(lines) == 1:
        return [f"{ind}# {method} takes no parameters."]
    return lines


def _call_lines(op, ctx, ind):
    """(pre_lines, call_expr, uses_date) for the SDK call."""
    m = ctx.method_name(op["op_id"], LANG)
    args, kwargs, pre, uses_date = [], [], [], False
    for p in op["params"]:
        if _shown(op, p) and p["required"]:
            args.append(_lit(_value(op, p, ctx), p))
            uses_date |= _is_date(p)
    bm = op.get("body_model")
    if bm:
        fields = ", ".join(f"{ctx.py_snake(k)}={_lit(v)}" for k, v in ctx.body_example(op).items())
        pre.append(f"{ind}body = whoisfreaks.{bm}({fields})")
        args.append("body")
    for p in op["params"]:
        if _shown(op, p) and not p["required"]:
            kwargs.append(f"{_py_name(p['name'], ctx)}={_lit(_value(op, p, ctx), p)}")
            uses_date |= _is_date(p)
    return pre, f"api.{m}({', '.join(args + kwargs)})", uses_date


def _header(op, run_file):
    run = (["Run it (public endpoint, no API key needed):", f"    python {run_file}"] if op["public"] else
           ["Run it with your API key in the environment:",
            f"    WHOISFREAKS_API_KEY=your_api_key python {run_file}"])
    return [f'"""{_clean(op["summary"] or op["op_id"])}: {op["method"]} {op["server"]}{op["path"]}', ""] \
        + run + ['"""']


def example(op, ctx):
    cls = ctx.api_class(op["tag"], LANG)
    m = ctx.method_name(op["op_id"], LANG)
    kind = _response_kind(op, ctx)
    ind = "    "
    pre, call, uses_date = _call_lines(op, ctx, ind)
    imports = []
    if kind in ("model", "model_list"):
        imports.append("import json")
    if kind == "binary" or not op["public"]:
        imports.append("import os")
    if uses_date:
        imports.append("from datetime import date")
    out = _header(op, f"{ctx.pascal(op['op_id'])}.py")
    out += imports + ["", "import whoisfreaks", ""]
    out.append("config = whoisfreaks.Configuration()")
    if op["public"]:
        out.append("# Public endpoint: no API key needed.")
    else:
        out.append('config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request')
    out += ["", "with whoisfreaks.ApiClient(config) as client:", f"{ind}api = whoisfreaks.{cls}(client)", ""]
    out += _params_comment(op, ctx, m, ind)
    out += pre
    if kind == "binary":
        fname = download_filename(op, ctx)
        out += [f"{ind}data = {call}  # the file's raw bytes",
                f'{ind}path = "{fname}"',
                f'{ind}with open(path, "wb") as f:',
                f"{ind}    f.write(data)",
                f'{ind}print(f"Saved {{len(data)}} bytes to {{os.path.abspath(path)}}")']
    elif kind == "model_list":
        out += [f"{ind}results = {call}",
                f"{ind}print(json.dumps([item.to_dict() for item in results], indent=2))"]
    elif kind == "string_list":
        out += [f"{ind}domains = {call}",
                f'{ind}print(f"{{len(domains)}} domains")',
                f'{ind}print("\\n".join(domains[:10]))']
    elif kind == "text":
        out += [f"{ind}new_key = {call}  # use this key from now on",
                f'{ind}print("New API key:", new_key)']
    else:
        out += [f"{ind}result = {call}",
                f"{ind}print(json.dumps(result.to_dict(), indent=2))"]
    return "\n".join(out)


def getting_started(ctx):
    pkg = ctx.LANGS[LANG]["pkg"]
    cls = ctx.api_class("WHOIS", LANG)
    m = ctx.method_name("whoisLive", LANG)
    return [
        "1. Create a project folder with a virtual environment and install the SDK:", "",
        "```bash",
        "mkdir whoisfreaks-test && cd whoisfreaks-test",
        "python3 -m venv .venv",
        "source .venv/bin/activate   # Windows: .venv\\Scripts\\activate",
        f"pip install {pkg}",
        "```", "",
        "2. Create `main.py`:", "",
        "```python",
        "import os",
        "",
        "import whoisfreaks",
        "",
        "config = whoisfreaks.Configuration()",
        'config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request',
        "",
        "with whoisfreaks.ApiClient(config) as client:",
        f'    record = whoisfreaks.{cls}(client).{m}("whoisfreaks.com")',
        '    print("Domain: ", record.domain_name)',
        '    print("Created:", record.create_date)',
        '    print("Expires:", record.expiry_date)',
        "```", "",
        "3. Set your API key and run it:", "",
        "```bash",
        'export WHOISFREAKS_API_KEY="your_api_key"   # PowerShell: $env:WHOISFREAKS_API_KEY="your_api_key"',
        "python main.py",
        "```",
    ]
