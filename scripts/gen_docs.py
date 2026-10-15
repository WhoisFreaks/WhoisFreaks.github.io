#!/usr/bin/env python3
"""Generate the WhoisFreaks SDK documentation monorepo from the OpenAPI spec.

Docs-as-code: every endpoint reference, parameter table, and per-language usage
example is derived from spec/whoisfreaks-openapi.yaml, so the docs stay accurate
and can be regenerated whenever the spec changes.

Output tree (under OUT_DIR):
  README.md                      root doc (install + quickstart for all languages)
  docs/authentication.md         API key setup, shared by all SDKs
  docs/languages/<lang>.md        install + configure + full endpoint usage per language
  docs/endpoints/README.md        endpoint catalog (grouped by tag)
  docs/endpoints/<slug>.md        per-tag reference: each operation, params, examples
"""
import os, re, sys, yaml, pathlib

SPEC = sys.argv[1] if len(sys.argv) > 1 else "spec/whoisfreaks-openapi.yaml"
OUT  = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "docs-repo")
# GitHub org that owns the SDK repos; Go module and Swift package paths use it.
OWNER = os.environ.get("OWNER", "WhoisFreaks")
# SDK release these docs describe; install lines pin to it. CI regenerates
# with this default, so bump it with each release.
SDK_VERSION = os.environ.get("SDK_VERSION", "0.23.2")

spec = yaml.safe_load(open(SPEC))
comps = spec.get("components", {})

def deref(node):
    if isinstance(node, dict) and "$ref" in node:
        _, _, section, name = node["$ref"].split("/")
        return comps.get(section, {}).get(name, {})
    return node

# ---- registry / install metadata per language -------------------------------
# name  = install identifier on the registry
# repo  = git distribution repo (for git-based langs)
LANGS = {
    "python":     {"label": "Python",     "registry": "PyPI",          "pkg": "whoisfreaks"},
    "javascript": {"label": "JavaScript", "registry": "npm",           "pkg": "whoisfreaks-js"},
    "typescript": {"label": "TypeScript", "registry": "npm",           "pkg": "whoisfreaks"},
    "java":       {"label": "Java",       "registry": "Maven Central",  "pkg": "com.whoisfreaks:whoisfreaks"},
    "kotlin":     {"label": "Kotlin",     "registry": "Maven Central",  "pkg": "com.whoisfreaks:whoisfreaks-kotlin"},
    "csharp":     {"label": "C# / .NET",  "registry": "NuGet",          "pkg": "WhoisFreaks"},
    "ruby":       {"label": "Ruby",       "registry": "RubyGems",       "pkg": "whoisfreaks"},
    "go":         {"label": "Go",         "registry": "Go modules",     "pkg": f"github.com/{OWNER}/whoisfreaks-go"},
    "swift":      {"label": "Swift",      "registry": "Swift PM",       "pkg": f"github.com/{OWNER}/whoisfreaks-swift"},
    "php":        {"label": "PHP",        "registry": "Packagist",      "pkg": "whoisfreaks/whoisfreaks-php"},  # Packagist names are lowercase
}
LANG_ORDER = list(LANGS.keys())

def install_snippet(lang, version=SDK_VERSION):
    m = LANGS[lang]; pkg = m["pkg"]
    if lang == "python":
        return "bash", f"pip install {pkg}"
    if lang == "javascript":
        return "bash", f"npm install {pkg}"
    if lang == "typescript":
        return "bash", f"npm install {pkg}"
    if lang == "java":
        g, a = pkg.split(":")
        return "xml", (f"<dependency>\n  <groupId>{g}</groupId>\n"
                       f"  <artifactId>{a}</artifactId>\n  <version>{version}</version>\n</dependency>")
    if lang == "kotlin":
        return "kotlin", f'implementation("{pkg}:{version}")'
    if lang == "csharp":
        return "bash", f"dotnet add package {pkg}"
    if lang == "ruby":
        return "bash", f"gem install {pkg}"
    if lang == "go":
        return "bash", f"go get {pkg}"
    if lang == "swift":
        return "swift", (f'.package(url: "https://{pkg}.git", from: "{version}")')
    if lang == "php":
        return "bash", f"composer require {pkg}"
    return "bash", ""

# ---- per-language "create a new project" walkthrough ------------------------

# ---- operationId -> per-language method name --------------------------------
def split_words(op_id):
    # camelCase / PascalCase -> words
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1 \2", op_id)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", s)
    return [w for w in re.split(r"[\s_]+", s) if w]

def method_name(op_id, lang):
    w = split_words(op_id)
    lower = [x.lower() for x in w]
    if lang in ("python", "ruby"):
        return "_".join(lower)
    # camelCase (lowercase first word): js, ts, php, java, kotlin, swift
    if lang in ("javascript", "typescript", "php", "java", "kotlin", "swift"):
        return lower[0] + "".join(x.capitalize() for x in lower[1:])
    # PascalCase (capitalize first word too): go, csharp
    if lang in ("go", "csharp"):
        return "".join(x.capitalize() for x in lower)
    return op_id

