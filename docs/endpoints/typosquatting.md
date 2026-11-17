# Typosquatting

*Section: API Solutions*

Detect typo variants of brand domains

2 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Typosquatting Lookup

`GET https://api.whoisfreaks.com/v3.0/domain/typos`

Find typo variants of a brand. 5 credits per page.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `keyword` | query | no | string |  | Brand or label to find typo variants for. Pass either keyword or pattern, not both. |
| `pattern` | query | no | string |  | Wildcard search string, where '*' matches any characters. Pass either keyword or pattern, not both. |
| `pageToken` | query | no | string |  | Token from nextPageToken in the previous response, needed from page 2 onward. Send it with the original keyword or pattern. |

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
    #   keyword (str, optional, keyword): Brand or label to find typo variants for. Pass either keyword or pattern, not...
    #   pattern (str, optional, keyword): Wildcard search string, where '*' matches any characters. Pass either keyword...
    #   page_token (str, optional, keyword): Token from nextPageToken in the previous response, needed from page 2 onward....
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
//   keyword (string, optional): Brand or label to find typo variants for. Pass either keyword or pattern, not...
//   pattern (string, optional): Wildcard search string, where '*' matches any characters. Pass either keyword...
//   pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward....
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
//   - keyword (string, optional): Brand or label to find typo variants for. Pass either keyword or pattern, not both.
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters. Pass either keyword or patter...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...

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

## Subdomain Typosquatting Lookup

`GET https://api.whoisfreaks.com/v3.0/subdomains/typos`

Find subdomains that carry a typo variant of a brand as one of their labels, such as login.paypa1.example.com. Phishing pages often hide the brand in the subdomain of an unrelated domain, so these hosts never show up in a domain typosquatting search. Pass either keyword or pattern, not both. 5 credits per page.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `keyword` | query | no | string |  | Brand or label to find typo variants for. 3 to 63 characters, letters, digits and hyphens, a single label with no dots, and it cannot start or end with a hyphen. |
| `pattern` | query | no | string |  | Wildcard search string, where '*' matches any characters and '?' matches one. At most 2 wildcards, at least 5 characters besides the wildcards, and no more than 63 characters in total. |
| `pageToken` | query | no | string |  | Token from nextPageToken in the previous response, needed from page 2 onward. Send it with the original keyword or pattern. |
| `fetch_size` | query | no | integer | `100` | Subdomains per page. 100 when the parameter is left out, and values above 10000 are capped at 10000. |

**Response** (`TyposquatSubdomainsResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `status` | boolean |  |
| `totalRecords` | integer |  |
| `currentPage` | integer |  |
| `totalPages` | integer |  |
| `hasNextPage` | boolean |  |
| `nextPageToken` | string |  |
| `subdomains` | array<TyposquatSubdomain> |  |

<details><summary><code>TyposquatSubdomain</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `subdomain` | string | The matching hostname. |
| `domain` | string | The registrable domain the subdomain belongs to. |
| `status` | string | Whether the subdomain is still resolving. |
| `firstSeen` | string | Date the subdomain was first seen, in YYYY-MM-DD format. |
| `lastSeen` | string | Date the subdomain was last seen, in YYYY-MM-DD format. |
| `inactiveFrom` | string | Date the subdomain stopped resolving, absent while it is active. |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Subdomain Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/subdomains/typos

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python SubdomainTyposquatting.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.TyposquattingApi(client)

    # subdomain_typosquatting parameters:
    #   keyword (str, optional, keyword): Brand or label to find typo variants for. 3 to 63 characters, letters, digits...
    #   pattern (str, optional, keyword): Wildcard search string, where '*' matches any characters and '?' matches one....
    #   page_token (str, optional, keyword): Token from nextPageToken in the previous response, needed from page 2 onward....
    #   fetch_size (int, optional, keyword): Subdomains per page. 100 when the parameter is left out, and values above 100...; default 100
    result = api.subdomain_typosquatting()
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Subdomain Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/subdomains/typos
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx SubdomainTyposquatting.ts
import { Configuration, TyposquattingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new TyposquattingApi(config);

// subdomainTyposquatting({ keyword?, pattern?, pageToken?, fetch_size? })
//   keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits...
//   pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one....
//   pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward....
//   fetch_size (number, optional): Subdomains per page. 100 when the parameter is left out, and values above 100...; default 100
async function main(): Promise<void> {
  const result = await api.subdomainTyposquatting();
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
// Runnable example: Subdomain Typosquatting Lookup (GET /v3.0/subdomains/typos)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for subdomainTyposquatting (GET /v3.0/subdomains/typos):
//   - keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits and hyphe...
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one. At most 2...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
//   - fetch_size (integer, optional): Subdomains per page. 100 when the parameter is left out, and values above 10000 are cap...

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

	result, _, err := client.TyposquattingAPI.SubdomainTyposquatting(ctx).Keyword("paypal").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
