# Account

*Section: Account & Utilities*

Account, API key, and usage utilities

3 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Rotate API Key

`GET https://api.whoisfreaks.com/v1.0/api-key/rotate`

Rotate API Key. Returns the file/snapshot described by this operation.

**Parameters**

None. The API key is set once on the client.

**Usage**

<details><summary>Python</summary>

```python
"""Rotate API Key: GET https://api.whoisfreaks.com/v1.0/api-key/rotate

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python RotateApiKey.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.AccountApi(client)

    # rotate_api_key takes no parameters.
    new_key = api.rotate_api_key()  # use this key from now on
    print("New API key:", new_key)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Rotate API Key: GET https://api.whoisfreaks.com/v1.0/api-key/rotate
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx RotateApiKey.ts
import { Configuration, AccountApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new AccountApi(config);

// rotateApiKey() takes no parameters.
async function main(): Promise<void> {
  const newKey = await api.rotateApiKey(); // use this key from now on
  console.log("New API key:", newKey);
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
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)

package main

import (
	"context"
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

	newKey, _, err := client.AccountAPI.RotateApiKey(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.
	fmt.Println("New API key:", newKey)
}

```

</details>

---

## Account Usage

`GET https://api.whoisfreaks.com/v1.0/whoisapi/usage`

Account Usage. Returns the file/snapshot described by this operation.

**Parameters**

None. The API key is set once on the client.

**Response** (`AccountUsageResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `apiKey` | string |  |
| `apiCredits` | ApiCredits |  |
| `apiSubscription` | ApiSubscription |  |

<details><summary><code>ApiCredits</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `totalCredits` | integer |  |
| `servedRequest` | integer |  |

</details>

<details><summary><code>ApiSubscription</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `requestLimit` | integer |  |
| `servedRequests` | integer |  |
| `subscriptionStatus` | string |  |
| `surchargeRequestLimit` | integer |  |
| `servedSurchargeRequests` | integer |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Account Usage: GET https://api.whoisfreaks.com/v1.0/whoisapi/usage

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python AccountUsage.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.AccountApi(client)

    # account_usage takes no parameters.
    result = api.account_usage()
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Account Usage: GET https://api.whoisfreaks.com/v1.0/whoisapi/usage
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx AccountUsage.ts
import { Configuration, AccountApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new AccountApi(config);

// accountUsage() takes no parameters.
async function main(): Promise<void> {
  const result = await api.accountUsage();
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
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)

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

	result, _, err := client.AccountAPI.AccountUsage(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Database File Status (Public)

`GET https://files.whoisfreaks.com/v3.4/status`

Public endpoint: no API key required.

No API key required. Returns freshness of all downloadable files.

**Parameters**

None. The API key is set once on the client.

**Response** (`DatabaseFileStatus`)

| Field | Type | Description |
|-------|------|-------------|
| `newly` | NewlyStatus |  |
| `expired` | DateRangeStatus |  |
| `cleaned_expired` | DateRangeStatus |  |
| `dropped` | DateRangeStatus |  |
| `dropped_with_backlinks` | DateRangeStatus |  |
| `threat_feed` | ThreatFeedStatus |  |
| `database_updates` | DatabaseUpdates |  |

<details><summary><code>NewlyStatus</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `gtld` | DateRangeStatus |  |
| `cctld` | DateRangeStatus |  |
| `dns` | DateRangeStatus |  |
| `cleaned_gtld` | DateRangeStatus |  |
| `cleaned_cctld` | DateRangeStatus |  |

</details>

<details><summary><code>DateRangeStatus</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `available_from` | string |  |
| `last_update` | string |  |

</details>

<details><summary><code>ThreatFeedStatus</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `phishing` | DateRangeStatus |  |
| `malware` | DateRangeStatus |  |
| `spam` | DateRangeStatus |  |

</details>

<details><summary><code>DatabaseUpdates</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domain_whois` | UpdateFrequencies |  |
| `dns` | UpdateFrequencies |  |
| `subdomains` | UpdateFrequencies |  |
| `ip_whois` | UpdateFrequencies |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Database File Status (Public): GET https://files.whoisfreaks.com/v3.4/status

Run it (public endpoint, no API key needed):
    python DatabaseFileStatus.py
"""
import json

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.AccountApi(client)

    # database_file_status takes no parameters.
    result = api.database_file_status()
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Database File Status (Public): GET https://files.whoisfreaks.com/v3.4/status
// Run (public endpoint, no API key needed): npx tsx DatabaseFileStatus.ts
import { AccountApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new AccountApi();

// databaseFileStatus() takes no parameters.
async function main(): Promise<void> {
  const result = await api.databaseFileStatus();
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
// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; no API key required)

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

	whoisfreaks "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
	// Public endpoint: no API key needed.
	ctx := context.Background()
	client := whoisfreaks.NewAPIClient(whoisfreaks.NewConfiguration())

	result, _, err := client.AccountAPI.DatabaseFileStatus(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