# ---- collect operations, grouped by tag -------------------------------------
import json

# Inline request bodies become models named <OperationId>Request, except that
# openapi-generator reuses the first model when two inline schemas are identical
# (bulkIpReputation's body is the same as bulkGeolocation's: BulkGeolocationRequest).
_INLINE_BODY_NAMES = {}
def _body_model(op):
    rb = op.get("requestBody")
    if not rb:
        return None
    sch = ((deref(rb).get("content") or {}).get("application/json") or {}).get("schema") or {}
    if sch.get("$ref"):
        return sch["$ref"].split("/")[-1]
    key = json.dumps({k: v for k, v in sch.items() if k != "example"}, sort_keys=True)
    if key not in _INLINE_BODY_NAMES:
        oid = op.get("operationId") or ""
        _INLINE_BODY_NAMES[key] = oid[:1].upper() + oid[1:] + "Request"
    return _INLINE_BODY_NAMES[key]

def _body_schema(op):
    rb = op.get("requestBody")
    if not rb:
        return None
    return deref(((deref(rb).get("content") or {}).get("application/json") or {}).get("schema") or {})

def collect():
    out = {}
    for path, item in spec["paths"].items():
        for method, op in item.items():
            if method not in ("get", "post", "put", "delete", "patch"):
                continue
            tag = (op.get("tags") or ["General"])[0]
            params = []
            for pa in op.get("parameters", []):
                pa = deref(pa)
                sc = pa.get("schema", {})
                params.append({
                    "name": pa.get("name"),
                    "in": pa.get("in"),
                    "required": pa.get("required", False),
                    "type": sc.get("type", "string"),
                    "enum": sc.get("enum"),
                    "default": sc.get("default"),
                    "format": sc.get("format"),
                    "example": pa.get("example", sc.get("example")),
                    "desc": (pa.get("description") or "").strip(),
                })
            # detect binary/file-download responses (application/octet-stream
            # or format: binary) so examples write bytes to a file, not print()
            _r = (op.get("responses") or {}).get("200") or {}
            _r = deref(_r)
            _content = _r.get("content") or {}
            _is_binary = "application/octet-stream" in _content or any(
                (deref(cv).get("schema") or {}).get("format") == "binary"
                for cv in _content.values()
            )
            # resolve the 200 JSON response schema name (for a response-fields table)
            _resp_schema = None
            _resp_is_array = False
            for _ct, _cv in _content.items():
                if _ct.startswith("application/json"):
                    _sc = deref(_cv).get("schema") or {}
                    if "$ref" in _sc:
                        _resp_schema = _sc["$ref"].split("/")[-1]
                    elif _sc.get("type") == "array" and "$ref" in (_sc.get("items") or {}):
                        _resp_schema = _sc["items"]["$ref"].split("/")[-1]
                        _resp_is_array = True
                    break
            _servers = op.get("servers") or item.get("servers") or spec["servers"]
            out.setdefault(tag, []).append({
                "tag": tag,
                "method": method.upper(),
                "path": path,
                "op_id": op.get("operationId") or "",
                "summary": op.get("summary") or "",
                "description": (op.get("description") or "").strip(),
                "params": params,
                "request_body": bool(op.get("requestBody")),
                "body_model": _body_model(op),
                "body_schema": _body_schema(op),
                "is_binary": _is_binary,
                "response_schema": _resp_schema,
                "response_is_array": _resp_is_array,
                "server": _servers[0]["url"],
                "public": op.get("security") == [],
            })
    return out

OPS = collect()

def slug(tag):
    return re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")

# ---- example values shared by the per-language renderers --------------------
FALLBACK_EXAMPLES = {"domainName": "whoisfreaks.com", "domain": "whoisfreaks.com",
                     "ip": "8.8.8.8", "ipAddress": "8.8.8.8", "asn": "AS15169",
                     "keyword": "whoisfreaks", "value": "8.8.8.8"}
def example_value(p):
    """A realistic value for parameter p as a Python value: the spec example, else
    the default, else a fallback by name/type. Dates are 'YYYY-MM-DD' strings;
    p['format'] == 'date' tells a renderer to use the language's date type."""
    if p.get("example") is not None:
        return p["example"]
    if p.get("default") is not None:
        return p["default"]
    if p["name"] in FALLBACK_EXAMPLES:
        return FALLBACK_EXAMPLES[p["name"]]
    if p.get("enum"):
        return p["enum"][0]
    if p.get("format") == "date":
        return "2026-10-01"
    return {"boolean": True, "integer": 1}.get(p["type"], "example")

