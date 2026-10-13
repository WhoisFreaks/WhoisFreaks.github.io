# Geolocation

*Section: API Solutions*

IP geolocation lookup

2 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## IP Geolocation Lookup

`GET https://api.whoisfreaks.com/v1.0/geolocation`

Get location, ASN, currency for an IP. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `ip` | query | yes | string |  |  |

**Response** (`GeolocationResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `ip` | string |  |
| `location` | IpLocation |  |
| `country_metadata` | CountryMetadata |  |
| `network` | GeoNetwork |  |
| `currency` | Currency |  |

<details><summary><code>IpLocation</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `continent_code` | string |  |
| `continent_name` | string |  |
| `country_code2` | string |  |
| `country_code3` | string |  |
| `country_name` | string |  |
| `country_name_official` | string |  |
| `country_capital` | string |  |
| `state_prov` | string |  |
| `state_code` | string |  |
| `district` | string |  |
| `city` | string |  |
| `locality` | string |  |
| `accuracy_radius` | string |  |
| `confidence` | string |  |
| `zipcode` | string |  |
| `latitude` | string |  |
| `longitude` | string |  |
| `is_eu` | boolean |  |
| `geoname_id` | string |  |
| `country_emoji` | string |  |

</details>

<details><summary><code>CountryMetadata</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `calling_code` | string |  |
| `tld` | string |  |
| `languages` | array<string> |  |

</details>

<details><summary><code>GeoNetwork</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `asn` | GeoAsn |  |
| `connection_type` | string |  |
| `company` | GeoCompany |  |

</details>

<details><summary><code>Currency</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `code` | string |  |
| `name` | string |  |
| `symbol` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""IP Geolocation Lookup: GET https://api.whoisfreaks.com/v1.0/geolocation

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python Geolocation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.GeolocationApi(client)

    # geolocation parameters:
    #   ip (str, required)
    result = api.geolocation("8.8.8.8")
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP Geolocation Lookup: GET https://api.whoisfreaks.com/v1.0/geolocation
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx Geolocation.ts
import { Configuration, GeolocationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new GeolocationApi(config);

// geolocation({ ip })
//   ip (string, required)
async function main(): Promise<void> {
  const result = await api.geolocation({ ip: "8.8.8.8" });
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
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)

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

	result, _, err := client.GeolocationAPI.Geolocation(ctx).Ip("8.8.8.8").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Bulk IP Geolocation

`POST https://api.whoisfreaks.com/v1.0/geolocation`

Up to 100 IPs.

**Parameters**

None. The API key is set once on the client.

**Request body** (`application/json`, model `BulkGeolocationRequest`)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ips` | array<string> | yes | Up to 100 items. |

Example: `{"ips": ["8.8.8.8", "1.1.1.1"]}`

**Response** (array of `GeolocationResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `ip` | string |  |
| `location` | IpLocation |  |
| `country_metadata` | CountryMetadata |  |
| `network` | GeoNetwork |  |
| `currency` | Currency |  |

<details><summary><code>IpLocation</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `continent_code` | string |  |
| `continent_name` | string |  |
| `country_code2` | string |  |
| `country_code3` | string |  |
| `country_name` | string |  |
| `country_name_official` | string |  |
| `country_capital` | string |  |
| `state_prov` | string |  |
| `state_code` | string |  |
| `district` | string |  |
| `city` | string |  |
| `locality` | string |  |
| `accuracy_radius` | string |  |
| `confidence` | string |  |
| `zipcode` | string |  |
| `latitude` | string |  |
| `longitude` | string |  |
| `is_eu` | boolean |  |
| `geoname_id` | string |  |
| `country_emoji` | string |  |

</details>

<details><summary><code>CountryMetadata</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `calling_code` | string |  |
| `tld` | string |  |
| `languages` | array<string> |  |

</details>

<details><summary><code>GeoNetwork</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `asn` | GeoAsn |  |
| `connection_type` | string |  |
| `company` | GeoCompany |  |

</details>

<details><summary><code>Currency</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `code` | string |  |
| `name` | string |  |
| `symbol` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Bulk IP Geolocation: POST https://api.whoisfreaks.com/v1.0/geolocation

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkGeolocation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.GeolocationApi(client)

    # bulk_geolocation parameters:
    #   bulk_geolocation_request (BulkGeolocationRequest, required): request body
    body = whoisfreaks.BulkGeolocationRequest(ips=["8.8.8.8", "1.1.1.1"])
    results = api.bulk_geolocation(body)
    print(json.dumps([item.to_dict() for item in results], indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Bulk IP Geolocation: POST https://api.whoisfreaks.com/v1.0/geolocation
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkGeolocation.ts
import { Configuration, GeolocationApi, ResponseError, type BulkGeolocationRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new GeolocationApi(config);

// bulkGeolocation({ bulkGeolocationRequest })
//   bulkGeolocationRequest (BulkGeolocationRequest, required): request body
async function main(): Promise<void> {
  const body: BulkGeolocationRequest = { ips: ["8.8.8.8", "1.1.1.1"] };
  const results = await api.bulkGeolocation({ bulkGeolocationRequest: body });
  console.log(JSON.stringify(results, null, 2));
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
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required): request body object

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

	body := whoisfreaks.NewBulkGeolocationRequest([]string{"8.8.8.8", "1.1.1.1"})
	result, _, err := client.GeolocationAPI.BulkGeolocation(ctx).
		BulkGeolocationRequest(*body).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
