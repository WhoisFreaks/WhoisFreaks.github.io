"""Ruby example renderer for gen_docs.py (SDK: the whoisfreaks gem).

Matches the generated Ruby client: required params are positional (spec order,
then the request body), optional params go in the trailing opts hash as
snake_case keywords, API classes are named like WhoisFreaks::WHOISApi, and
downloads come back as a Tempfile that is deleted when the program exits.
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


# ---- Ruby rendering ----------------------------------------------------------
def _lit(v, p=None):
    if p is not None and p.get("format") == "date" and isinstance(v, str):
        return f'Date.parse("{v}")'        # the generated client documents Date for these
    if isinstance(v, bool):
        return "true" if v else "false"
    if v is None:
        return "nil"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, (list, tuple)):
        return "[" + ", ".join(_lit(x) for x in v) + "]"
    return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"').replace("#{", "\\#{") + '"'


def _call_args(op, ctx):
    params = _params(op)
    pos = [_lit(_value(p, ctx), p) for p in params if p["required"]]
    if op.get("body_model"):
        pos.append("request")
    opts = [f"{ctx.py_snake(p['name'])}: {_lit(_value(p, ctx), p)}"
            for p in params if not p["required"] and _shown(op, p)]
    return ", ".join(pos + opts)


def _uses_date(op, ctx):
    return any(p.get("format") == "date" and _shown(op, p) for p in _params(op))


def _header(op, ctx):
    # parameter names as the Ruby client spells them (snake_case)
    cmt = re.sub(r"^(#   - )(\w+)", lambda m: m.group(1) + ctx.py_snake(m.group(2)),
                 ctx.params_comment("ruby", op), flags=re.M)
    return f"# {op['summary'] or op['op_id']}\n#\n" + cmt


def example(op, ctx):
    cls = ctx.api_class(op["tag"], "ruby")
    method = ctx.method_name(op["op_id"], "ruby")
    args = _call_args(op, ctx)
    call = f"api.{method}({args})" if args else f"api.{method}"
    kind = _return_kind(op, ctx)

    requires = []
    if _uses_date(op, ctx):
        requires.append("date")
    if kind == "file":
        requires.append("fileutils")
    if kind in ("model", "models"):
        requires.append("json")
    lines = [_header(op, ctx), ""]
    lines += [f'require "{r}"' for r in sorted(requires)] + ['require "whoisfreaks"', ""]
    lines += ["# Read the API key from the environment and set it once."]
    if op.get("public"):
        lines.append("# (This endpoint is public, so the key is not sent with this request.)")
    lines += ["WhoisFreaks.configure do |config|",
              '  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")',
              "end", "",
              f"api = WhoisFreaks::{cls}.new"]
    if op.get("body_model"):
        fields = ", ".join(f"{ctx.py_snake(k)}: {_lit(v)}" for k, v in _body_fields(op, ctx))
        lines += ["", f"request = WhoisFreaks::{op['body_model']}.new({fields})"]

    if kind == "file":
        body = [f"  file = {call}",
                "  # The SDK returns a Tempfile that is deleted when the program exits: copy it.",
                f'  save_as = "{_download_name(op, ctx)}"',
                "  FileUtils.cp(file.path, save_as)",
                '  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"']
    elif kind == "model":
        body = [f"  result = {call}", "  puts JSON.pretty_generate(result.to_hash)"]
    elif kind == "models":
        body = [f"  results = {call}", "  puts JSON.pretty_generate(results.map(&:to_hash))"]
    elif kind == "strings":
        body = [f"  domains = {call}", "  puts domains"]
    elif op["op_id"] == "rotateApiKey":
        body = [f"  new_key = {call}",
                "  # The old key stops working now: store the new one before making more calls.",
                '  puts "New API key: #{new_key}"']
    else:
        body = [f"  result = {call}", "  puts result"]

    lines += ["", "begin"] + body + [
        "rescue WhoisFreaks::ApiError => e",
        '  warn "Request failed: HTTP #{e.code} #{e.response_body}"',
        "  exit 1",
        "end"]
    return "\n".join(lines) + "\n"


def getting_started(ctx):
    pkg = ctx.LANGS["ruby"]["pkg"]
    v = ctx.SDK_VERSION
    return [
        "You need Ruby 2.7 or later and Bundler.", "",
        "1. Create a project directory:", "",
        "```bash",
        "mkdir whoisfreaks-test && cd whoisfreaks-test",
        "```", "",
        "2. Create a `Gemfile` that pins the SDK:", "",
        "```ruby",
        'source "https://rubygems.org"',
        "",
        f'gem "{pkg}", "~> {v}"',
        "```", "",
        "3. Install it:", "",
        "```bash",
        "bundle install",
        "```", "",
        "4. Create `main.rb`:", "",
        "```ruby",
        'require "whoisfreaks"',
        "",
        "# Read the API key from the environment and set it once.",
        "WhoisFreaks.configure do |config|",
        '  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")',
        "end",
        "",
        'record = WhoisFreaks::WHOISApi.new.whois_live("whoisfreaks.com")',
        "",
        'puts "Registrar: #{record.domain_registrar&.registrar_name}"',
        'puts "Created:   #{record.create_date}"',
        'puts "Expires:   #{record.expiry_date}"',
        "```", "",
        "5. Set your API key and run it:", "",
        "```bash",
        'export WHOISFREAKS_API_KEY="your_api_key"',
        "bundle exec ruby main.rb",
        "```",
    ]