def download_name(op):
    """File name a download example saves to: <OperationId> plus the extension the
    spec's 200 response description names (CSV, ZIP archive, JSON, JSON gzipped)."""
    r = deref(((spec["paths"][op["path"]][op["method"].lower()].get("responses") or {}).get("200")) or {})
    d = (r.get("description") or "").lower()
    if "gzip" in d:
        ext = "json.gz" if "json" in d else "gz"
    elif "zip" in d:
        ext = "zip"
    elif "json" in d:
        ext = "json"
    elif "csv" in d:
        ext = "csv"
    else:
        ext = "bin"
    return f"{_pascal(op['op_id'])}.{ext}"

BODY_EXAMPLES = {"domainNames": ["whoisfreaks.com", "example.com"], "ips": ["8.8.8.8", "1.1.1.1"]}
def body_example(op):
    """Example request body as {jsonFieldName: value}: the spec example if any,
    else the required fields (or the main list field) with sample values."""
    sch = op.get("body_schema") or {}
    if sch.get("example"):
        return dict(sch["example"])
    props = sch.get("properties") or {}
    fields = sch.get("required") or [k for k in BODY_EXAMPLES if k in props][:1]
    return {k: BODY_EXAMPLES.get(k, ["example"]) for k in fields}

# ---- example call renderer (per language) -----------------------------------
def api_class(tag, lang):
    """Generated API class/type name for a tag. VERIFIED against all 10 real
    generated SDKs:
      * Java is the ONLY language that title-cases acronyms:
        WhoisApi, SslApi, IpWhoisApi, DatabasesIpWhoisApi
      * Every other language keeps acronyms UPPER:
        - python/js/ts/csharp/kotlin/php/ruby: WHOISApi, SSLApi, IPWHOISApi (+ 'Api')
        - swift:  WHOISAPI, SSLAPI, IPWHOISAPI (+ 'API')
        - go:     WHOISAPIService (accessed on the client as .WHOISAPI)
    """
    words = re.sub(r"[^A-Za-z0-9]+", " ", tag).split()
    if lang == "java":
        core = "".join(w.capitalize() for w in words)      # acronyms title-cased
    else:
        core = "".join(w if w.isupper() else w.capitalize() for w in words)
    if lang == "swift":
        return core + "API"
    if lang == "go":
        return core + "APIService"      # the struct type; accessor is core+"API"
    return core + "Api"

def go_accessor(tag):
    """Field name used to reach a service on the Go APIClient, e.g. client.WHOISAPI."""
    words = re.sub(r"[^A-Za-z0-9]+", " ", tag).split()
    return "".join(w if w.isupper() else w.capitalize() for w in words) + "API"

def py_snake(name):
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()

def py_module(cls):
    """Python api module filename (without .py) for a given generated class name.
    openapi-generator inserts '_' at lower->Upper boundaries and at
    ACRONYM->Word boundaries, then lowercases. Acronym runs with no trailing
    lowercase word stay glued: IPWHOISApi -> ipwhois_api, but
    IPReputationApi -> ip_reputation_api. Verified against the real SDK."""
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", cls)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    return s.lower()


# yesterday-at-runtime expression + value literal per language ----------------
# fixed lower-bound date for `after`; a plain quoted literal in every language
# languages whose date expressions need extra imports / the 'time' package


COMMENT_PREFIX = {
    "python": "# ", "ruby": "# ", "go": "// ", "php": "// ",
    "javascript": "// ", "typescript": "// ", "java": "// ",
    "kotlin": "// ", "csharp": "// ", "swift": "// ",
}
def params_comment(lang, op):
    """A comment block listing every input parameter: name, type, required/optional,
    and description. Returned as a single string (already comment-prefixed)."""
    pre = COMMENT_PREFIX.get(lang, "# ")
    lines = [f"{pre}Parameters for {op['op_id']} ({op['method']} {op['path']}):"]
    any_p = False
    for p in op["params"]:
        any_p = True
        req = "required" if p["required"] else "optional"
        t = p.get("type") or "string"
        if p.get("enum"):
            t += " (one of: " + ", ".join(str(e) for e in p["enum"]) + ")"
        desc = (p.get("desc") or "").strip().replace("\n", " ")
        if len(desc) > 90: desc = desc[:87] + "..."
        line = f"{pre}  - {p['name']} ({t}, {req})"
        if desc: line += f": {desc}"
        lines.append(line)
    if op.get("body_model"):
        lines.append(f"{pre}  - body: {op['body_model']} (required): request body object")
    if not any_p and not op.get("body_model"):
        lines.append(f"{pre}  (no parameters" + ("; no API key required)" if op.get("public")
                                                 else "; the API key is set on the client)"))
    return "\n".join(lines)

def _pascal(op_id):
    return "".join(w.capitalize() for w in split_words(op_id)) or "Example"


