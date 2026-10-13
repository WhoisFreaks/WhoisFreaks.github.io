# Typosquatting

*Section: API Solutions*

Detect typo variants of brand domains

1 endpoint. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Typosquatting Lookup

`GET https://api.whoisfreaks.com/v3.0/domain/typos`

Find typo variants of a brand. 5 credits per page.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `keyword` | query | no | string |  |  |
| `pattern` | query | no | string |  |  |
| `pageToken` | query | no | string |  |  |

**Response** (`TyposquattingResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `status` | boolean |  |
| `totalRecords` | integer |  |
| `currentPage` | integer |  |
| `totalPages` | integer |  |
| `hasNextPage` | boolean |  |
| `nextPageToken` | string |  |
| `domains` | array<TyposquattingDomain> |  |

<details><summary><code>TyposquattingDomain</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `createDate` | string |  |
| `expiryDate` | string |  |
| `lastSeen` | string |  |
| `isDropped` | boolean |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/domain/typos

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python Typosquatting.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.TyposquattingApi(client)

    # typosquatting parameters:
    #   keyword (str, optional, keyword)
    #   pattern (str, optional, keyword)
    #   page_token (str, optional, keyword)
    result = api.typosquatting(keyword="whoisfreaks")
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/domain/typos
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx Typosquatting.ts
import { Configuration, TyposquattingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new TyposquattingApi(config);

// typosquatting({ keyword?, pattern?, pageToken? })
//   keyword (string, optional)
//   pattern (string, optional)
//   pageToken (string, optional)
async function main(): Promise<void> {
  const result = await api.typosquatting({ keyword: "whoisfreaks" });
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
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)

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

	result, _, err := client.TyposquattingAPI.Typosquatting(ctx).Keyword("whoisfreaks").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
