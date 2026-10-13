# ASN WHOIS

*Section: API Solutions*

Autonomous System Number WHOIS

1 endpoint. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## ASN WHOIS Lookup

`GET https://api.whoisfreaks.com/v2.0/asn-whois`

WHOIS for an ASN. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `asn` | query | yes | string |  |  |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Response** (`AsnWhoisResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `asn` | AsnInfo |  |

<details><summary><code>AsnInfo</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `as_number` | string |  |
| `organization` | string |  |
| `country` | string |  |
| `type` | string |  |
| `domain` | string |  |
| `date_allocated` | string |  |
| `asn_name` | string |  |
| `allocation_status` | string |  |
| `num_of_ipv4_routes` | string |  |
| `num_of_ipv6_routes` | string |  |
| `rir` | string |  |
| `routes` | array<string> |  |
| `downstreams` | array<AsnPeer> |  |
| `upstreams` | array<AsnPeer> |  |
| `peers` | array<AsnPeer> |  |
| `whois_response` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""ASN WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/asn-whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python AsnWhois.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.ASNWHOISApi(client)

    # asn_whois parameters:
    #   asn (str, required)
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.asn_whois("as15169")
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// ASN WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/asn-whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx AsnWhois.ts
import { Configuration, ASNWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new ASNWHOISApi(config);

// asnWhois({ asn, format? })
//   asn (string, required)
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.asnWhois({ asn: "as15169" });
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
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
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

	result, _, err := client.ASNWHOISAPI.AsnWhois(ctx).Asn("as15169").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
