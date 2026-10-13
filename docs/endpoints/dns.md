# DNS

*Section: API Solutions*

DNS lookup APIs (live, historical, reverse, bulk)

4 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Live DNS Lookup

`GET https://api.whoisfreaks.com/v2.0/dns/live`

Real-time DNS record lookup. 1 credit per query.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domainName` | query | no | string |  |  |
| `ipAddress` | query | no | string |  | Use for PTR lookups |
| `type` | query | yes | string | `all` | all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Response** (`DnsResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `ipAddress` | string |  |
| `queryTime` | string |  |
| `status` | boolean |  |
| `domainRegistered` | boolean |  |
| `dnsTypes` | object |  |
| `dnsRecords` | array<DnsRecord> |  |

<details><summary><code>DnsRecord</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `type` | integer | Numeric DNS record type: 1 A, 2 NS, 5 CNAME, 6 SOA, 12 PTR, 15 MX, 16 TXT, 28 AAAA, 99 SPF. |
| `dnsType` | string | Record type name, e.g. A, MX, TXT |
| `name` | string |  |
| `ttl` | integer |  |
| `rawText` | string | The record in zone-file format |
| `rRsetType` | integer |  |
| `singleName` | string | Target host for NS, CNAME and PTR records |
| `address` | string |  |
| `priority` | integer |  |
| `exchange` | string |  |
| `target` | string |  |
| `strings` | array<string> |  |
| `host` | string |  |
| `admin` | string |  |
| `serial` | integer | SOA serial; values above 2^31 are common, so it is 64-bit |
| `refresh` | integer |  |
| `retry` | integer |  |
| `expire` | integer |  |
| `minimum` | integer |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Live DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsLive.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_live parameters:
    #   type (str, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME; default "all"
    #   domain_name (str, optional, keyword)
    #   ip_address (str, optional, keyword): Use for PTR lookups
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.dns_live("A,MX,TXT", domain_name="whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Live DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsLive.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsLive({ type, domainName?, ipAddress?, format? })
//   type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME; default "all"
//   domainName (string, optional)
//   ipAddress (string, optional): Use for PTR lookups
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.dnsLive({ type: "A,MX,TXT", domainName: "whoisfreaks.com" });
  console.log(JSON.stringify(result, null, 2));
}

main().catch(async (err: unknown) => {
  // API errors carry the HTTP response
  if (err instanceof ResponseError) {
    console.error(`HTTP ${err.response.status}: ${await err.response.text()}`);
  } else {
    console.error(err);
  }
  process.exitCode = 1;
});
```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, optional)
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"

	whoisfreaks "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
	// Set the API key once on the context; every call made with ctx sends it.
	ctx := context.WithValue(context.Background(), whoisfreaks.ContextAPIKeys,
		map[string]whoisfreaks.APIKey{"ApiKeyAuth": {Key: os.Getenv("WHOISFREAKS_API_KEY")}})
	client := whoisfreaks.NewAPIClient(whoisfreaks.NewConfiguration())

	result, _, err := client.DNSAPI.DnsLive(ctx).
		DomainName("whoisfreaks.com").Type_("A,MX,TXT").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Historical DNS Lookup

`GET https://api.whoisfreaks.com/v2.0/dns/historical`

All historical DNS records. 2 credits per page (100 records/page).

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domainName` | query | yes | string |  |  |
| `type` | query | yes | string | `all` |  |
| `page` | query | no | integer | `1` |  |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Response** (`HistoricalDnsResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `totalPages` | integer |  |
| `currentPage` | integer |  |
| `totalRecords` | integer |  |
| `historicalDnsRecords` | array<DnsResponse> |  |

