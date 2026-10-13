"""PHP example renderer for gen_docs.py (SDK: whoisfreaks/whoisfreaks-php).

Matches the generated PHP client: positional arguments in the generated order
(required params in spec order, then the request body, then optional params in
spec order), API classes named like WHOISApi, models in WhoisFreaks\\Model, and
downloads returned as an \\SplFileObject temp file.
"""
import re

FILES_HOST = "files.whoisfreaks.com"
# Optional params worth showing; every other optional param is left at its default.
SHOWN_OPTIONALS = {"domainName", "keyword", "sug", "count", "page"}
VALUE_OVERRIDES = {"sug": True}     # suggestions only matter when turned on


# ---- shared helpers (kept local to this module) -----------------------------
def _is_db(op):
    return FILES_HOST in (op.get("server") or "")


def _shown(op, p):
    if p["required"] or p["name"] in SHOWN_OPTIONALS:
        return True
    return p["name"] == "date" and _is_db(op)


def _value(p, ctx):
    return VALUE_OVERRIDES.get(p["name"], ctx.example_value(p))


def _params(op):
    return [p for p in op["params"] if p["name"] != "apiKey"]


def _response(op, ctx):
    item = ctx.spec["paths"][op["path"]][op["method"].lower()]
    return ctx.deref((item.get("responses") or {}).get("200") or {})


def _return_kind(op, ctx):
    """file | model | models | strings | string"""
    if op.get("is_binary"):
        return "file"
    if op.get("response_schema"):
        return "models" if op.get("response_is_array") else "model"
    for c in (_response(op, ctx).get("content") or {}).values():
        sch = ctx.deref(c.get("schema") or {})
        return "strings" if sch.get("type") == "array" else "string"
    return "string"


def _download_name(op, ctx):
    return ctx.download_name(op)


def _body_fields(op, ctx):
    """[(jsonField, value)] for the request body, in the model's property order."""
    ex = ctx.body_example(op)
    order = list(((op.get("body_schema") or {}).get("properties") or {}).keys())
    return sorted(ex.items(), key=lambda kv: order.index(kv[0]) if kv[0] in order else len(order))


def _camel(name):
    parts = [w for w in re.split(r"[^A-Za-z0-9]+", name) if w]
    return parts[0][:1].lower() + parts[0][1:] + "".join(w[:1].upper() + w[1:] for w in parts[1:])


# ---- PHP rendering -----------------------------------------------------------
def _lit(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if v is None:
        return "null"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, (list, tuple)):
        return "[" + ", ".join(_lit(x) for x in v) + "]"
    return "'" + str(v).replace("\\", "\\\\").replace("'", "\\'") + "'"


def _args(op, ctx):
    """Positional (name, code) pairs up to the last argument worth passing.
    Skipped optionals before it are filled with their default value."""
    params = _params(op)
    seq = [("p", p) for p in params if p["required"]]
    if op.get("body_model"):
        seq.append(("body", None))
    seq += [("p", p) for p in params if not p["required"]]
    out, pending = [], []
    for kind, p in seq:
        if kind == "body":
            bm = op["body_model"]
            out += pending + [(bm[:1].lower() + bm[1:], "$request")]
            pending = []
        elif _shown(op, p):
            out += pending + [(p["name"], _lit(_value(p, ctx)))]
            pending = []
        else:
            pending.append((p["name"], _lit(p.get("default"))))
    return out


def _header(op, ctx):
    return f"// {op['summary'] or op['op_id']}\n//\n" + ctx.params_comment("php", op)


def _setup(cls, extra_uses=(), public=False):
    uses = sorted({"GuzzleHttp\\Client", f"WhoisFreaks\\Api\\{cls}", "WhoisFreaks\\ApiException",
                   "WhoisFreaks\\Configuration", *extra_uses}, key=str.lower)
    lines = ["require __DIR__ . '/vendor/autoload.php';", ""]
    lines += [f"use {u};" for u in uses]
    lines += ["", "// Read the API key from the environment and set it once."]
    if public:
        lines.append("// (This endpoint is public, so the key is not sent with this request.)")
    lines += ["$config = Configuration::getDefaultConfiguration()",
              "    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));", "",
              f"$api = new {cls}(new Client(), $config);"]
    return lines


