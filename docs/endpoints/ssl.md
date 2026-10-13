# SSL

*Section: API Solutions*

SSL certificate lookup

1 endpoint. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## SSL Certificate Lookup

`GET https://api.whoisfreaks.com/v1.0/ssl/live`

Real-time SSL cert with optional chain.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domainName` | query | yes | string |  |  |
| `chain` | query | no | boolean | `false` |  |
| `sslRaw` | query | no | boolean | `false` |  |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Response** (`SslResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `queryTime` | string |  |
| `sslCertificates` | array<SslCertificate> |  |
| `sslRaw` | string |  |

<details><summary><code>SslCertificate</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `chainOrder` | string |  |
| `authenticationType` | string |  |
| `validityStartDate` | string |  |
| `validityEndDate` | string |  |
| `serialNumber` | string |  |
| `signatureAlgorithm` | string |  |
| `subject` | SslUnitInfo |  |
| `issuer` | SslUnitInfo |  |
| `publicKey` | SslPublicKeyInfo |  |
| `extensions` | SslExtensionsInfo |  |
| `pemRaw` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""SSL Certificate Lookup: GET https://api.whoisfreaks.com/v1.0/ssl/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python SslLookup.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.SSLApi(client)

    # ssl_lookup parameters:
    #   domain_name (str, required)
    #   chain (bool, optional, keyword): default False
    #   ssl_raw (bool, optional, keyword): default False
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.ssl_lookup("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// SSL Certificate Lookup: GET https://api.whoisfreaks.com/v1.0/ssl/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx SslLookup.ts
import { Configuration, SSLApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new SSLApi(config);

// sslLookup({ domainName, chain?, sslRaw?, format? })
//   domainName (string, required)
//   chain (boolean, optional): default false
//   sslRaw (boolean, optional): default false
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.sslLookup({ domainName: "whoisfreaks.com" });
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
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
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

	result, _, err := client.SSLAPI.SslLookup(ctx).DomainName("whoisfreaks.com").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
