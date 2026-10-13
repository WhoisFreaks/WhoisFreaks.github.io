# WHOIS

*Section: API Solutions*

WHOIS lookup APIs (live, historical, reverse, bulk)

4 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Live WHOIS Lookup

`GET https://api.whoisfreaks.com/v2.0/whois/live`

Real-time WHOIS lookup from authoritative servers. Cost 1 credit.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domainName` | query | yes | string |  |  |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Response** (`WhoisResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `status` | boolean |  |
| `domain_name` | string |  |
| `query_time` | string |  |
| `whois_server` | string |  |
| `domain_registered` | string |  |
| `secure_dns` | boolean |  |
| `domain_handle` | string |  |
| `create_date` | string |  |
| `update_date` | string |  |
| `expiry_date` | string |  |
| `domain_registrar` | RegistrarInformation |  |
| `reseller_contact` | ResellerContact |  |
| `registrant_contact` | PersonalInformation |  |
| `administrative_contact` | PersonalInformation |  |
| `technical_contact` | PersonalInformation |  |
| `billing_contact` | PersonalInformation |  |
| `eligibility_info` | EligibilityInfo |  |
| `abuse_contact` | RegistrarInformation |  |
| `name_servers` | array<string> |  |
| `domain_status` | array<string> |  |
| `whois_raw_domain` | string |  |
| `registry_data` | RegistryData |  |

<details><summary><code>RegistrarInformation</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `id` | string |  |
| `id_type` | string |  |
| `iana_id` | string |  |
| `registry_id` | string |  |
| `handle` | string |  |
| `status` | string |  |
| `registrar_name` | string |  |
| `normalized_name` | string |  |
| `whois_server` | string |  |
| `rdap_server` | string |  |
| `website_url` | string |  |
| `email_address` | string |  |
| `phone_number` | string |  |
| `authoritative_registry_name` | string |  |
| `organization_number` | string |  |
| `is_sponsor` | boolean |  |

</details>

<details><summary><code>ResellerContact</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `name` | string |  |
| `email_address` | string |  |
| `phone` | string |  |

</details>

<details><summary><code>PersonalInformation</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `id` | string |  |
| `id_type` | string |  |
| `handle` | string |  |
| `name` | string |  |
| `company` | string |  |
| `street` | string |  |
| `city` | string |  |
| `state` | string |  |
| `zip_code` | string |  |
| `country_name` | string |  |
| `country_code` | string |  |
| `email_address` | string |  |
| `phone` | string |  |
| `fax` | string |  |
| `mailing_address` | string |  |

</details>

<details><summary><code>EligibilityInfo</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `id` | string |  |
| `name` | string |  |
| `type` | string |  |

</details>

<details><summary><code>RegistryData</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domain_name` | string |  |
| `query_time` | string |  |
| `whois_server` | string |  |
| `domain_registered` | string |  |
| `create_date` | string |  |
| `update_date` | string |  |
| `expiry_date` | string |  |
| `domain_registrar` | RegistrarInformation |  |
| `name_servers` | array<string> |  |
| `domain_status` | array<string> |  |
| `whois_raw_registery` | string | Raw registry WHOIS text (field name spelled as the API returns it) |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Live WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/whois/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python WhoisLive.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # whois_live parameters:
    #   domain_name (str, required)
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.whois_live("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Live WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/whois/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx WhoisLive.ts
import { Configuration, WHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new WHOISApi(config);

// whoisLive({ domainName, format? })
//   domainName (string, required)
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.whoisLive({ domainName: "whoisfreaks.com" });
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
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
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

	result, _, err := client.WHOISAPI.WhoisLive(ctx).DomainName("whoisfreaks.com").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Bulk WHOIS Lookup

`POST https://api.whoisfreaks.com/v2.0/bulkwhois/live`

Up to 100 domains in one request. 1 credit per successful domain.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Request body** (`application/json`, model `BulkWhoisRequest`)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `domainNames` | array<string> | yes | Up to 100 items. |

Example: `{"domainNames": ["whoisfreaks.com", "jfreaks.com"]}`

