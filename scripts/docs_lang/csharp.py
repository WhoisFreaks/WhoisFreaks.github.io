"""C# example renderer (NuGet package WhoisFreaks, httpclient library, net8.0).

Examples are top-level-statement programs (a `dotnet new console` Program.cs).
API classes keep acronyms upper case (WHOISApi, DatabasesDNSApi). The API key
name is "apiKey"; BasePath is left alone so database operations reach the files
host. Optional params are C# optional arguments, so examples pass the ones they
show by name. Dates are DateOnly; downloads return a FileParameter whose
Content stream is copied to a file.
"""
import json

ENV = "WHOISFREAKS_API_KEY"

# Optional params worth showing: the date on database downloads, suggestions on
# availability, the page on paginated lookups, and the lookup subject where the
# spec marks it optional (dnsLive domainName, typosquatting keyword).
_SHOWN = {"date", "sug", "count", "page", "domainName", "keyword"}


def _shown(p):
    return p["required"] or p["name"] in _SHOWN


def _value(p, ctx):
    if p["name"] == "sug":
        return True          # suggestions on, so `count` means something
    return ctx.example_value(p)


def _signature(op):
    """SDK argument order: required params, then the request body, then optionals."""
    params = [p for p in op["params"] if p["name"] != "apiKey"]
    body = [None] if op.get("body_model") else []
    return [p for p in params if p["required"]] + body + [p for p in params if not p["required"]]


def _response(op, ctx):
    path = ctx.spec["paths"][op["path"]][op["method"].lower()]
    return ctx.deref((path.get("responses") or {}).get("200") or {})


def _returns(op, ctx):
    """('file'|'model'|'models'|'strings'|'string', model name or None)."""
    if op.get("is_binary"):
        return "file", None
    for _ct, media in (_response(op, ctx).get("content") or {}).items():
        sch = ctx.deref(media).get("schema") or {}
        if "$ref" in sch:
            return "model", sch["$ref"].split("/")[-1]
        if sch.get("type") == "array":
            items = sch.get("items") or {}
            if "$ref" in items:
                return "models", items["$ref"].split("/")[-1]
            return "strings", None
        if sch.get("type") == "string":
            return "string", None
    return "string", None


def _lit(v, p=None):
    if p and p.get("format") == "date":
        y, m, d = (int(x) for x in str(v).split("-"))
        return f"new DateOnly({y}, {m}, {d})"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, (list, tuple)):
        return "new List<string> { " + ", ".join(_lit(x) for x in v) + " }"
    return json.dumps(str(v))


def example(op, ctx):
    api = ctx.api_class(op["tag"], "csharp")
    method = op["op_id"][0].upper() + op["op_id"][1:]
    usings = {"System", "WhoisFreaks.Api", "WhoisFreaks.Client"}

    body, args, named = [], [], False
    for p in _signature(op):
        if p is None:
            model = op["body_model"]
            usings.update({"System.Collections.Generic", "WhoisFreaks.Model"})
            fields = ", ".join(f"{k}: {_lit(v)}" for k, v in ctx.body_example(op).items())
            body = [f"var body = new {model}({fields});"]
            pname = model[0].lower() + model[1:]
            args.append(f"{pname}: body" if named else "body")
        elif not _shown(p):
            named = True     # skipped optional: everything after it is named
        else:
            lit = _lit(_value(p, ctx), p)
            if named or not p["required"]:
                named = True
                args.append(f"{p['name']}: {lit}")
            else:
                args.append(lit)
    call = f"api.{method}({', '.join(args)})"

    kind, model = _returns(op, ctx)
    out = []
    if kind == "file":
        usings.add("System.IO")
        name = ctx.download_name(op)
        out += [f"FileParameter download = {call};",
                "// The SDK returns the response body as a stream: copy it to a file.",
                f'var path = Path.GetFullPath("{name}");',
                "using (Stream input = download.Content)",
                "using (FileStream output = File.Create(path))",
                "{",
                "    input.CopyTo(output);",
                "}",
                'Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");']
    elif op["op_id"] == "rotateApiKey":
        out += [f"string newKey = {call};",
                "// The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.",
                'Console.WriteLine($"New API key: {newKey}");']
    elif kind in ("models", "strings"):
        usings.add("System.Collections.Generic")
        item = model or "string"
        if model:
            usings.add("WhoisFreaks.Model")
        out += [f"List<{item}> result = {call};",
                "foreach (var item in result)",
                "{",
                "    Console.WriteLine(item.ToJson());" if model else "    Console.WriteLine(item);",
                "}"]
    else:
        rtype = model or "string"
        if model:
            usings.add("WhoisFreaks.Model")
        out += [f"{rtype} result = {call};",
                "Console.WriteLine(result.ToJson());" if model else "Console.WriteLine(result);"]

    pc = ctx.params_comment("csharp", op)
    if op.get("public"):
        pc = pc.replace("(no parameters; the API key is set on the client)",
                        "(no parameters; public endpoint, no API key needed)")
    lines = [f"// Runnable example: {op['summary']} ({op['method']} {op['path']})",
             "// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`",
             pc]
    order = ["System", "System.Collections.Generic", "System.IO",
             "WhoisFreaks.Api", "WhoisFreaks.Client", "WhoisFreaks.Model"]
    lines += [f"using {u};" for u in order if u in usings]
    lines += [""]
    lines += ["var config = new Configuration();"]
    if op.get("public"):
        lines += ["// Public endpoint: no API key needed."]
    else:
        lines += [f'var apiKey = Environment.GetEnvironmentVariable("{ENV}")',
                  f'    ?? throw new InvalidOperationException("Set the {ENV} environment variable");',
                  'config.AddApiKey("apiKey", apiKey);  // set once, sent with every call']
    lines += [f"var api = new {api}(config);", ""]
    lines += body + out
    return "\n".join(lines) + "\n"


def getting_started(ctx):
    pkg = ctx.LANGS["csharp"]["pkg"]
    v = ctx.SDK_VERSION
    return [
        "You need the .NET 8 SDK or later. Create a console app and add the package:", "",
        "```bash",
        "dotnet new console -o whoisfreaks-test",
        "cd whoisfreaks-test",
        f"dotnet add package {pkg} --version {v}",
        "```", "",
        "Replace `Program.cs` with:", "",
        "```csharp",
        "using System;",
        "using WhoisFreaks.Api;",
        "using WhoisFreaks.Client;",
        "using WhoisFreaks.Model;",
        "",
        "var config = new Configuration();",
        f'var apiKey = Environment.GetEnvironmentVariable("{ENV}")',
        f'    ?? throw new InvalidOperationException("Set the {ENV} environment variable");',
        'config.AddApiKey("apiKey", apiKey);  // set once, sent with every call',
        "",
        "var whois = new WHOISApi(config);",
        'WhoisResponse record = whois.WhoisLive("whoisfreaks.com");',
        'Console.WriteLine($"{record.DomainName} expires {record.ExpiryDate}");',
        "Console.WriteLine(record.ToJson());",
        "```", "",
        "Set your API key and run it:", "",
        "```bash",
        f'export {ENV}="your_api_key"',
        "dotnet run",
        "```", "",
        "To run one of the [runnable examples](../../examples/csharp/README.md), use it "
        "as `Program.cs` and run `dotnet run` again.",
    ]
