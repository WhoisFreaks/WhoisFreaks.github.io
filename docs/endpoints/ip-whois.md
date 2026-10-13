# IP WHOIS

*Section: API Solutions*

IP address WHOIS

1 endpoint. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## IP WHOIS Lookup

`GET https://api.whoisfreaks.com/v1.0/ip-whois`

WHOIS for an IP address. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `ip` | query | yes | string |  |  |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Response** (`IpWhoisResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `status` | boolean |  |
| `ip_address` | string |  |
| `as_number` | string |  |
| `query_time` | string |  |
| `whois_server` | string |  |
| `whois_raw_response` | string |  |
| `r_whois_raw_response` | string |  |
| `inet_nums` | array<InetNum> |  |
| `organization` | WhoisOrganization |  |
| `irt` | Irt |  |
| `administrative_contacts` | array<WhoisPerson> |  |
| `technical_contacts` | array<WhoisPerson> |  |
| `abuse_contacts` | array<WhoisPerson> |  |
| `routes` | array<Route> |  |

<details><summary><code>InetNum</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `start_ip` | string |  |
| `end_ip` | string |  |
| `cidr` | array<string> |  |
| `net_name` | string |  |
| `net_handle` | string |  |
| `description` | array<string> |  |
| `countries` | array<string> |  |
| `geofeed` | string |  |
| `latitude` | number |  |
| `longitude` | number |  |
| `city` | string |  |
| `languages` | array<string> |  |
| `status` | string |  |
| `organization` | string |  |
| `sponsoring_organization` | string |  |
| `remarks` | array<string> |  |
| `assignment_size` | string |  |
| `notify` | array<string> |  |
| `mnt_by` | array<string> |  |
| `mnt_lower` | array<string> |  |
| `mnt_domains` | array<string> |  |
| `mnt_routes` | array<string> |  |
| `mnt_irt` | array<string> |  |
| `date_created` | string |  |
| `date_updated` | string |  |
| `source` | string |  |
| `parents` | array<string> |  |

</details>

<details><summary><code>WhoisOrganization</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `handle` | string |  |
| `name` | string |  |
| `type` | string |  |
| `description` | array<string> |  |
| `address` | array<string> |  |
| `street` | string |  |
| `city` | string |  |
| `district` | string |  |
| `state` | string |  |
| `zip_code` | string |  |
| `country` | array<string> |  |
| `latitude` | number |  |
| `longitude` | number |  |
| `email` | array<string> |  |
| `abuse_mailbox` | array<string> |  |
| `phone` | array<string> |  |
| `fax_no` | array<string> |  |
| `organizations` | array<string> |  |
| `admin_contacts` | array<string> |  |
| `tech_contacts` | array<string> |  |
| `abuse_contacts` | array<string> |  |
| `languages` | array<string> |  |
| `remarks` | array<string> |  |
| `notify` | array<string> |  |
| `ref_nfy` | array<string> |  |
| `mnt_ref` | array<string> |  |
| `mnt_by` | array<string> |  |
| `date_created` | string |  |
| `date_updated` | string |  |
| `source` | string |  |

</details>

<details><summary><code>Irt</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `handle` | string |  |
| `address` | array<string> |  |
| `street` | string |  |
| `city` | string |  |
| `district` | string |  |
| `state` | string |  |
| `zip_code` | string |  |
| `country` | string |  |
| `email` | array<string> |  |
| `abuse_mailbox` | array<string> |  |
| `phone` | array<string> |  |
| `fax_no` | array<string> |  |
| `organizations` | array<string> |  |
| `admin_contacts` | array<string> |  |
| `tech_contacts` | array<string> |  |
| `remarks` | array<string> |  |
| `signature` | array<string> |  |
| `encryption` | array<string> |  |
| `auth` | array<string> |  |
| `notify` | array<string> |  |
| `irt_nfy` | array<string> |  |
| `mnt_by` | array<string> |  |
| `mnt_ref` | array<string> |  |

</details>

<details><summary><code>WhoisPerson</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `handle` | string |  |
| `name` | string |  |
| `address` | array<string> |  |
| `street` | string |  |
| `city` | string |  |
| `district` | string |  |
| `state` | string |  |
| `zip_code` | string |  |
| `country` | string |  |
| `email` | array<string> |  |
| `abuse_mailbox` | array<string> |  |
| `phone` | array<string> |  |
| `fax_no` | array<string> |  |
| `organizations` | array<string> |  |
| `admin_contacts` | array<string> |  |
| `tech_contacts` | array<string> |  |
| `remarks` | array<string> |  |
| `notify` | array<string> |  |
| `mnt_by` | array<string> |  |
| `mnt_ref` | array<string> |  |
| `date_created` | string |  |
| `date_updated` | string |  |
| `source` | string |  |

</details>

<details><summary><code>Route</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `route` | string |  |
| `description` | array<string> |  |
| `origin` | string |  |
| `pingable` | array<string> |  |
| `ping_hdl` | array<string> |  |
| `holes` | array<string> |  |
| `country` | string |  |
| `organizations` | array<string> |  |
| `member_of` | array<string> |  |
| `inject` | array<string> |  |
| `aggr_mtd` | string |  |
| `aggr_bndry` | string |  |
| `export_comps` | string |  |
| `components` | string |  |
| `remarks` | array<string> |  |
| `notify` | array<string> |  |
| `mnt_lower` | array<string> |  |
| `mnt_routes` | array<string> |  |
| `mnt_by` | array<string> |  |
| `date_created` | string |  |
| `date_updated` | string |  |
| `source` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""IP WHOIS Lookup: GET https://api.whoisfreaks.com/v1.0/ip-whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python IpWhois.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.IPWHOISApi(client)

    # ip_whois parameters:
    #   ip (str, required)
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.ip_whois("8.8.8.8")
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP WHOIS Lookup: GET https://api.whoisfreaks.com/v1.0/ip-whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx IpWhois.ts
import { Configuration, IPWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new IPWHOISApi(config);

// ipWhois({ ip, format? })
//   ip (string, required)
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.ipWhois({ ip: "8.8.8.8" });
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
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
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

	result, _, err := client.IPWHOISAPI.IpWhois(ctx).Ip("8.8.8.8").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
