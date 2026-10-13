# Subdomains

*Section: API Solutions*

Subdomain enumeration

1 endpoint. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Subdomains Lookup

`GET https://api.whoisfreaks.com/v1.0/subdomains`

All subdomains including nested. 2 credits per query.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domain` | query | yes | string |  |  |
| `after` | query | no | string (date) |  |  |
| `before` | query | no | string (date) |  |  |
| `status` | query | no | string |  |  (one of: active, inactive) |
| `page` | query | no | integer | `1` |  |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Response** (`SubdomainsResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `domain` | string |  |
| `status` | boolean |  |
| `current_page` | integer |  |
| `total_pages` | integer |  |
| `query_time` | string |  |
| `total_records` | integer |  |
| `subdomains` | array<Subdomain> |  |

<details><summary><code>Subdomain</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `subdomain` | string |  |
| `first_seen` | string |  |
| `last_seen` | string |  |
| `inactive_from` | string |  |
| `dns_records` | DnsResponse |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Subdomains Lookup: GET https://api.whoisfreaks.com/v1.0/subdomains

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python Subdomains.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.SubdomainsApi(client)

    # subdomains parameters:
    #   domain (str, required)
    #   after (datetime.date, optional, keyword)
    #   before (datetime.date, optional, keyword)
    #   status (str, optional, keyword): one of active, inactive
    #   page (int, optional, keyword): default 1
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.subdomains("whoisfreaks.com", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Subdomains Lookup: GET https://api.whoisfreaks.com/v1.0/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx Subdomains.ts
import { Configuration, SubdomainsApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new SubdomainsApi(config);

// subdomains({ domain, after?, before?, status?, page?, format? })
//   domain (string, required)
//   after (Date, optional)
//   before (Date, optional)
//   status ("active" | "inactive", optional)
//   page (number, optional): default 1
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.subdomains({ domain: "whoisfreaks.com", page: 1 });
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
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
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

	result, _, err := client.SubdomainsAPI.Subdomains(ctx).Domain("whoisfreaks.com").Page(1).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