# ---- per-language renderers: scripts/docs_lang/<lang>.py ---------------------
# Each module defines example(op, ctx) and getting_started(ctx); ctx carries the
# shared helpers below.
import importlib, types
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
CTX = types.SimpleNamespace(
    OWNER=OWNER, SDK_VERSION=SDK_VERSION, LANGS=LANGS, spec=spec, deref=deref,
    install_snippet=install_snippet, method_name=method_name, api_class=api_class,
    go_accessor=go_accessor, py_snake=py_snake, py_module=py_module,
    params_comment=params_comment, pascal=_pascal, split_words=split_words,
    example_value=example_value, body_example=body_example, download_name=download_name)

def _lang_module(lang):
    return importlib.import_module(f"docs_lang.{lang}")

def runnable_example(lang, op):
    return _lang_module(lang).example(op, CTX)

def getting_started(lang):
    return _lang_module(lang).getting_started(CTX)

# unify: doc snippets use the same full-signature renderer as runnable files
# (render_example forwards to runnable_example; see its definition above)


def render_example(lang, op):
    # Forwarder: language pages (docs/languages/*.md) and endpoint pages must use
    # the SAME renderer as the runnable example files so inline snippets stay in
    # sync. runnable_example returns just the code string; inline callers expect
    # a (fence, code) tuple, so wrap it with the right syntax-highlight fence.
    FENCE = {"python": "python", "javascript": "javascript", "typescript": "typescript",
             "java": "java", "kotlin": "kotlin", "csharp": "csharp", "ruby": "ruby",
             "go": "go", "php": "php", "swift": "swift"}
    return FENCE.get(lang, ""), runnable_example(lang, op)

def w(path, text):
    p = OUT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + "\n")

def param_table(params):
    if not params:
        return "None. The API key is set once on the client."
    rows = ["| Parameter | In | Required | Type | Default | Description |",
            "|-----------|----|----------|------|---------|-------------|"]
    for p in params:
        allowed = f" (one of: {', '.join(map(str, p['enum']))})" if p["enum"] else ""
        req = "yes" if p["required"] else "no"
        typ = p["type"] + (f" ({p['format']})" if p.get("format") else "")
        default = "" if p.get("default") is None else f"`{str(p['default']).lower() if isinstance(p['default'], bool) else p['default']}`"
        # Escaped outside the f-string: Python < 3.12 rejects backslashes there.
        desc = (p['desc'] or '').replace('|', '\\|')
        rows.append(f"| `{p['name']}` | {p['in']} | {req} | {typ} | {default} | "
                    f"{desc}{allowed} |")
    return "\n".join(rows)

def body_table(op):
    sch = op.get("body_schema") or {}
    req = set(sch.get("required") or [])
    rows = ["| Field | Type | Required | Description |", "|-------|------|----------|-------------|"]
    for k, v in (sch.get("properties") or {}).items():
        t = v.get("type", "any")
        if t == "array":
            t = f"array<{(v.get('items') or {}).get('type', 'any')}>"
        note = f"Up to {v['maxItems']} items." if v.get("maxItems") else ""
        rows.append(f"| `{k}` | {t} | {'yes' if k in req else 'no'} | {(v.get('description') or note).strip()} |")
    return "\n".join(rows) + "\n\nExample: `" + json.dumps(body_example(op)) + "`"

TOTAL_OPS = sum(len(v) for v in OPS.values())
INFO = spec["info"]
# flatten the multi-line spec description into a single clean sentence
DESC1 = " ".join(INFO["description"].split("\n\n")[0].split())

# ---------- super-section grouping (API Solutions / Databases / Account) -----
SECTIONS = [
    ("API Solutions",
     "Real-time and on-demand lookup APIs. Query a single domain, IP, or ASN and "
     "get structured JSON (or XML) back immediately.",
     ["WHOIS", "DNS", "Domain Availability", "Typosquatting", "SSL", "Geolocation",
      "Subdomains", "IP Reputation", "Domain Reputation", "ASN WHOIS", "IP WHOIS"]),
    ("Databases",
     "Bulk data feeds and downloadable database snapshots for large-scale "
     "processing: newly registered, expiring/dropped, and full WHOIS/DNS/IP datasets.",
     ["Databases - Newly Registered", "Databases - Expiring & Dropped",
      "Databases - WHOIS", "Databases - DNS", "Databases - Subdomains",
      "Databases - IP Geolocation", "Databases - ASN WHOIS",
      "Databases - IP WHOIS", "Databases - IP Security",
      "Databases - Threat Feed"]),
    ("Account & Utilities",
     "Manage your account, monitor API usage and credits, and rotate your API key.",
     ["Account"]),
]
def section_of(tag):
    for name, _desc, tags in SECTIONS:
        if tag in tags:
            return name
    return "Other"

