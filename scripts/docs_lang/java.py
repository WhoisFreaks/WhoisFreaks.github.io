"""Java example renderer (com.whoisfreaks:whoisfreaks, okhttp-gson client).

Signatures follow the generated Java SDK: every parameter is positional, in the
order required params, request body, optional params, so optional parameters
that the example leaves unset are passed as null. Date params are LocalDate,
downloads return a temporary java.io.File that the example moves into place.
"""
import json

ENV = "WHOISFREAKS_API_KEY"
PKG = "com.whoisfreaks.client"

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


def _str(s):
    return json.dumps(str(s))


def _lit(v, p, imports):
    if p and p.get("format") == "date":
        y, m, d = (int(x) for x in str(v).split("-"))
        imports.add("java.time.LocalDate")
        return f"LocalDate.of({y}, {m}, {d})"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, (list, tuple)):
        imports.add("java.util.Arrays")
        return "Arrays.asList(" + ", ".join(_lit(x, None, imports) for x in v) + ")"
    return _str(v)


def _header(op, ctx, cls):
    pc = ctx.params_comment("java", op)
    if op.get("public"):
        pc = pc.replace("(no parameters; the API key is set on the client)",
                        "(no parameters; public endpoint, no API key needed)")
    return [f"// Runnable example: {op['summary']} ({op['method']} {op['path']})",
            f"// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass={cls}",
            pc]


def example(op, ctx):
    cls = ctx.pascal(op["op_id"])
    api = ctx.api_class(op["tag"], "java")
    method = op["op_id"]
    imports = {f"{PKG}.ApiClient", f"{PKG}.Configuration", f"{PKG}.api.{api}"}
    if not op.get("public"):
        imports.add(f"{PKG}.auth.ApiKeyAuth")

    body = []
    args, names, skipped = [], [], False
    for p in _signature(op):
        if p is None:
            model = op["body_model"]
            imports.add(f"{PKG}.model.{model}")
            fields = ctx.body_example(op)
            chain = "".join(f"\n            .{k}({_lit(v, None, imports)})" for k, v in fields.items())
            body = [f"        {model} body = new {model}(){chain};"]
            args.append("body")
            names.append(model[0].lower() + model[1:])
        elif _shown(p):
            args.append(_lit(_value(p, ctx), p, imports))
            names.append(p["name"])
        else:
            args.append("null")
            names.append(p["name"])
            skipped = True

    kind, model = _returns(op, ctx)
    if kind == "file":
        rtype = "File"
        imports.update({"java.io.File", "java.nio.file.Files", "java.nio.file.Path",
                        "java.nio.file.Paths", "java.nio.file.StandardCopyOption"})
    elif kind == "model":
        rtype = model
        imports.add(f"{PKG}.model.{model}")
    elif kind == "models":
        rtype = f"List<{model}>"
        imports.update({f"{PKG}.model.{model}", "java.util.List"})
    elif kind == "strings":
        rtype = "List<String>"
        imports.add("java.util.List")
    else:
        rtype = "String"

    # A model named like the example class (DatabaseFileStatus) is used fully qualified.
    clash = f"{PKG}.model.{cls}"
    if clash in imports:
        imports.discard(clash)
        rtype = rtype.replace(cls, clash)

    lines = _header(op, ctx, cls)
    sdk = sorted(i for i in imports if i.startswith(PKG))
    jdk = sorted(i for i in imports if not i.startswith(PKG))
    lines += [f"import {i};" for i in sdk]
    if jdk:
        lines += [""] + [f"import {i};" for i in jdk]
    lines += ["", f"public class {cls} {{",
              "    public static void main(String[] args) throws Exception {",
              "        ApiClient client = Configuration.getDefaultApiClient();"]
    if op.get("public"):
        lines += ["        // Public endpoint: no API key needed."]
    else:
        lines += ['        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");',
                  f'        auth.setApiKey(System.getenv("{ENV}"));  // set once, sent with every call']
    lines += [f"        {api} api = new {api}(client);", ""]
    lines += body
    if skipped:
        lines += [f"        // {method}({', '.join(names)}); null leaves an optional parameter unset"]
    call = f"api.{method}({', '.join(args)})"

    if kind == "file":
        name = ctx.download_name(op)
        lines += [f"        File download = {call};",
                  "        // The SDK saves the response to a temporary file: move it where you want it.",
                  f'        Path target = Paths.get("{name}");',
                  "        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);",
                  '        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());']
    elif op["op_id"] == "rotateApiKey":
        lines += [f"        String newKey = {call};",
                  "        // The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.",
                  '        System.out.println("New API key: " + newKey);']
    else:
        lines += [f"        {rtype} result = {call};",
                  "        System.out.println(result);"]
    lines += ["    }", "}"]
    return "\n".join(lines) + "\n"


