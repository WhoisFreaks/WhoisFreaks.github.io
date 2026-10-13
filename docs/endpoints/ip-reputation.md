# IP Reputation

*Section: API Solutions*

IP threat intelligence

2 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## IP Reputation Lookup

`GET https://api.whoisfreaks.com/v1.0/security`

Threat intel for IP: VPN, proxy, Tor, bots. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `ip` | query | yes | string |  |  |

**Response** (`IpReputationResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `ip` | string |  |
| `location` | IpLocation |  |
| `network` | IpSecurityNetwork |  |
| `asn` | IpSecurityAsn |  |
| `security` | IpSecurity |  |

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

<details><summary><code>IpSecurityNetwork</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `connection_type` | string |  |
| `route` | string |  |
| `is_anycast` | boolean |  |

</details>

<details><summary><code>IpSecurityAsn</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `as_number` | string |  |
| `organization` | string |  |
| `country` | string |  |
| `type` | string |  |
| `domain` | string |  |
| `date_allocated` | string |  |
| `rir` | string |  |

</details>

<details><summary><code>IpSecurity</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `threat_score` | integer |  |
| `is_tor` | boolean |  |
| `is_proxy` | boolean |  |
| `proxy_provider_names` | array<string> |  |
| `proxy_confidence_score` | integer |  |
| `proxy_last_seen` | string |  |
| `is_residential_proxy` | boolean |  |
| `is_vpn` | boolean |  |
| `vpn_provider_names` | array<string> |  |
| `vpn_confidence_score` | integer |  |
| `vpn_last_seen` | string |  |
| `is_relay` | boolean |  |
| `relay_provider_name` | string |  |
| `is_anonymous` | boolean |  |
| `is_known_attacker` | boolean |  |
| `is_bot` | boolean |  |
| `is_spam` | boolean |  |
| `is_cloud_provider` | boolean |  |
| `cloud_provider_name` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""IP Reputation Lookup: GET https://api.whoisfreaks.com/v1.0/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python IpReputation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.IPReputationApi(client)

    # ip_reputation parameters:
    #   ip (str, required)
    result = api.ip_reputation("8.8.8.8")
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP Reputation Lookup: GET https://api.whoisfreaks.com/v1.0/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx IpReputation.ts
import { Configuration, IPReputationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new IPReputationApi(config);

// ipReputation({ ip })
//   ip (string, required)
async function main(): Promise<void> {
  const result = await api.ipReputation({ ip: "8.8.8.8" });
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
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for ipReputation (GET /v1.0/security):
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

	result, _, err := client.IPReputationAPI.IpReputation(ctx).Ip("8.8.8.8").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Bulk IP Reputation

`POST https://api.whoisfreaks.com/v1.0/security`

Up to 100 IPs.

**Parameters**

None. The API key is set once on the client.

**Request body** (`application/json`, model `BulkGeolocationRequest`)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ips` | array<string> | yes | Up to 100 items. |

Example: `{"ips": ["8.8.8.8", "1.1.1.1"]}`

**Response** (array of `IpReputationResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `ip` | string |  |
| `location` | IpLocation |  |
| `network` | IpSecurityNetwork |  |
| `asn` | IpSecurityAsn |  |
| `security` | IpSecurity |  |

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

<details><summary><code>IpSecurityNetwork</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `connection_type` | string |  |
| `route` | string |  |
| `is_anycast` | boolean |  |

</details>

<details><summary><code>IpSecurityAsn</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `as_number` | string |  |
| `organization` | string |  |
| `country` | string |  |
| `type` | string |  |
| `domain` | string |  |
| `date_allocated` | string |  |
| `rir` | string |  |

</details>

<details><summary><code>IpSecurity</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `threat_score` | integer |  |
| `is_tor` | boolean |  |
| `is_proxy` | boolean |  |
| `proxy_provider_names` | array<string> |  |
| `proxy_confidence_score` | integer |  |
| `proxy_last_seen` | string |  |
| `is_residential_proxy` | boolean |  |
| `is_vpn` | boolean |  |
| `vpn_provider_names` | array<string> |  |
| `vpn_confidence_score` | integer |  |
| `vpn_last_seen` | string |  |
| `is_relay` | boolean |  |
| `relay_provider_name` | string |  |
| `is_anonymous` | boolean |  |
| `is_known_attacker` | boolean |  |
| `is_bot` | boolean |  |
| `is_spam` | boolean |  |
| `is_cloud_provider` | boolean |  |
| `cloud_provider_name` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Bulk IP Reputation: POST https://api.whoisfreaks.com/v1.0/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkIpReputation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.IPReputationApi(client)

    # bulk_ip_reputation parameters:
    #   bulk_geolocation_request (BulkGeolocationRequest, required): request body
    body = whoisfreaks.BulkGeolocationRequest(ips=["8.8.8.8", "1.1.1.1"])
    results = api.bulk_ip_reputation(body)
    print(json.dumps([item.to_dict() for item in results], indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Bulk IP Reputation: POST https://api.whoisfreaks.com/v1.0/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkIpReputation.ts
import { Configuration, IPReputationApi, ResponseError, type BulkGeolocationRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new IPReputationApi(config);

// bulkIpReputation({ bulkGeolocationRequest })
//   bulkGeolocationRequest (BulkGeolocationRequest, required): request body
async function main(): Promise<void> {
  const body: BulkGeolocationRequest = { ips: ["8.8.8.8", "1.1.1.1"] };
  const results = await api.bulkIpReputation({ bulkGeolocationRequest: body });
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
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for bulkIpReputation (POST /v1.0/security):
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
	result, _, err := client.IPReputationAPI.BulkIpReputation(ctx).
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
