"""Swift example renderer for gen_docs.py (SDK: github.com/WhoisFreaks/whoisfreaks-swift).

Matches the generated Swift client: async/await class methods on API types
named like WHOISAPI, labels in the generated order (required params in spec
order, then the request body, then optional params in spec order), typed enums
for enum params, OpenAPIDateWithoutTime for date params, the key set once on
WhoisFreaksAPI.apiKey, and downloads returned as a file URL. Examples are
top-level code for an executable target's main.swift.
"""
import re

FILES_HOST = "files.whoisfreaks.com"
# Optional params worth showing; every other optional param is left at its default.
SHOWN_OPTIONALS = {"domainName", "keyword", "sug", "count", "page"}
VALUE_OVERRIDES = {"sug": True}     # suggestions only matter when turned on
TOOLS_VERSION = "5.7"               # top-level await in main.swift needs Swift 5.7


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


# ---- Swift rendering ---------------------------------------------------------
def _str(v):
    return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'


def _lit(v, p=None):
    if p is not None:
        if p.get("enum"):
            return "." + _camel(str(v))                       # typed enum case, e.g. .a
        if p.get("format") == "date":
            return f"OpenAPIDateWithoutTime(rawValue: {_str(v)})!"
    if isinstance(v, bool):
        return "true" if v else "false"
    if v is None:
        return "nil"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, (list, tuple)):
        return "[" + ", ".join(_lit(x) for x in v) + "]"
    return _str(v)


def _call_args(op, ctx):
    params = _params(op)
    args = [f"{p['name']}: {_lit(_value(p, ctx), p)}" for p in params if p["required"]]
    if op.get("body_model"):
        bm = op["body_model"]
        args.append(f"{bm[:1].lower() + bm[1:]}: request")
    args += [f"{p['name']}: {_lit(_value(p, ctx), p)}"
             for p in params if not p["required"] and _shown(op, p)]
    return ", ".join(args)


def _header(op, ctx):
    return (f"// {op['summary'] or op['op_id']}\n//\n" + ctx.params_comment("swift", op) + "\n//\n"
            "// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).")


SETUP = ["import Foundation", "import WhoisFreaks", "",
         "// Read the API key from the environment and set it once.",
         'WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]']

CATCH = ["} catch ErrorResponse.error(let status, let data, _, let underlying) {",
         '    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\\(underlying)"',
         '    print("Request failed: HTTP \\(status) \\(body)")',
         "    exit(1)",
         "} catch {",
         '    print("Request failed: \\(error)")',
         "    exit(1)",
         "}"]


def example(op, ctx):
    cls = ctx.api_class(op["tag"], "swift")
    method = ctx.method_name(op["op_id"], "swift")
    call = f"try await {cls}.{method}({_call_args(op, ctx)})"
    kind = _return_kind(op, ctx)

    lines = [_header(op, ctx), ""] + SETUP
    if op.get("public"):
        lines.append("// (This endpoint is public, so the key is not sent with this request.)")
    if op.get("body_model"):
        fields = ", ".join(f"{_camel(k)}: {_lit(v)}" for k, v in _body_fields(op, ctx))
        lines += ["", f"let request = {op['body_model']}({fields})"]

    if kind == "file":
        body = [f"    let file = {call}",
                "    // The SDK saves the download under the caches directory: move it somewhere permanent.",
                f'    let saveAs = URL(fileURLWithPath: "{_download_name(op, ctx)}")',
                "    try? FileManager.default.removeItem(at: saveAs)",
                "    try FileManager.default.moveItem(at: file, to: saveAs)",
                '    print("Saved \\(saveAs.path)")']
    elif kind in ("model", "models"):
        body = [f"    let result = {call}",
                "    print(String(decoding: try CodableHelper.jsonEncoder.encode(result), as: UTF8.self))"]
    elif kind == "strings":
        body = [f"    let domains = {call}", '    print(domains.joined(separator: "\\n"))']
    elif op["op_id"] == "rotateApiKey":
        body = [f"    let newKey = {call}",
                "    // The old key stops working now: store the new one before making more calls.",
                '    print("New API key: \\(newKey)")']
    else:
        body = [f"    let result = {call}", "    print(result)"]

    lines += ["", "do {"] + body + CATCH
    return "\n".join(lines) + "\n"


def getting_started(ctx):
    pkg = ctx.LANGS["swift"]["pkg"]
    repo = pkg.rsplit("/", 1)[-1]                 # SwiftPM package identity, e.g. whoisfreaks-swift
    v = ctx.SDK_VERSION
    return [
        f"You need Swift {TOOLS_VERSION} or later (Xcode 14+) on macOS 10.15 or later. "
        "The SDK uses async/await.", "",
        "1. Create an executable package:", "",
        "```bash",
        "mkdir -p whoisfreaks-test/Sources/WhoisFreaksTest",
        "cd whoisfreaks-test",
        "```", "",
        "2. Create `Package.swift` with the SDK as a dependency:", "",
        "```swift",
        f"// swift-tools-version:{TOOLS_VERSION}",
        "import PackageDescription",
        "",
        "let package = Package(",
        '    name: "WhoisFreaksTest",',
        "    platforms: [.macOS(.v10_15)],",
        "    dependencies: [",
        f'        .package(url: "https://{pkg}.git", from: "{v}"),',
        "    ],",
        "    targets: [",
        "        .executableTarget(",
        '            name: "WhoisFreaksTest",',
        f'            dependencies: [.product(name: "WhoisFreaks", package: "{repo}")]',
        "        ),",
        "    ]",
        ")",
        "```", "",
        "3. Create `Sources/WhoisFreaksTest/main.swift`:", "",
        "```swift",
        "import Foundation",
        "import WhoisFreaks",
        "",
        "// Read the API key from the environment and set it once.",
        'WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]',
        "",
        'let record = try await WHOISAPI.whoisLive(domainName: "whoisfreaks.com")',
        "",
        'print("Registrar:", record.domainRegistrar?.registrarName ?? "-")',
        'print("Created:  ", record.createDate ?? "-")',
        'print("Expires:  ", record.expiryDate ?? "-")',
        "```", "",
        "4. Set your API key and run it:", "",
        "```bash",
        'export WHOISFREAKS_API_KEY="your_api_key"',
        "swift run",
        "```",
    ]