def example(op, ctx):
    cls = ctx.api_class(op["tag"], "php")
    method = ctx.method_name(op["op_id"], "php")
    args = _args(op, ctx)
    call = f"$api->{method}({', '.join(code for _, code in args)});"
    if len(args) > 1:
        call += "  // " + ", ".join(name for name, _ in args)

    uses, pre = [], []
    if op.get("body_model"):
        bm = op["body_model"]
        uses.append(f"WhoisFreaks\\Model\\{bm}")
        pre += ["", f"$request = new {bm}(["]
        pre += [f"    '{_camel(k)}' => {_lit(v)}," for k, v in _body_fields(op, ctx)]
        pre += ["]);"]

    kind = _return_kind(op, ctx)
    body = []
    if kind == "file":
        name = _download_name(op, ctx)
        body = [f"    $file = {call}",
                "    // The SDK streams the download into a temporary file: copy it somewhere permanent.",
                f"    $saveAs = '{name}';",
                "    copy($file->getPathname(), $saveAs);",
                "    echo 'Saved ', realpath($saveAs), ' (', filesize($saveAs), ' bytes)', PHP_EOL;"]
    elif kind == "model":
        body = [f"    $result = {call}", "    echo $result, PHP_EOL;  // models print as JSON"]
    elif kind == "models":
        body = [f"    $results = {call}", "    foreach ($results as $result) {",
                "        echo $result, PHP_EOL;  // models print as JSON", "    }"]
    elif kind == "strings":
        body = [f"    $domains = {call}", "    echo implode(PHP_EOL, $domains), PHP_EOL;"]
    else:
        if op["op_id"] == "rotateApiKey":
            body = [f"    $newKey = {call}",
                    "    // The old key stops working now: store the new one before making more calls.",
                    "    echo 'New API key: ', $newKey, PHP_EOL;"]
        else:
            body = [f"    $result = {call}", "    echo $result, PHP_EOL;"]

    lines = ["<?php", _header(op, ctx), ""] + _setup(cls, uses, op.get("public")) + pre
    lines += ["", "try {"] + body + [
        "} catch (ApiException $e) {",
        "    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);",
        "    exit(1);",
        "}"]
    return "\n".join(lines) + "\n"


def getting_started(ctx):
    pkg = ctx.LANGS["php"]["pkg"]
    return [
        "You need PHP 7.4 or later (PHP 8 supported) and [Composer](https://getcomposer.org).", "",
        "1. Create a project and install the SDK:", "",
        "```bash",
        "mkdir whoisfreaks-test && cd whoisfreaks-test",
        f"composer require {pkg}",
        "```", "",
        "2. Create `main.php`:", "",
        "```php",
        "<?php",
        "require __DIR__ . '/vendor/autoload.php';",
        "",
        "use GuzzleHttp\\Client;",
        "use WhoisFreaks\\Api\\WHOISApi;",
        "use WhoisFreaks\\Configuration;",
        "",
        "// Read the API key from the environment and set it once.",
        "$config = Configuration::getDefaultConfiguration()",
        "    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));",
        "",
        "$whois = new WHOISApi(new Client(), $config);",
        "$record = $whois->whoisLive('whoisfreaks.com');",
        "",
        "echo 'Registrar: ', $record->getDomainRegistrar()->getRegistrarName(), PHP_EOL;",
        "echo 'Created:   ', $record->getCreateDate(), PHP_EOL;",
        "echo 'Expires:   ', $record->getExpiryDate(), PHP_EOL;",
        "```", "",
        "3. Set your API key and run it:", "",
        "```bash",
        'export WHOISFREAKS_API_KEY="your_api_key"',
        "php main.php",
        "```",
    ]