def response_fields_table(op):
    """Render a Markdown table of the top-level response fields, expanding nested
    object $refs one level so the reader sees the shape without chasing refs."""
    name = op.get("response_schema")
    if not name:
        return None
    schema = (spec.get("components", {}).get("schemas", {}) or {}).get(name)
    if not schema or "properties" not in schema:
        return None
    def type_of(v):
        if "$ref" in v:
            return v["$ref"].split("/")[-1]
        if v.get("type") == "array":
            it = v.get("items", {})
            inner = it["$ref"].split("/")[-1] if "$ref" in it else it.get("type", "any")
            return f"array<{inner}>"
        return v.get("type", "any")
    rows = ["| Field | Type | Description |", "|-------|------|-------------|"]
    for k, v in schema["properties"].items():
        desc = (v.get("description") or "").replace("\n", " ").strip()
        rows.append(f"| `{k}` | {type_of(v)} | {desc} |")
    label = f"array of `{name}`" if op.get("response_is_array") else f"`{name}`"
    out = [f"**Response** ({label})", "", "\n".join(rows), ""]
    # expand nested object schemas one level (unique refs referenced above)
    nested = []
    seen = set()
    for v in schema["properties"].values():
        ref = None
        if "$ref" in v:
            ref = v["$ref"].split("/")[-1]
        elif v.get("type") == "array" and "$ref" in (v.get("items") or {}):
            ref = v["items"]["$ref"].split("/")[-1]
        if ref and ref not in seen:
            seen.add(ref)
            sub = (spec.get("components", {}).get("schemas", {}) or {}).get(ref)
            if sub and "properties" in sub:
                nested.append((ref, sub))
    for ref, sub in nested:
        sr = ["| Field | Type | Description |", "|-------|------|-------------|"]
        for k, v in sub["properties"].items():
            d = (v.get("description") or "").replace("\n", " ").strip()
            sr.append(f"| `{k}` | {type_of(v)} | {d} |")
        out += [f"<details><summary><code>{ref}</code> object</summary>", "",
                "\n".join(sr), "", "</details>", ""]
    return "\n".join(out)

# ---------- endpoints/<tag>.md -----------------------------------------------
for tag, ops in OPS.items():
    body = [f"# {tag}", ""]
    body += [f"*Section: {section_of(tag)}*", ""]
    if TAG_DESC := next((t.get("description") for t in spec.get("tags", []) if t.get("name") == tag), None):
        body += [TAG_DESC, ""]
    body += [f"{len(ops)} endpoint{'s' if len(ops) != 1 else ''}. Requests need your API key "
             f"unless noted otherwise. See [Authentication](../authentication.md).", ""]
    for op in ops:
        anchor = op["op_id"] or op["path"]
        body += [f"## {op['summary'] or op['op_id']}", ""]
        body += [f"`{op['method']} {op['server']}{op['path']}`", ""]
        if op["public"]:
            body += ["Public endpoint: no API key required.", ""]
        if op["description"]:
            body += [op["description"], ""]
        body += ["**Parameters**", "", param_table(op["params"]), ""]
        if op.get("body_schema"):
            body += [f"**Request body** (`application/json`, model `{op['body_model']}`)", "",
                     body_table(op), ""]
        # response fields table (from the spec response schema), when not a binary download
        if not op.get("is_binary"):
            rt = response_fields_table(op)
            if rt:
                body += [rt, ""]
        # usage example in three common languages
        body += ["**Usage**", ""]
        for lang in ("python", "typescript", "go"):
            fence, code = render_example(lang, op)
            body += [f"<details><summary>{LANGS[lang]['label']}</summary>", "",
                     f"```{fence}", code, "```", "", "</details>", ""]
        body += ["---", ""]
    w(f"docs/endpoints/{slug(tag)}.md", "\n".join(body))

# ---------- endpoints/README.md (catalog, grouped by section) ----------------
cat = ["# Endpoint Reference", "",
       f"The WhoisFreaks API exposes **{TOTAL_OPS} endpoints** across "
       f"**{len(OPS)} categories**, organized into {len(SECTIONS)} sections. "
       f"Every endpoint is available in all {len(LANGS)} SDKs.", ""]
for sec_name, sec_desc, sec_tags in SECTIONS:
    present = [t for t in sec_tags if t in OPS]
    if not present:
        continue
    total = sum(len(OPS[t]) for t in present)
    cat += [f"## {sec_name}", "", sec_desc, "",
            f"{total} endpoint{'s' if total != 1 else ''} across {len(present)} "
            f"categor{'ies' if len(present) != 1 else 'y'}. See the "
            f"[{sec_name} overview]({slug(sec_name)}.md).", ""]
    for t in present:
        n = len(OPS[t])
        cat.append(f"- [{t}]({slug(t)}.md): {n} endpoint{'s' if n != 1 else ''}")
    cat.append("")
cat += ["## Full endpoint list", "",
        "| Section | Category | Method | Path | Operation |",
        "|---------|----------|--------|------|-----------|"]
for tag, ops in OPS.items():
    for op in ops:
        cat.append(f"| {section_of(tag)} | {tag} | {op['method']} | "
                   f"`{op['path']}` | `{op['op_id']}` |")
w("docs/endpoints/README.md", "\n".join(cat))

