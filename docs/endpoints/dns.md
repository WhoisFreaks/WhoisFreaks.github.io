# DNS

*Section: API Solutions*

DNS lookup APIs (live, historical, reverse, bulk)

8 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Live DNS Lookup

`GET https://api.whoisfreaks.com/v2.0/dns/live`

Real-time DNS record lookup. 1 credit per query.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domainName` | query | no | string |  | Domain to look up. |
| `ipAddress` | query | no | string |  | Use for PTR lookups |
| `type` | query | yes | string | `all` | all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME |
| `format` | query | no | string | `json` | Response format. JSON when the parameter is left out. (one of: json, xml) |

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
    #   domain_name (str, optional, keyword): Domain to look up
    #   ip_address (str, optional, keyword): Use for PTR lookups
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
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
//   domainName (string, optional): Domain to look up
//   ipAddress (string, optional): Use for PTR lookups
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
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
//   - domainName (string, optional): Domain to look up.
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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
| `domainName` | query | yes | string |  | Domain to look up. |
| `type` | query | yes | string | `all` | Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all. |
| `page` | query | no | integer | `1` | Page of results to return. Defaults to 1. |
| `format` | query | no | string | `json` | Response format. JSON when the parameter is left out. (one of: json, xml) |

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
    #   domain_name (str, required): Domain to look up
    #   type (str, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
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
//   domainName (string, required): Domain to look up
//   type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
//   page (number, optional): Page of results to return. Defaults to 1; default 1
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
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
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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
| `type` | query | yes | string |  | DNS record type to search by. (one of: a, mx, cname, ns, aaaa, txt, soa) |
| `exact` | query | no | boolean | `false` | Set true to match value exactly. Defaults to false, where value is treated as a pattern and '*' matches any characters. Ignored for A and AAAA records, which always match the IP. |
| `page` | query | no | integer | `1` | Page of results to return. Defaults to 1. |
| `format` | query | no | string | `json` | Response format. JSON when the parameter is left out. (one of: json, xml) |

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
    #   type (str, required): DNS record type to search by; one of a, mx, cname, ns, aaaa, txt, soa
    #   exact (bool, optional, keyword): Set true to match value exactly. Defaults to false, where value is treated as...; default False
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
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
//   type ("a" | "mx" | "cname" | "ns" | "aaaa" | "txt" | "soa", required): DNS record type to search by
//   exact (boolean, optional): Set true to match value exactly. Defaults to false, where value is treated as...; default false
//   page (number, optional): Page of results to return. Defaults to 1; default 1
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
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
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): Set true to match value exactly. Defaults to false, where value is treated as a pattern...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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

## Historical DNS Lookup (v2.2)

`GET https://api.whoisfreaks.com/v2.2/dns/historical`

Same records as /v2.0/dns/historical, with two differences. Each entry reports firstSeen and lastSeen instead of queryTime, and the results can be sorted. 2 credits per page (100 records/page).

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domainName` | query | yes | string |  | Domain to look up. |
| `type` | query | yes | string | `all` | Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all. |
| `page` | query | no | integer | `1` | Page of results to return. Defaults to 1. |
| `sort` | query | no | string |  | Sort direction. Omit to leave the results unsorted. (one of: asc, desc) |
| `sortBy` | query | no | string | `lastSeen` | Field to sort on. Only applies when sort is given. (one of: firstSeen, lastSeen) |
| `format` | query | no | string | `json` | Response format. JSON when the parameter is left out. (one of: json, xml) |

**Response** (`HistoricalDnsResponseV2_2`)

| Field | Type | Description |
|-------|------|-------------|
| `totalRecords` | integer |  |
| `totalPages` | integer |  |
| `currentPage` | integer |  |
| `historicalDnsRecords` | array<DnsEntryV2_2> |  |

<details><summary><code>DnsEntryV2_2</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `ipAddress` | string |  |
| `firstSeen` | string | Date the record was first observed (yyyy-MM-dd) |
| `lastSeen` | string | Date the record was last observed (yyyy-MM-dd) |
| `status` | boolean |  |
| `domainRegistered` | boolean |  |
| `dnsTypes` | object |  |
| `dnsRecords` | array<DnsRecord> |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Historical DNS Lookup (v2.2): GET https://api.whoisfreaks.com/v2.2/dns/historical

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsHistoricalV22.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_historical_v22 parameters:
    #   domain_name (str, required): Domain to look up
    #   type (str, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   sort (str, optional, keyword): Sort direction. Omit to leave the results unsorted; one of asc, desc
    #   sort_by (str, optional, keyword): Field to sort on. Only applies when sort is given; one of firstSeen, lastSeen; default "lastSeen"
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
    result = api.dns_historical_v22("whoisfreaks.com", "A,MX,TXT", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Historical DNS Lookup (v2.2): GET https://api.whoisfreaks.com/v2.2/dns/historical
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsHistoricalV22.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsHistoricalV22({ domainName, type, page?, sort?, sortBy?, format? })
//   domainName (string, required): Domain to look up
//   type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
//   page (number, optional): Page of results to return. Defaults to 1; default 1
//   sort ("asc" | "desc", optional): Sort direction. Omit to leave the results unsorted
//   sortBy ("firstSeen" | "lastSeen", optional): Field to sort on. Only applies when sort is given; default "lastSeen"
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
async function main(): Promise<void> {
  const result = await api.dnsHistoricalV22({ domainName: "whoisfreaks.com", type: "A,MX,TXT", page: 1 });
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
// Runnable example: Historical DNS Lookup (v2.2) (GET /v2.2/dns/historical)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dnsHistoricalV22 (GET /v2.2/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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

	result, _, err := client.DNSAPI.DnsHistoricalV22(ctx).
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

## Historical DNS Lookup (v2.3)

`GET https://api.whoisfreaks.com/v2.3/dns/historical`

