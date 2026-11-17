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
| `domain` | query | yes | string |  | Domain whose subdomains you want. |
| `after` | query | no | string (date) |  | Only return records created after this date, in YYYY-MM-DD format. Defaults to the oldest record held, and must not be in the future or later than before. |
| `before` | query | no | string (date) |  | Only return records created before this date, in YYYY-MM-DD format. Defaults to today, and must not be in the future. |
| `status` | query | no | string |  | Limit results to active or inactive subdomains. Both are returned when the parameter is left out. (one of: active, inactive) |
| `page` | query | no | integer | `1` | Page of results to return. Defaults to 1. |
| `format` | query | no | string | `json` | Response format. JSON when the parameter is left out. (one of: json, xml) |

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
    #   domain (str, required): Domain whose subdomains you want
    #   after (datetime.date, optional, keyword): Only return records created after this date, in YYYY-MM-DD format. Defaults t...
    #   before (datetime.date, optional, keyword): Only return records created before this date, in YYYY-MM-DD format. Defaults ...
    #   status (str, optional, keyword): Limit results to active or inactive subdomains. Both are returned when the pa...; one of active, inactive
    #   page (int, optional, keyword): Page of results to return. Defaults to 1; default 1
    #   format (str, optional, keyword): Response format. JSON when the parameter is left out; one of json, xml; default "json"
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
//   domain (string, required): Domain whose subdomains you want
//   after (Date, optional): Only return records created after this date, in YYYY-MM-DD format. Defaults t...
//   before (Date, optional): Only return records created before this date, in YYYY-MM-DD format. Defaults ...
//   status ("active" | "inactive", optional): Limit results to active or inactive subdomains. Both are returned when the pa...
//   page (number, optional): Page of results to return. Defaults to 1; default 1
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
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
//   - domain (string, required): Domain whose subdomains you want.
//   - after (string, optional): Only return records created after this date, in YYYY-MM-DD format. Defaults to the olde...
//   - before (string, optional): Only return records created before this date, in YYYY-MM-DD format. Defaults to today, ...
//   - status (string (one of: active, inactive), optional): Limit results to active or inactive subdomains. Both are returned when the parameter is...
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