# ---------- endpoints/<section>.md (section landing pages) -------------------
for sec_name, sec_desc, sec_tags in SECTIONS:
    present = [t for t in sec_tags if t in OPS]
    if not present:
        continue
    total = sum(len(OPS[t]) for t in present)
    sb = [f"# {sec_name}", "", sec_desc, "",
          f"**{total} endpoint{'s' if total != 1 else ''}** across **{len(present)} "
          f"categor{'ies' if len(present) != 1 else 'y'}**. Requests need your API key "
          f"unless noted otherwise. See [Authentication](../authentication.md).", "",
          "## Categories", ""]
    for t in present:
        tag_desc = next((td.get("description") for td in spec.get("tags", [])
                         if td.get("name") == t), "") or ""
        sb.append(f"### [{t}]({slug(t)}.md)")
        sb.append("")
        if tag_desc:
            sb += [tag_desc, ""]
        n = len(OPS[t])
        sb += [f"{n} endpoint{'s' if n != 1 else ''}:", ""]
        for op in OPS[t]:
            sb.append(f"- **{op['summary'] or op['op_id']}**: "
                      f"`{op['method']} {op['path']}`")
        sb.append("")
    w(f"docs/endpoints/{slug(sec_name)}.md", "\n".join(sb))

# ---------- authentication.md ------------------------------------------------
auth = f"""# Authentication

Every WhoisFreaks API request needs an **API key**, passed as the `apiKey`
query parameter. The one exception is the public database file status check
(`GET /v3.4/status`). Each SDK exposes a configuration hook so you set the key
once and it is attached to every request automatically.

## Get an API key

New to WhoisFreaks? Follow the step-by-step guide, [Getting Started with WhoisFreaks: How to Sign Up and Get Your API Key](https://whoisfreaks.com/resources/tutorial/getting-started-with-whoisfreaks-how-to-sign-up-and-get-your-api-key), which walks through account creation and locating your key.

In short:

1. Sign in at <https://billing.whoisfreaks.com>.
2. Copy your API key from the dashboard.
3. Keep it secret. Do **not** commit it to source control; the examples read it
   from the `WHOISFREAKS_API_KEY` environment variable.

## Base URLs

| Purpose | Base URL |
|---------|----------|
| Live lookups, bulk lookups and account | `{spec['servers'][0]['url']}` |
| Database downloads, threat feeds and database file status | `{spec['servers'][1]['url']}` |

The SDKs pick the right host for each endpoint; every endpoint page shows its full URL.

## Setting the key per language

""".splitlines()
# reuse the first WHOIS op (falling back to any op) for a per-language auth example
first_op = OPS.get("WHOIS", next(iter(OPS.values())))[0]
for lang in LANG_ORDER:
    fence, code = render_example(lang, first_op)
    auth += [f"### {LANGS[lang]['label']}", "", f"```{fence}", code, "```", ""]
w("docs/authentication.md", "\n".join(auth))

# ---------- SEO metadata + build-from-source per language --------------------
def _about(lang):
    label = LANGS[lang]["label"]
    return (f"The official **WhoisFreaks {label} SDK**: a complete client for "
            f"WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP "
            f"reputation, ASN, typosquatting, and domain reputation lookups, plus "
            f"bulk database downloads. Query real-time and historical domain data, "
            f"reverse WHOIS, and threat intelligence from {label} with a single API "
            f"key. Generated from the WhoisFreaks OpenAPI specification and published "
            f"to {LANGS[lang]['registry']}.")

# Broad, search-optimized keyword set (shared domain-intelligence terms + the
# language) so each page ranks for both the topic and the language binding.
_COMMON_TAGS = [
    "whois api", "whois lookup", "domain api", "dns api", "dns lookup",
    "reverse whois", "historical whois", "domain availability api",
    "ssl certificate api", "ip geolocation api", "ip reputation api",
    "asn lookup", "subdomain finder", "typosquatting api",
    "domain reputation", "threat intelligence api", "domain data api",
    "whois sdk", "domain monitoring", "brand protection api",
]
def _tags(lang):
    label = LANGS[lang]["label"].lower()
    lead = [f"{label} whois api", f"{label} whois sdk", f"whoisfreaks {label}",
            f"{label} domain lookup", f"{label} dns api"]
    return lead + _COMMON_TAGS