Same response as /v2.2/dns/historical. The difference is in error handling. Up to v2.2 a query that failed or ran past the server time limit still returned HTTP 200 with totalRecords 0, which was indistinguishable from a domain with no history. From v2.3 that case returns HTTP 408 instead. 2 credits per page (100 records/page).

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domainName` | query | yes | string |  | Domain to look up. |
| `type` | query | yes | string | `all` | Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all. |
| `page` | query | no | integer | `1` | Page of results to return. Defaults to 1. |
| `sort` | query | no | string |  | Sort direction. Omit to leave the results unsorted. (one of: asc, desc) |
| `sortBy` | query | no | string | `lastSeen` | Field to sort on. Only applies when sort is given. (one of: firstSeen, lastSeen) |
| `format` | query | no | string | `json` | Response format. JSON when the parameter is left out. (one of: json, xml) |

**Response** (`HistoricalDnsResponseV2_2`)

| Field | Type | Description |
|-------|------|-------------|
| `totalRecords` | integer |  |
| `totalPages` | integer |  |
| `currentPage` | integer |  |
| `historicalDnsRecords` | array<DnsEntryV2_2> |  |

<details><summary><code>DnsEntryV2_2</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `ipAddress` | string |  |
| `firstSeen` | string | Date the record was first observed (yyyy-MM-dd) |
| `lastSeen` | string | Date the record was last observed (yyyy-MM-dd) |
| `status` | boolean |  |
| `domainRegistered` | boolean |  |
| `dnsTypes` | object |  |
| `dnsRecords` | array<DnsRecord> |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Historical DNS Lookup (v2.3): GET https://api.whoisfreaks.com/v2.3/dns/historical

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsHistoricalV23.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_historical_v23 parameters:
    #   domain_name (str, required): Domain to look up
    #   type (str, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   sort (str, optional, keyword): Sort direction. Omit to leave the results unsorted; one of asc, desc
    #   sort_by (str, optional, keyword): Field to sort on. Only applies when sort is given; one of firstSeen, lastSeen; default "lastSeen"
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
    result = api.dns_historical_v23("whoisfreaks.com", "A,MX,TXT", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Historical DNS Lookup (v2.3): GET https://api.whoisfreaks.com/v2.3/dns/historical
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsHistoricalV23.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsHistoricalV23({ domainName, type, page?, sort?, sortBy?, format? })
//   domainName (string, required): Domain to look up
//   type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
//   page (number, optional): Page of results to return. Defaults to 1; default 1
//   sort ("asc" | "desc", optional): Sort direction. Omit to leave the results unsorted
//   sortBy ("firstSeen" | "lastSeen", optional): Field to sort on. Only applies when sort is given; default "lastSeen"
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
async function main(): Promise<void> {
  const result = await api.dnsHistoricalV23({ domainName: "whoisfreaks.com", type: "A,MX,TXT", page: 1 });
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
// Runnable example: Historical DNS Lookup (v2.3) (GET /v2.3/dns/historical)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dnsHistoricalV23 (GET /v2.3/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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

	result, _, err := client.DNSAPI.DnsHistoricalV23(ctx).
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

## Reverse DNS Lookup (v2.2)

`GET https://api.whoisfreaks.com/v2.2/dns/reverse`