**Response** (`BulkWhoisResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `bulk_whois_response` | array<BulkWhoisItem> |  |

<details><summary><code>BulkWhoisItem</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `status` | boolean |  |
| `domain_name` | string |  |
| `error` | string |  |
| `query_time` | string |  |
| `whois_server` | string |  |
| `domain_registered` | string |  |
| `secure_dns` | boolean |  |
| `domain_handle` | string |  |
| `create_date` | string |  |
| `update_date` | string |  |
| `expiry_date` | string |  |
| `domain_registrar` | RegistrarInformation |  |
| `reseller_contact` | ResellerContact |  |
| `registrant_contact` | PersonalInformation |  |
| `administrative_contact` | PersonalInformation |  |
| `technical_contact` | PersonalInformation |  |
| `billing_contact` | PersonalInformation |  |
| `eligibility_info` | EligibilityInfo |  |
| `abuse_contact` | RegistrarInformation |  |
| `name_servers` | array<string> |  |
| `domain_status` | array<string> |  |
| `whois_raw_domain` | string |  |
| `registry_data` | RegistryData |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Bulk WHOIS Lookup: POST https://api.whoisfreaks.com/v2.0/bulkwhois/live

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python BulkWhois.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # bulk_whois parameters:
    #   bulk_whois_request (BulkWhoisRequest, required): request body
    #   format (str, optional, keyword): one of json, xml; default "json"
    body = whoisfreaks.BulkWhoisRequest(domain_names=["whoisfreaks.com", "jfreaks.com"])
    result = api.bulk_whois(body)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Bulk WHOIS Lookup: POST https://api.whoisfreaks.com/v2.0/bulkwhois/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkWhois.ts
import { Configuration, WHOISApi, ResponseError, type BulkWhoisRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new WHOISApi(config);

// bulkWhois({ bulkWhoisRequest, format? })
//   bulkWhoisRequest (BulkWhoisRequest, required): request body
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const body: BulkWhoisRequest = { domainNames: ["whoisfreaks.com", "jfreaks.com"] };
  const result = await api.bulkWhois({ bulkWhoisRequest: body });
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
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required): request body object

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

	body := whoisfreaks.NewBulkWhoisRequest([]string{"whoisfreaks.com", "jfreaks.com"})
	result, _, err := client.WHOISAPI.BulkWhois(ctx).BulkWhoisRequest(*body).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Historical WHOIS records for a domain

`GET https://api.whoisfreaks.com/v2.0/whois/history`

Every WHOIS record captured for the domain since 1986, in one response (no pagination). Cost 2 credits.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domainName` | query | yes | string |  | Domain to fetch historical WHOIS records for |
| `format` | query | no | string |  |  (one of: json, xml) |

**Response** (`WhoisHistoricalResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `status` | boolean |  |
| `whois` | string |  |
| `total_records` | string |  |
| `whois_domains_historical` | array<WhoisHistoricalItem> |  |

<details><summary><code>WhoisHistoricalItem</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `num` | integer |  |
| `status` | boolean |  |
| `domain_name` | string |  |
| `query_time` | string |  |
| `whois_server` | string |  |
| `domain_registered` | string |  |
| `secure_dns` | boolean |  |
| `domain_handle` | string |  |
| `create_date` | string |  |
| `update_date` | string |  |
| `expiry_date` | string |  |
| `domain_registrar` | RegistrarInformation |  |
| `reseller_contact` | ResellerContact |  |
| `registrant_contact` | PersonalInformation |  |
| `administrative_contact` | PersonalInformation |  |
| `technical_contact` | PersonalInformation |  |
| `billing_contact` | PersonalInformation |  |
| `eligibility_info` | EligibilityInfo |  |
| `abuse_contact` | RegistrarInformation |  |
| `name_servers` | array<string> |  |
| `domain_status` | array<string> |  |
| `whois_raw_domain` | string |  |
| `registry_data` | RegistryData |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Historical WHOIS records for a domain: GET https://api.whoisfreaks.com/v2.0/whois/history

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python WhoisHistory.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # whois_history parameters:
    #   domain_name (str, required): Domain to fetch historical WHOIS records for
    #   format (str, optional, keyword): one of json, xml
    result = api.whois_history("whoisfreaks.com")
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Historical WHOIS records for a domain: GET https://api.whoisfreaks.com/v2.0/whois/history
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx WhoisHistory.ts
import { Configuration, WHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new WHOISApi(config);

// whoisHistory({ domainName, format? })
//   domainName (string, required): Domain to fetch historical WHOIS records for
//   format ("json" | "xml", optional)
async function main(): Promise<void> {
  const result = await api.whoisHistory({ domainName: "whoisfreaks.com" });
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
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
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

	result, _, err := client.WHOISAPI.WhoisHistory(ctx).DomainName("whoisfreaks.com").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Reverse WHOIS lookup by keyword

`GET https://api.whoisfreaks.com/v2.0/whois/reverse`

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `keyword` | query | yes | string |  | Keyword to search across WHOIS records |
| `page` | query | no | integer |  | Page number |
| `format` | query | no | string |  |  (one of: json, xml) |

**Response** (`ReverseWhoisResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `total_Result` | integer |  |
| `total_Pages` | integer |  |
| `current_Page` | integer |  |
| `whois_domains_historical` | array<WhoisHistoricalItem> |  |

<details><summary><code>WhoisHistoricalItem</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `num` | integer |  |
| `status` | boolean |  |
| `domain_name` | string |  |
| `query_time` | string |  |
| `whois_server` | string |  |
| `domain_registered` | string |  |
| `secure_dns` | boolean |  |
| `domain_handle` | string |  |
| `create_date` | string |  |
| `update_date` | string |  |
| `expiry_date` | string |  |
| `domain_registrar` | RegistrarInformation |  |
| `reseller_contact` | ResellerContact |  |
| `registrant_contact` | PersonalInformation |  |
| `administrative_contact` | PersonalInformation |  |
| `technical_contact` | PersonalInformation |  |
| `billing_contact` | PersonalInformation |  |
| `eligibility_info` | EligibilityInfo |  |
| `abuse_contact` | RegistrarInformation |  |
| `name_servers` | array<string> |  |
| `domain_status` | array<string> |  |
| `whois_raw_domain` | string |  |
| `registry_data` | RegistryData |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Reverse WHOIS lookup by keyword: GET https://api.whoisfreaks.com/v2.0/whois/reverse

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python WhoisReverse.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.WHOISApi(client)

    # whois_reverse parameters:
    #   keyword (str, required): Keyword to search across WHOIS records
    #   page (int, optional, keyword): Page number
    #   format (str, optional, keyword): one of json, xml
    result = api.whois_reverse("whoisfreaks", page=1)
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Reverse WHOIS lookup by keyword: GET https://api.whoisfreaks.com/v2.0/whois/reverse
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx WhoisReverse.ts
import { Configuration, WHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new WHOISApi(config);

// whoisReverse({ keyword, page?, format? })
//   keyword (string, required): Keyword to search across WHOIS records
//   page (number, optional): Page number
//   format ("json" | "xml", optional)
async function main(): Promise<void> {
  const result = await api.whoisReverse({ keyword: "whoisfreaks", page: 1 });
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
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
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

	result, _, err := client.WHOISAPI.WhoisReverse(ctx).Keyword("whoisfreaks").Page(1).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
