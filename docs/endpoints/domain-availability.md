# Domain Availability

*Section: API Solutions*

Check domain availability

2 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Domain Availability Check with Suggestions

`GET https://api.whoisfreaks.com/v2.0/domain/availability`

Check availability of a single domain and optionally get suggestions across multiple TLDs. 1 credit per domain checked. sug=false checks only the queried domain; sug=true returns up to `count` (max 100) TLD suggestions.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domain` | query | yes | string |  | The domain name to check |
| `sug` | query | no | boolean | `false` | Whether to return TLD suggestions alongside the queried domain. |
| `count` | query | no | integer | `5` | Number of TLD suggestions to return when sug=true. Maximum is 100. |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Response** (`DomainAvailabilityResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `domain` | string |  |
| `availability` | string |  |
| `message` | string |  |
| `domain_available_response` | array<DomainAvailabilityItem> |  |

<details><summary><code>DomainAvailabilityItem</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domain` | string |  |
| `availability` | string |  |
| `status` | boolean |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Domain Availability Check with Suggestions: GET https://api.whoisfreaks.com/v2.0/domain/availability

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DomainAvailabilityV2.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DomainAvailabilityApi(client)

    # domain_availability_v2 parameters:
    #   domain (str, required): The domain name to check
    #   sug (bool, optional, keyword): Whether to return TLD suggestions alongside the queried domain; default False
    #   count (int, optional, keyword): Number of TLD suggestions to return when sug=true. Maximum is 100; default 5
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.domain_availability_v2("google.com", sug=True, count=5)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Domain Availability Check with Suggestions: GET https://api.whoisfreaks.com/v2.0/domain/availability
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DomainAvailabilityV2.ts
import { Configuration, DomainAvailabilityApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DomainAvailabilityApi(config);

// domainAvailabilityV2({ domain, sug?, count?, format? })
//   domain (string, required): The domain name to check
//   sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain; default false
//   count (number, optional): Number of TLD suggestions to return when sug=true. Maximum is 100; default 5
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.domainAvailabilityV2({ domain: "google.com", sug: true, count: 5 });
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
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
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

	result, _, err := client.DomainAvailabilityAPI.DomainAvailabilityV2(ctx).
		Domain("google.com").Sug(true).Count(5).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Bulk Domain Availability Check

`POST https://api.whoisfreaks.com/v2.0/domain/availability`

Two bulk modes. Mode 1: POST domainNames array. Mode 2: POST tld array plus domain query param. Max 100 domains per request. 1 credit per domain checked.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domain` | query | no | string |  | Required for TLD-mode bulk check (base domain). |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Request body** (`application/json`, model `BulkDomainAvailabilityRequest`)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domainNames` | array<string> | no | Mode 1: list of full domain names. Cannot be used with tld. |
| `tld` | array<string> | no | Mode 2: TLDs to check against the domain query param. Cannot be used with domainNames. |

Example: `{"domainNames": ["whoisfreaks.com", "example.com"]}`

**Response** (`BulkDomainAvailabilityResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `bulk_domain_availability_response` | array<DomainAvailabilityItem> |  |

<details><summary><code>DomainAvailabilityItem</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domain` | string |  |
| `availability` | string |  |
| `status` | boolean |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Bulk Domain Availability Check: POST https://api.whoisfreaks.com/v2.0/domain/availability

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkDomainAvailabilityV2.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DomainAvailabilityApi(client)

    # bulk_domain_availability_v2 parameters:
    #   bulk_domain_availability_request (BulkDomainAvailabilityRequest, required): request body
    #   domain (str, optional, keyword): Required for TLD-mode bulk check (base domain)
    #   format (str, optional, keyword): one of json, xml; default "json"
    body = whoisfreaks.BulkDomainAvailabilityRequest(domain_names=["whoisfreaks.com", "example.com"])
    result = api.bulk_domain_availability_v2(body)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Bulk Domain Availability Check: POST https://api.whoisfreaks.com/v2.0/domain/availability
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkDomainAvailabilityV2.ts
import { Configuration, DomainAvailabilityApi, ResponseError, type BulkDomainAvailabilityRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DomainAvailabilityApi(config);

// bulkDomainAvailabilityV2({ bulkDomainAvailabilityRequest, domain?, format? })
//   bulkDomainAvailabilityRequest (BulkDomainAvailabilityRequest, required): request body
//   domain (string, optional): Required for TLD-mode bulk check (base domain)
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const body: BulkDomainAvailabilityRequest = { domainNames: ["whoisfreaks.com", "example.com"] };
  const result = await api.bulkDomainAvailabilityV2({ bulkDomainAvailabilityRequest: body });
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
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required): request body object

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

	body := whoisfreaks.NewBulkDomainAvailabilityRequest()
	body.SetDomainNames([]string{"whoisfreaks.com", "example.com"})
	result, _, err := client.DomainAvailabilityAPI.BulkDomainAvailabilityV2(ctx).
		BulkDomainAvailabilityRequest(*body).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