Same search as /v2.1/dns/reverse. Each entry reports firstSeen and lastSeen instead of queryTime, and the results can be sorted. 5 credits per page.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `value` | query | yes | string |  | IP, CIDR, or record value |
| `type` | query | yes | string |  | DNS record type to search by. (one of: a, mx, cname, ns, aaaa, txt, soa) |
| `exact` | query | no | boolean | `true` | When false the value is matched as a substring, which is far slower than an exact match on a large record type. |
| `page` | query | no | integer | `1` | Page of results to return. Defaults to 1. |
| `sort` | query | no | string |  | Sort direction. Omit to leave the results unsorted. (one of: asc, desc) |
| `sortBy` | query | no | string | `lastSeen` | Field to sort on. Only applies when sort is given. (one of: firstSeen, lastSeen) |
| `format` | query | no | string | `json` | Response format. JSON when the parameter is left out. (one of: json, xml) |

**Response** (`ReverseDnsResponseV2_2`)

| Field | Type | Description |
|-------|------|-------------|
| `totalRecords` | integer |  |
| `totalPages` | integer |  |
| `currentPage` | integer |  |
| `reverseDnsRecords` | array<DnsEntryV2_2> |  |

<details><summary><code>DnsEntryV2_2</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `ipAddress` | string |  |
| `firstSeen` | string | Date the record was first observed (yyyy-MM-dd) |
| `lastSeen` | string | Date the record was last observed (yyyy-MM-dd) |
| `status` | boolean |  |
| `domainRegistered` | boolean |  |
| `dnsTypes` | object |  |
| `dnsRecords` | array<DnsRecord> |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Reverse DNS Lookup (v2.2): GET https://api.whoisfreaks.com/v2.2/dns/reverse

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsReverseV22.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_reverse_v22 parameters:
    #   value (str, required): IP, CIDR, or record value
    #   type (str, required): DNS record type to search by; one of a, mx, cname, ns, aaaa, txt, soa
    #   exact (bool, optional, keyword): When false the value is matched as a substring, which is far slower than an e...; default True
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   sort (str, optional, keyword): Sort direction. Omit to leave the results unsorted; one of asc, desc
    #   sort_by (str, optional, keyword): Field to sort on. Only applies when sort is given; one of firstSeen, lastSeen; default "lastSeen"
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
    result = api.dns_reverse_v22("8.8.8.8", "a", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Reverse DNS Lookup (v2.2): GET https://api.whoisfreaks.com/v2.2/dns/reverse
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsReverseV22.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsReverseV22({ value, type, exact?, page?, sort?, sortBy?, format? })
//   value (string, required): IP, CIDR, or record value
//   type ("a" | "mx" | "cname" | "ns" | "aaaa" | "txt" | "soa", required): DNS record type to search by
//   exact (boolean, optional): When false the value is matched as a substring, which is far slower than an e...; default true
//   page (number, optional): Page of results to return. Defaults to 1; default 1
//   sort ("asc" | "desc", optional): Sort direction. Omit to leave the results unsorted
//   sortBy ("firstSeen" | "lastSeen", optional): Field to sort on. Only applies when sort is given; default "lastSeen"
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
async function main(): Promise<void> {
  const result = await api.dnsReverseV22({ value: "8.8.8.8", type: "a", page: 1 });
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
// Runnable example: Reverse DNS Lookup (v2.2) (GET /v2.2/dns/reverse)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dnsReverseV22 (GET /v2.2/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): When false the value is matched as a substring, which is far slower than an exact match...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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

	result, _, err := client.DNSAPI.DnsReverseV22(ctx).Value("8.8.8.8").Type_("a").Page(1).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Reverse DNS Lookup (v2.3)

`GET https://api.whoisfreaks.com/v2.3/dns/reverse`

Same search as /v2.2/dns/reverse, with a bounded total. Counting every match of a broad search can take minutes, so from v2.3 the count stops at 10,000 and totalRecordsCapped reports whether it did. When totalRecordsCapped is true the real total is higher than totalRecords and totalPages is capped with it. Earlier versions still return the exact total. A query that runs past the server time limit returns HTTP 408. 5 credits per page.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `value` | query | yes | string |  | IP, CIDR, or record value |
| `type` | query | yes | string |  | DNS record type to search by. (one of: a, mx, cname, ns, aaaa, txt, soa) |
| `exact` | query | no | boolean | `true` | When false the value is matched as a substring, which is far slower than an exact match on a large record type. |
| `page` | query | no | integer | `1` | Page of results to return. Defaults to 1. |
| `sort` | query | no | string |  | Sort direction. Omit to leave the results unsorted. (one of: asc, desc) |
| `sortBy` | query | no | string | `lastSeen` | Field to sort on. Only applies when sort is given. (one of: firstSeen, lastSeen) |
| `format` | query | no | string | `json` | Response format. JSON when the parameter is left out. (one of: json, xml) |

**Response** (`ReverseDnsResponseV2_3`)

| Field | Type | Description |
|-------|------|-------------|
| `totalRecords` | integer | Matching records. When totalRecordsCapped is true this is the cap, not the real total. |
| `totalRecordsCapped` | boolean | True when counting stopped at the 10,000 cap, so the real total is higher. Present from v2.3 only. |
| `totalPages` | integer |  |
| `currentPage` | integer |  |
| `reverseDnsRecords` | array<DnsEntryV2_2> |  |

<details><summary><code>DnsEntryV2_2</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `ipAddress` | string |  |
| `firstSeen` | string | Date the record was first observed (yyyy-MM-dd) |
| `lastSeen` | string | Date the record was last observed (yyyy-MM-dd) |
| `status` | boolean |  |
| `domainRegistered` | boolean |  |
| `dnsTypes` | object |  |
| `dnsRecords` | array<DnsRecord> |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Reverse DNS Lookup (v2.3): GET https://api.whoisfreaks.com/v2.3/dns/reverse

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DnsReverseV23.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DNSApi(client)

    # dns_reverse_v23 parameters:
    #   value (str, required): IP, CIDR, or record value
    #   type (str, required): DNS record type to search by; one of a, mx, cname, ns, aaaa, txt, soa
    #   exact (bool, optional, keyword): When false the value is matched as a substring, which is far slower than an e...; default True
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   sort (str, optional, keyword): Sort direction. Omit to leave the results unsorted; one of asc, desc
    #   sort_by (str, optional, keyword): Field to sort on. Only applies when sort is given; one of firstSeen, lastSeen; default "lastSeen"
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
    result = api.dns_reverse_v23("8.8.8.8", "a", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Reverse DNS Lookup (v2.3): GET https://api.whoisfreaks.com/v2.3/dns/reverse
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsReverseV23.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsReverseV23({ value, type, exact?, page?, sort?, sortBy?, format? })
//   value (string, required): IP, CIDR, or record value
//   type ("a" | "mx" | "cname" | "ns" | "aaaa" | "txt" | "soa", required): DNS record type to search by
//   exact (boolean, optional): When false the value is matched as a substring, which is far slower than an e...; default true
//   page (number, optional): Page of results to return. Defaults to 1; default 1
//   sort ("asc" | "desc", optional): Sort direction. Omit to leave the results unsorted
//   sortBy ("firstSeen" | "lastSeen", optional): Field to sort on. Only applies when sort is given; default "lastSeen"
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
async function main(): Promise<void> {
  const result = await api.dnsReverseV23({ value: "8.8.8.8", type: "a", page: 1 });
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
// Runnable example: Reverse DNS Lookup (v2.3) (GET /v2.3/dns/reverse)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dnsReverseV23 (GET /v2.3/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): When false the value is matched as a substring, which is far slower than an exact match...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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

	result, _, err := client.DNSAPI.DnsReverseV23(ctx).Value("8.8.8.8").Type_("a").Page(1).Execute()
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
| `type` | query | yes | string | `all` | Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all. |
| `format` | query | no | string | `json` | Response format. JSON when the parameter is left out. (one of: json, xml) |

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
    #   type (str, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
    #   dns_bulk_request (DnsBulkRequest, required): request body
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
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
//   type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
//   dnsBulkRequest (DnsBulkRequest, required): request body
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
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
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
