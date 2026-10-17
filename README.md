# WhoisFreaks SDK Documentation

Official documentation for the **WhoisFreaks** SDKs: one API, 10
languages, 60 endpoints. Every SDK is generated from the same
[OpenAPI specification](spec/whoisfreaks-openapi.yaml) and published to
its language's standard registry.

> Complete WhoisFreaks API: WHOIS, DNS, SSL, Geolocation, Typosquatting, IP Intelligence, Domain Reputation, and bulk database downloads.

## Contents

- [Authentication](docs/authentication.md): get and configure your API key
- [Language guides](#language-guides): install + usage for each SDK
- [Endpoint reference](docs/endpoints/README.md): all 60 endpoints, grouped by category
- [Runnable examples](examples/README.md): copy-paste, ready-to-run example for every endpoint in every language

## Language guides

| Language | Registry | Package | Guide |
|----------|----------|---------|-------|
| Python | PyPI | `whoisfreaks` | [Guide](docs/languages/python.md) |
| JavaScript | npm | `whoisfreaks-js` | [Guide](docs/languages/javascript.md) |
| TypeScript | npm | `whoisfreaks` | [Guide](docs/languages/typescript.md) |
| Java | Maven Central | `com.whoisfreaks:whoisfreaks` | [Guide](docs/languages/java.md) |
| Kotlin | Maven Central | `com.whoisfreaks:whoisfreaks-kotlin` | [Guide](docs/languages/kotlin.md) |
| C# / .NET | NuGet | `WhoisFreaks` | [Guide](docs/languages/csharp.md) |
| Ruby | RubyGems | `whoisfreaks` | [Guide](docs/languages/ruby.md) |
| Go | Go modules | `github.com/WhoisFreaks/whoisfreaks-go` | [Guide](docs/languages/go.md) |
| Swift | Swift PM | `github.com/WhoisFreaks/whoisfreaks-swift` | [Guide](docs/languages/swift.md) |
| PHP | Packagist | `whoisfreaks/whoisfreaks-php` | [Guide](docs/languages/php.md) |

## Quick start

Pick your language, install the package, set your API key, and call an endpoint.
Example (Python):

```bash
pip install whoisfreaks
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

The API is organized into three sections. See the [full endpoint reference](docs/endpoints/README.md) for every operation with its URL, parameters, response fields and Python, TypeScript and Go examples. The [language guides](#language-guides) show every operation in all 10 languages.

### [API Solutions](docs/endpoints/api-solutions.md) (20 endpoints)

Real-time and on-demand lookup APIs. Query a single domain, IP, or ASN and get structured JSON (or XML) back immediately.

[WHOIS](docs/endpoints/whois.md), [DNS](docs/endpoints/dns.md), [Domain Availability](docs/endpoints/domain-availability.md), [Typosquatting](docs/endpoints/typosquatting.md), [SSL](docs/endpoints/ssl.md), [Geolocation](docs/endpoints/geolocation.md), [Subdomains](docs/endpoints/subdomains.md), [IP Reputation](docs/endpoints/ip-reputation.md), [Domain Reputation](docs/endpoints/domain-reputation.md), [ASN WHOIS](docs/endpoints/asn-whois.md), [IP WHOIS](docs/endpoints/ip-whois.md)

### [Databases](docs/endpoints/databases.md) (37 endpoints)

Bulk data feeds and downloadable database snapshots for large-scale processing: newly registered, expiring/dropped, and full WHOIS/DNS/IP datasets.

[Databases - Newly Registered](docs/endpoints/databases-newly-registered.md), [Databases - Expiring & Dropped](docs/endpoints/databases-expiring-dropped.md), [Databases - WHOIS](docs/endpoints/databases-whois.md), [Databases - DNS](docs/endpoints/databases-dns.md), [Databases - Subdomains](docs/endpoints/databases-subdomains.md), [Databases - IP Geolocation](docs/endpoints/databases-ip-geolocation.md), [Databases - ASN WHOIS](docs/endpoints/databases-asn-whois.md), [Databases - IP WHOIS](docs/endpoints/databases-ip-whois.md), [Databases - IP Security](docs/endpoints/databases-ip-security.md), [Databases - Threat Feed](docs/endpoints/databases-threat-feed.md)

### [Account & Utilities](docs/endpoints/account-utilities.md) (3 endpoints)

Manage your account, monitor API usage and credits, and rotate your API key.

[Account](docs/endpoints/account.md)


## Authentication at a glance

Every request except the public database file status check needs an `apiKey`
query parameter. Get a key at <https://billing.whoisfreaks.com>, then configure it
once via each SDK's configuration object. See [Authentication](docs/authentication.md).

Base URLs:

| Purpose | URL |
|---------|-----|
| Live lookups, bulk lookups and account | `https://api.whoisfreaks.com` |
| Database downloads, threat feeds and database file status | `https://files.whoisfreaks.com` |

## About these docs

These docs are generated from the OpenAPI spec by `scripts/gen_docs.py`, so they
stay in sync with the API. To regenerate after a spec change or an SDK release
(`SDK_VERSION` sets the version in install lines):

```bash
SDK_VERSION=0.24.0 python3 scripts/gen_docs.py spec/whoisfreaks-openapi.yaml .
```

## Support

- API docs: <https://whoisfreaks.com/documentation>
- Billing & keys: <https://billing.whoisfreaks.com>
- Email: support@whoisfreaks.com

## License

MIT. See individual SDK repositories for details.