def getting_started(ctx):
    g, a = ctx.LANGS["java"]["pkg"].split(":")
    v = ctx.SDK_VERSION
    return [
        "You need JDK 8 or later and Maven. Create the project directory:", "",
        "```bash",
        "mkdir -p whoisfreaks-test/src/main/java && cd whoisfreaks-test",
        "```", "",
        "Create `pom.xml`. The `exec.mainClass` property picks the class that "
        "`mvn exec:java` runs:", "",
        "```xml",
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<project xmlns="http://maven.apache.org/POM/4.0.0"',
        '         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">',
        "  <modelVersion>4.0.0</modelVersion>",
        "  <groupId>com.example</groupId>",
        "  <artifactId>whoisfreaks-test</artifactId>",
        "  <version>1.0-SNAPSHOT</version>", "",
        "  <properties>",
        "    <maven.compiler.source>1.8</maven.compiler.source>",
        "    <maven.compiler.target>1.8</maven.compiler.target>",
        "    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>",
        "    <exec.mainClass>Main</exec.mainClass>",
        "  </properties>", "",
        "  <dependencies>",
        "    <dependency>",
        f"      <groupId>{g}</groupId>",
        f"      <artifactId>{a}</artifactId>",
        f"      <version>{v}</version>",
        "    </dependency>",
        "  </dependencies>", "",
        "  <build>",
        "    <plugins>",
        "      <plugin>",
        "        <groupId>org.codehaus.mojo</groupId>",
        "        <artifactId>exec-maven-plugin</artifactId>",
        "        <version>3.5.0</version>",
        "      </plugin>",
        "    </plugins>",
        "  </build>",
        "</project>",
        "```", "",
        "Create `src/main/java/Main.java`:", "",
        "```java",
        f"import {PKG}.ApiClient;",
        f"import {PKG}.Configuration;",
        f"import {PKG}.api.WhoisApi;",
        f"import {PKG}.auth.ApiKeyAuth;",
        f"import {PKG}.model.WhoisResponse;",
        "",
        "public class Main {",
        "    public static void main(String[] args) throws Exception {",
        "        ApiClient client = Configuration.getDefaultApiClient();",
        '        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");',
        f'        auth.setApiKey(System.getenv("{ENV}"));  // set once, sent with every call',
        "",
        "        WhoisApi whois = new WhoisApi(client);",
        "        // whoisLive(domainName, format); null format returns JSON",
        '        WhoisResponse record = whois.whoisLive("whoisfreaks.com", null);',
        '        System.out.println(record.getDomainName() + " expires " + record.getExpiryDate());',
        "        System.out.println(record);",
        "    }",
        "}",
        "```", "",
        "Set your API key and run it:", "",
        "```bash",
        f'export {ENV}="your_api_key"',
        "mvn -q compile exec:java",
        "```", "",
        "To run one of the [runnable examples](../../examples/java/README.md), copy it "
        "into `src/main/java` and pass its class name, for example "
        "`mvn -q compile exec:java -Dexec.mainClass=WhoisLive`.",
    ]
