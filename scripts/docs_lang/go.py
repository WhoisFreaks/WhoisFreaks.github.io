"""Go example renderer (github.com/<OWNER>/whoisfreaks-go).

Requests use the generated builder pattern: client.<Tag>API.<Op>(ctx).<Param>(v)
...Execute(). The API key travels in the context (ContextAPIKeys, scheme
"ApiKeyAuth"). The `type` param's setter is Type_ (reserved word), dates are
plain "YYYY-MM-DD" strings, and downloads return a temporary *os.File that the
example copies to its destination.
"""
import json

ENV = "WHOISFREAKS_API_KEY"
GO_KEYWORDS = {"break", "case", "chan", "const", "continue", "default", "defer", "else",
               "fallthrough", "for", "func", "go", "goto", "if", "import", "interface",
               "map", "package", "range", "return", "select", "struct", "switch", "type", "var"}

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


def _exported(name):
    s = name[0].upper() + name[1:]
    return s + "_" if name in GO_KEYWORDS else s


def _lit(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, (list, tuple)):
        items = [_lit(x) for x in v]
        kind = "string" if all(isinstance(x, str) for x in v) else "interface{}"
        return f"[]{kind}{{" + ", ".join(items) + "}"
    return json.dumps(str(v))


def _body(op, ctx, alias):
    """Lines building `body` with the model constructor (required fields) and setters."""
    model = op["body_model"]
    sch = op.get("body_schema") or {}
    required = set(sch.get("required") or [])
    fields = ctx.body_example(op)
    ctor = [k for k in (sch.get("properties") or {}) if k in required]
    args = ", ".join(_lit(fields.get(k, [])) for k in ctor)
    lines = [f"\tbody := {alias}.New{model}({args})"]
    for k, v in fields.items():
        if k not in required:
            lines.append(f"\tbody.Set{_exported(k)}({_lit(v)})")
    return lines


def _fatal():
    return ["\tif err != nil {", "\t\tlog.Fatal(err)", "\t}"]


def example(op, ctx):
    alias = "whoisfreaks"
    module = ctx.LANGS["go"]["pkg"]
    imports = {"context", "fmt", "log"}
    lines_body = []
    setters = ""
    for p in op["params"]:
        if p["name"] == "apiKey" or not _shown(p):
            continue
        setters += f".{_exported(p['name'])}({_lit(_value(p, ctx))})"
    if op.get("body_model"):
        lines_body = _body(op, ctx, alias)
        setters += f".{op['body_model']}(*body)"
    method = op["op_id"][0].upper() + op["op_id"][1:]
    head = f"client.{ctx.go_accessor(op['tag'])}.{method}(ctx)"
    call = f"{head}{setters}.Execute()"
    if len(call) > 80 and setters:
        call = f"{head}.\n\t\t{setters[1:]}.Execute()"

    main = []
    if op.get("public"):
        main += ["\t// Public endpoint: no API key needed.",
                 "\tctx := context.Background()"]
    else:
        imports.add("os")
        main += ["\t// Set the API key once on the context; every call made with ctx sends it.",
                 f"\tctx := context.WithValue(context.Background(), {alias}.ContextAPIKeys,",
                 f'\t\tmap[string]{alias}.APIKey{{"ApiKeyAuth": {{Key: os.Getenv("{ENV}")}}}})']
    main += [f"\tclient := {alias}.NewAPIClient({alias}.NewConfiguration())", ""]
    main += lines_body

    if op.get("is_binary"):
        imports.update({"io", "os", "path/filepath"})
        name = ctx.download_name(op)
        main += [f"\tfile, _, err := {call}"] + _fatal() + [
            "\t// The SDK saves the response to a temporary file: copy it to its destination.",
            "\tdefer os.Remove(file.Name())",
            "\tdefer file.Close()",
            "",
            f'\tout, err := os.Create("{name}")'] + _fatal() + [
            "\tdefer out.Close()",
            "\tn, err := io.Copy(out, file)"] + _fatal() + [
            "\tpath, _ := filepath.Abs(out.Name())",
            '\tfmt.Printf("Saved %d bytes to %s\\n", n, path)']
    elif op["op_id"] == "rotateApiKey":
        main += [f"\tnewKey, _, err := {call}"] + _fatal() + [
            "\t// The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.",
            '\tfmt.Println("New API key:", newKey)']
    else:
        imports.add("encoding/json")
        main += [f"\tresult, _, err := {call}"] + _fatal() + [
            '\tout, _ := json.MarshalIndent(result, "", "  ")',
            "\tfmt.Println(string(out))"]

    pc = ctx.params_comment("go", op)
    if op.get("public"):
        pc = pc.replace("(no parameters; the API key is set on the client)",
                        "(no parameters; public endpoint, no API key needed)")
    lines = [f"// Runnable example: {op['summary']} ({op['method']} {op['path']})",
             "// Run it from the Getting Started module: save it as main.go, then `go run .`",
             pc, "", "package main", "", "import ("]
    lines += [f'\t"{i}"' for i in sorted(imports)]
    lines += ["", f'\t{alias} "{module}"', ")", "", "func main() {"] + main + ["}"]
    return "\n".join(lines) + "\n"


def getting_started(ctx):
    module = ctx.LANGS["go"]["pkg"]
    v = ctx.SDK_VERSION
    return [
        "You need Go 1.18 or later. Create a module and add the SDK:", "",
        "```bash",
        "mkdir whoisfreaks-test && cd whoisfreaks-test",
        "go mod init whoisfreaks-test",
        f"go get {module}@v{v}",
        "```", "",
        "Create `main.go`:", "",
        "```go",
        "package main",
        "",
        "import (",
        '\t"context"',
        '\t"fmt"',
        '\t"log"',
        '\t"os"',
        "",
        f'\twhoisfreaks "{module}"',
        ")",
        "",
        "func main() {",
        "\t// Set the API key once on the context; every call made with ctx sends it.",
        "\tctx := context.WithValue(context.Background(), whoisfreaks.ContextAPIKeys,",
        f'\t\tmap[string]whoisfreaks.APIKey{{"ApiKeyAuth": {{Key: os.Getenv("{ENV}")}}}})',
        "\tclient := whoisfreaks.NewAPIClient(whoisfreaks.NewConfiguration())",
        "",
        '\trecord, _, err := client.WHOISAPI.WhoisLive(ctx).DomainName("whoisfreaks.com").Execute()',
        "\tif err != nil {",
        "\t\tlog.Fatal(err)",
        "\t}",
        '\tfmt.Println(record.GetDomainName(), "expires", record.GetExpiryDate())',
        "}",
        "```", "",
        "Set your API key, tidy the module and run it:", "",
        "```bash",
        f'export {ENV}="your_api_key"',
        "go mod tidy",
        "go run .",
        "```", "",
        "To run one of the [runnable examples](../../examples/go/README.md), save it as "
        "`main.go` in this module and run `go run .` again.",
    ]