def build_from_source(lang):
    """Instructions to clone + build the SDK locally from its public
    per-language distribution repository (github.com/WhoisFreaks/whoisfreaks-<lang>)."""
    repo = f"https://github.com/WhoisFreaks/whoisfreaks-{lang}"
    steps = {
        "python":     [f"git clone {repo}", f"cd whoisfreaks-{lang}",
                       "pip install -e .   # editable local install"],
        "javascript": [f"git clone {repo}", f"cd whoisfreaks-{lang}",
                       "npm install", "npm run build"],
        "typescript": [f"git clone {repo}", f"cd whoisfreaks-{lang}",
                       "npm install", "npm run build"],
        "java":       [f"git clone {repo}", f"cd whoisfreaks-{lang}",
                       "mvn clean install   # builds + installs to local ~/.m2"],
        "kotlin":     [f"git clone {repo}", f"cd whoisfreaks-{lang}",
                       "./gradlew build   # or: ./gradlew publishToMavenLocal"],
        "csharp":     [f"git clone {repo}", f"cd whoisfreaks-{lang}",
                       "dotnet build   # or: dotnet pack -c Release"],
        "ruby":       [f"git clone {repo}", f"cd whoisfreaks-{lang}",
                       "gem build *.gemspec", "gem install ./whoisfreaks-*.gem"],
        "go":         [f"git clone {repo}", f"cd whoisfreaks-{lang}",
                       "go build ./...   # or import the module path directly"],
        "php":        [f"git clone {repo}", f"cd whoisfreaks-{lang}", "composer install"],
        "swift":      [f"git clone {repo}", f"cd whoisfreaks-{lang}", "swift build"],
    }
    lines = steps.get(lang, [f"git clone {repo}"])
    return ["```bash"] + lines + ["```"]

# ---------- languages/<lang>.md ----------------------------------------------
for lang in LANG_ORDER:
    m = LANGS[lang]
    fence_i, inst = install_snippet(lang)
    body = [f"# {m['label']} SDK", "",
            "## About", "",
            _about(lang), "",
            "**Keywords:** " + ", ".join(_tags(lang)), "",
            f"- **Registry:** {m['registry']}",
            f"- **Package:** `{m['pkg']}`", "",
            "## Install", "", f"```{fence_i}", inst, "```", "",
            "## Build from Source", "",
            "Prefer to build the SDK yourself instead of installing from "
            f"{m['registry']}? Clone the {m['label']} SDK repository and build it "
            "locally:", ""]
    body += build_from_source(lang)
    body += ["",
            "## Getting Started", "",
            "A complete walkthrough from an empty directory to a running "
            "program:", ""]
    body += getting_started(lang)
    body += ["",
            "## Configure", "",
            f"See [Authentication](../authentication.md) for how to obtain a key. "
            f"Minimal setup:", ""]
    fence_c, code = render_example(lang, first_op)
    body += [f"```{fence_c}", code, "```", "",
             "## Endpoints", "",
             f"All {TOTAL_OPS} endpoints are shown below, grouped by category. "
             f"Each includes its method, path, parameters, and a runnable example. "
             f"See the [full endpoint reference](../endpoints/README.md) for "
             f"response shapes and field details.", ""]
    # show every operation, grouped by category (tag)
    for tag, ops in OPS.items():
        body += [f"### {tag}", ""]
        for op in ops:
            fence, code = render_example(lang, op)
            body += [f"#### {op['summary'] or op['op_id']}", "",
                     f"`{op['method']} {op['path']}`", "",
                     f"```{fence}", code, "```", ""]
    w(f"docs/languages/{lang}.md", "\n".join(body))

# ---------- root README ------------------------------------------------------
lang_rows = "\n".join(
    f"| {LANGS[l]['label']} | {LANGS[l]['registry']} | `{LANGS[l]['pkg']}` | "
    f"[Guide](docs/languages/{l}.md) |"
    for l in LANG_ORDER)
cat_rows = "\n".join(f"| [{tag}](docs/endpoints/{slug(tag)}.md) | {len(ops)} |"
                     for tag, ops in OPS.items())
# section-grouped rows for the root README
_sr = []
for _sn, _sd, _st in SECTIONS:
    _present = [t for t in _st if t in OPS]
    if not _present:
        continue
    _tot = sum(len(OPS[t]) for t in _present)
    _cats = ", ".join(f"[{t}](docs/endpoints/{slug(t)}.md)" for t in _present)
    _sr.append(f"### [{_sn}](docs/endpoints/{slug(_sn)}.md) ({_tot} endpoints)\n\n{_sd}\n\n{_cats}\n")
section_rows = "\n".join(_sr)
# Kept out of the f-string below: Python < 3.12 rejects backslashes there.
desc1_plain = DESC1.replace(" — ", ": ")