<details><summary><code>DnsResponse</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `ipAddress` | string |  |
| `queryTime` | string |  |
| `status` | boolean |  |
| `domainRegistered` | boolean |  |
| `dnsTypes` | object |  |
| `dnsRecords` | array<DnsRecord> |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Historical DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/historical

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsHistorical.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_historical parameters:
    #   domain_name (str, required)
    #   type (str, required): default "all"
    #   page (int, optional, keyword): default 1
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.dns_historical("whoisfreaks.com", "A,MX,TXT", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Historical DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/historical
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsHistorical.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsHistorical({ domainName, type, page?, format? })
//   domainName (string, required)
//   type (string, required): default "all"
//   page (number, optional): default 1
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.dnsHistorical({ domainName: "whoisfreaks.com", type: "A,MX,TXT", page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch(async (err: unknown) => {
  // API errors carry the HTTP response
  if (err instanceof ResponseError) {
    console.error(`HTTP ${err.response.status}: ${await err.response.text()}`);
  } else {
    console.error(err);
  }
  process.exitCode = 1;
});
```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"

	whoisfreaks "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
	// Set the API key once on the context; every call made with ctx sends it.
	ctx := context.WithValue(context.Background(), whoisfreaks.ContextAPIKeys,
		map[string]whoisfreaks.APIKey{"ApiKeyAuth": {Key: os.Getenv("WHOISFREAKS_API_KEY")}})
	client := whoisfreaks.NewAPIClient(whoisfreaks.NewConfiguration())

	result, _, err := client.DNSAPI.DnsHistorical(ctx).
		DomainName("whoisfreaks.com").Type_("A,MX,TXT").Page(1).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Reverse DNS Lookup

`GET https://api.whoisfreaks.com/v2.1/dns/reverse`

Search domains by IP or DNS value. 5 credits per page.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `value` | query | yes | string |  | IP, CIDR, or record value |
| `type` | query | yes | string |  |  (one of: a, mx, cname, ns, aaaa, txt, soa) |
| `exact` | query | no | boolean | `true` |  |
| `page` | query | no | integer | `1` |  |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Response** (`ReverseDnsResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `totalRecords` | integer |  |
| `totalPages` | integer |  |
| `currentPage` | integer |  |
| `reverseDnsRecords` | array<DnsResponse> |  |

<details><summary><code>DnsResponse</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `ipAddress` | string |  |
| `queryTime` | string |  |
| `status` | boolean |  |
| `domainRegistered` | boolean |  |
| `dnsTypes` | object |  |
| `dnsRecords` | array<DnsRecord> |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Reverse DNS Lookup: GET https://api.whoisfreaks.com/v2.1/dns/reverse

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsReverse.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_reverse parameters:
    #   value (str, required): IP, CIDR, or record value
    #   type (str, required): one of a, mx, cname, ns, aaaa, txt, soa
    #   exact (bool, optional, keyword): default True
    #   page (int, optional, keyword): default 1
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.dns_reverse("8.8.8.8", "a", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Reverse DNS Lookup: GET https://api.whoisfreaks.com/v2.1/dns/reverse
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsReverse.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsReverse({ value, type, exact?, page?, format? })
//   value (string, required): IP, CIDR, or record value
//   type ("a" | "mx" | "cname" | "ns" | "aaaa" | "txt" | "soa", required)
//   exact (boolean, optional): default true
//   page (number, optional): default 1
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.dnsReverse({ value: "8.8.8.8", type: "a", page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch(async (err: unknown) => {
  // API errors carry the HTTP response
  if (err instanceof ResponseError) {
    console.error(`HTTP ${err.response.status}: ${await err.response.text()}`);
  } else {
    console.error(err);
  }
  process.exitCode = 1;
});
```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"

	whoisfreaks "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
	// Set the API key once on the context; every call made with ctx sends it.
	ctx := context.WithValue(context.Background(), whoisfreaks.ContextAPIKeys,
		map[string]whoisfreaks.APIKey{"ApiKeyAuth": {Key: os.Getenv("WHOISFREAKS_API_KEY")}})
	client := whoisfreaks.NewAPIClient(whoisfreaks.NewConfiguration())

	result, _, err := client.DNSAPI.DnsReverse(ctx).Value("8.8.8.8").Type_("a").Page(1).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Bulk DNS Lookup

`POST https://api.whoisfreaks.com/v2.0/dns/bulk/live`

Up to 100 domains + 100 IPs in one request.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `type` | query | yes | string | `all` |  |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Request body** (`application/json`, model `DnsBulkRequest`)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domainNames` | array<string> | no |  |
| `ipAddresses` | array<string> | no |  |

Example: `{"domainNames": ["whoisfreaks.com", "example.com"]}`

**Response** (`BulkDnsResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `bulk_dns_info` | array<DnsResponse> |  |

<details><summary><code>DnsResponse</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `ipAddress` | string |  |
| `queryTime` | string |  |
| `status` | boolean |  |
| `domainRegistered` | boolean |  |
| `dnsTypes` | object |  |
| `dnsRecords` | array<DnsRecord> |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Bulk DNS Lookup: POST https://api.whoisfreaks.com/v2.0/dns/bulk/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsBulk.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_bulk parameters:
    #   type (str, required): default "all"
    #   dns_bulk_request (DnsBulkRequest, required): request body
    #   format (str, optional, keyword): one of json, xml; default "json"
    body = whoisfreaks.DnsBulkRequest(domain_names=["whoisfreaks.com", "example.com"])
    result = api.dns_bulk("A,MX,TXT", body)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Bulk DNS Lookup: POST https://api.whoisfreaks.com/v2.0/dns/bulk/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsBulk.ts
import { Configuration, DNSApi, ResponseError, type DnsBulkRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsBulk({ type, dnsBulkRequest, format? })
//   type (string, required): default "all"
//   dnsBulkRequest (DnsBulkRequest, required): request body
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const body: DnsBulkRequest = { domainNames: ["whoisfreaks.com", "example.com"] };
  const result = await api.dnsBulk({ type: "A,MX,TXT", dnsBulkRequest: body });
  console.log(JSON.stringify(result, null, 2));
}

main().catch(async (err: unknown) => {
  // API errors carry the HTTP response
  if (err instanceof ResponseError) {
    console.error(`HTTP ${err.response.status}: ${await err.response.text()}`);
  } else {
    console.error(err);
  }
  process.exitCode = 1;
});
```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required): request body object

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"

	whoisfreaks "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
	// Set the API key once on the context; every call made with ctx sends it.
	ctx := context.WithValue(context.Background(), whoisfreaks.ContextAPIKeys,
		map[string]whoisfreaks.APIKey{"ApiKeyAuth": {Key: os.Getenv("WHOISFREAKS_API_KEY")}})
	client := whoisfreaks.NewAPIClient(whoisfreaks.NewConfiguration())

	body := whoisfreaks.NewDnsBulkRequest()
	body.SetDomainNames([]string{"whoisfreaks.com", "example.com"})
	result, _, err := client.DNSAPI.DnsBulk(ctx).Type_("A,MX,TXT").DnsBulkRequest(*body).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
