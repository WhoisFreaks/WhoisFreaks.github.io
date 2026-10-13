"""Kotlin example renderer (com.whoisfreaks:whoisfreaks-kotlin, jvm-okhttp4 client).

API classes keep acronyms upper case (WHOISApi, DatabasesDNSApi). Optional
parameters have Kotlin defaults, so examples pass required params positionally
and the optional ones they show as named arguments. Enum params (format, the
dnsReverse type) are nested enum classes; date params are java.time.LocalDate;
downloads return a temporary java.io.File (deleteOnExit) that is copied out.
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


def _lit(v, p, imports, api=None, op=None):
    if p and p.get("enum"):
        # nested enum class: <Api>.<Param><OperationId>, constants named like the values
        imports.add(f"{PKG}.apis.{api}")
        enum = p["name"][0].upper() + p["name"][1:] + op["op_id"][0].upper() + op["op_id"][1:]
        return f"{api}.{enum}.{v}"
    if p and p.get("format") == "date":
        y, m, d = (int(x) for x in str(v).split("-"))
        imports.add("java.time.LocalDate")
        return f"LocalDate.of({y}, {m}, {d})"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, (list, tuple)):
        return "listOf(" + ", ".join(_lit(x, None, imports) for x in v) + ")"
    return json.dumps(str(v)).replace("$", "\\$")


def _header(op, ctx, cls):
    pc = ctx.params_comment("kotlin", op)
    if op.get("public"):
        pc = pc.replace("(no parameters; the API key is set on the client)",
                        "(no parameters; public endpoint, no API key needed)")
    return [f"// Runnable example: {op['summary']} ({op['method']} {op['path']})",
            f"// Run it from the Getting Started project: gradle run -PmainClass={cls}Kt",
            pc]


def example(op, ctx):
    cls = ctx.pascal(op["op_id"])
    api = ctx.api_class(op["tag"], "kotlin")
    imports = {f"{PKG}.apis.{api}"}
    if not op.get("public"):
        imports.add(f"{PKG}.infrastructure.ApiClient")

    body, args, named = [], [], False
    for p in _signature(op):
        if p is None:
            model = op["body_model"]
            imports.add(f"{PKG}.models.{model}")
            fields = ", ".join(f"{k} = {_lit(v, None, imports)}"
                               for k, v in ctx.body_example(op).items())
            body = [f"    val body = {model}({fields})"]
            pname = model[0].lower() + model[1:]
            args.append(f"{pname} = body" if named else "body")
        elif not _shown(p):
            named = True     # skipped optional: everything after it is named
        else:
            lit = _lit(_value(p, ctx), p, imports, api, op)
            if named or not p["required"]:
                named = True
                args.append(f"{p['name']} = {lit}")
            else:
                args.append(lit)
    call = f"api.{op['op_id']}({', '.join(args)})"

    lines = _header(op, ctx, cls)
    if op.get("is_binary"):
        imports.add("java.io.File")
    sdk = sorted(i for i in imports if i.startswith(PKG))
    jdk = sorted(i for i in imports if not i.startswith(PKG))
    lines += [f"import {i}" for i in sdk + jdk]
    lines += ["", "fun main() {"]
    if op.get("public"):
        lines += ["    // Public endpoint: no API key needed."]
    else:
        lines += [f'    ApiClient.apiKey["apiKey"] = System.getenv("{ENV}")  // set once, sent with every call']
    lines += [f"    val api = {api}()", ""]
    lines += body
    if op.get("is_binary"):
        name = ctx.download_name(op)
        lines += [f"    val download = {call}",
                  "    // The SDK saves the response to a temporary file that is deleted on exit: copy it.",
                  f'    val target = download.copyTo(File("{name}"), overwrite = true)',
                  '    println("Saved ${target.length()} bytes to ${target.absolutePath}")']
    elif op["op_id"] == "rotateApiKey":
        lines += [f"    val newKey = {call}",
                  "    // The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.",
                  '    println("New API key: $newKey")']
    else:
        lines += [f"    val result = {call}",
                  "    println(result)"]
    lines += ["}"]
    return "\n".join(lines) + "\n"


def getting_started(ctx):
    pkg = ctx.LANGS["kotlin"]["pkg"]
    v = ctx.SDK_VERSION
    return [
        "You need JDK 11 or later and [Gradle](https://gradle.org/install/) 8. "
        "Create the project directory:", "",
        "```bash",
        "mkdir -p whoisfreaks-test/src/main/kotlin && cd whoisfreaks-test",
        "```", "",
        "Create `settings.gradle.kts`:", "",
        "```kotlin",
        'rootProject.name = "whoisfreaks-test"',
        "```", "",
        "Create `build.gradle.kts`. The `mainClass` property picks the program "
        "that `gradle run` starts:", "",
        "```kotlin",
        "plugins {",
        '    kotlin("jvm") version "2.0.21"',
        "    application",
        "}", "",
        "repositories {",
        "    mavenCentral()",
        "}", "",
        "dependencies {",
        f'    implementation("{pkg}:{v}")',
        "}", "",
        "application {",
        '    mainClass.set(providers.gradleProperty("mainClass").orElse("MainKt"))',
        "}",
        "```", "",
        "Create `src/main/kotlin/Main.kt`:", "",
        "```kotlin",
        f"import {PKG}.apis.WHOISApi",
        f"import {PKG}.infrastructure.ApiClient",
        "",
        "fun main() {",
        f'    ApiClient.apiKey["apiKey"] = System.getenv("{ENV}")  // set once, sent with every call',
        "",
        '    val record = WHOISApi().whoisLive("whoisfreaks.com")',
        '    println("${record.domainName} expires ${record.expiryDate}")',
        "    println(record)",
        "}",
        "```", "",
        "Set your API key and run it:", "",
        "```bash",
        f'export {ENV}="your_api_key"',
        "gradle run",
        "```", "",
        "To run one of the [runnable examples](../../examples/kotlin/README.md), copy it "
        "into `src/main/kotlin` and pass its class name (file name plus `Kt`), for "
        "example `gradle run -PmainClass=WhoisLiveKt`.",
    ]