readme = f"""# WhoisFreaks SDK Documentation

Official documentation for the **WhoisFreaks** SDKs: one API, {len(LANGS)}
languages, {TOTAL_OPS} endpoints. Every SDK is generated from the same
[OpenAPI specification](spec/whoisfreaks-openapi.yaml) and published to
its language's standard registry.

> {desc1_plain}

## Contents

- [Authentication](docs/authentication.md): get and configure your API key
- [Language guides](#language-guides): install + usage for each SDK
- [Endpoint reference](docs/endpoints/README.md): all {TOTAL_OPS} endpoints, grouped by category
- [Runnable examples](examples/README.md): copy-paste, ready-to-run example for every endpoint in every language

## Language guides

| Language | Registry | Package | Guide |
|----------|----------|---------|-------|
{lang_rows}

## Quick start

Pick your language, install the package, set your API key, and call an endpoint.
Example (Python):

```bash
pip install {LANGS['python']['pkg']}
```

```python
import os
import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]

with whoisfreaks.ApiClient(config) as client:
    record = whoisfreaks.WHOISApi(client).whois_live("example.com")
    print(record.domain_registrar.registrar_name, record.expiry_date)
```

The equivalent for every other language is in its [language guide](#language-guides).

## Endpoint sections

The API is organized into three sections. See the [full endpoint reference](docs/endpoints/README.md) for every operation with its URL, parameters, response fields and Python, TypeScript and Go examples. The [language guides](#language-guides) show every operation in all {len(LANGS)} languages.

{section_rows}

## Authentication at a glance

Every request except the public database file status check needs an `apiKey`
query parameter. Get a key at <https://billing.whoisfreaks.com>, then configure it
once via each SDK's configuration object. See [Authentication](docs/authentication.md).

Base URLs:

| Purpose | URL |
|---------|-----|
| Live lookups, bulk lookups and account | `{spec['servers'][0]['url']}` |
| Database downloads, threat feeds and database file status | `{spec['servers'][1]['url']}` |

## About these docs

These docs are generated from the OpenAPI spec by `scripts/gen_docs.py`, so they
stay in sync with the API. To regenerate after a spec change or an SDK release
(`SDK_VERSION` sets the version in install lines):

```bash
SDK_VERSION={SDK_VERSION} python3 scripts/gen_docs.py spec/whoisfreaks-openapi.yaml .
```

## Support

- API docs: <https://whoisfreaks.com/documentation>
- Billing & keys: <https://billing.whoisfreaks.com>
- Email: {INFO.get('contact', {}).get('email', 'support@whoisfreaks.com')}

## License

{spec.get('info', {}).get('license', {}).get('name', 'MIT')}. See individual SDK repositories for details.
"""
w("README.md", readme)

print(f"generated docs for {len(LANGS)} languages and {TOTAL_OPS} endpoints "
      f"across {len(OPS)} categories -> {OUT}")


# ============================================================================
# Runnable, copy-paste examples: one file per endpoint per language.
# These use the FULL method signature (all params positional where the language
# requires it, passing null/None for optionals) so they compile/run as-is.
# ============================================================================
EXT = {"python":"py","javascript":"js","typescript":"ts","java":"java",
       "kotlin":"kt","csharp":"cs","ruby":"rb","go":"go","swift":"swift","php":"php"}

def write_examples():
    count=0
    written=set()
    for tag, ops in OPS.items():
        for op in ops:
            P=_pascal(op["op_id"])
            for lang in LANG_ORDER:
                code=runnable_example(lang, op)
                w(f"examples/{lang}/{P}.{EXT[lang]}", code)
                written.add(f"examples/{lang}/{P}.{EXT[lang]}")
                count+=1
    # drop examples for operations that no longer exist in the spec
    for lang in LANG_ORDER:
        for f in (OUT / "examples" / lang).glob(f"*.{EXT[lang]}"):
            if f"examples/{lang}/{f.name}" not in written:
                f.unlink()
                print(f"removed stale example {f.relative_to(OUT)}")
    # index
    idx=["# Runnable Examples","",
         f"Copy-paste, ready-to-run examples for **every one of the {TOTAL_OPS} "
         f"endpoints** in **all {len(LANGS)} languages** ({count} files).","",
         "Set the `WHOISFREAKS_API_KEY` environment variable to your key (from "
         "<https://billing.whoisfreaks.com>) and run. Layout: "
         "`examples/<language>/<Operation>.<ext>`.","",
         "| Endpoint | Operation | Example file (per language) |",
         "|----------|-----------|------------------------------|"]
    for tag, ops in OPS.items():
        for op in ops:
            P=_pascal(op["op_id"])
            links=" · ".join(f"[{LANGS[l]['label']}]({l}/{P}.{EXT[l]})" for l in LANG_ORDER)
            idx.append(f"| {op['summary']} | `{op['op_id']}` | {links} |")
    # per-language example index
    for lang in LANG_ORDER:
        li=[f"# {LANGS[lang]['label']} Runnable Examples","",
            f"Install: see the [{LANGS[lang]['label']} guide](../../docs/languages/{lang}.md). "
            f"Set the `WHOISFREAKS_API_KEY` environment variable and run any file below.",""]
        for tag, ops in OPS.items():
            li.append(f"## {tag}")
            for op in ops:
                P=_pascal(op["op_id"])
                li.append(f"- [`{P}.{EXT[lang]}`]({P}.{EXT[lang]}): {op['summary']} (`{op['method']} {op['path']}`)")
            li.append("")
        w(f"examples/{lang}/README.md", "\n".join(li))
    w("examples/README.md","\n".join(idx))
    return count

_ex = write_examples()
print(f"wrote {_ex} runnable example files")
