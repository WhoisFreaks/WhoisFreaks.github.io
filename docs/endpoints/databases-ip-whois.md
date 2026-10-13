# Databases - IP WHOIS

*Section: Databases*

IP WHOIS database snapshots

2 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## IP WHOIS Snapshot

`GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/whois`

IP WHOIS Snapshot. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  |  |

**Usage**

<details><summary>Python</summary>

```python
"""IP WHOIS Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpWhois.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPWHOISApi(client)

    # db_ip_whois parameters:
    #   var_date (datetime.date, required)
    data = api.db_ip_whois(date(2026, 10, 1))  # the file's raw bytes
    path = "DbIpWhois.json.gz"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP WHOIS Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbIpWhois.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesIPWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesIPWHOISApi(config);

// dbIpWhois({ date })
//   date (Date, required)
async function main(): Promise<void> {
  const blob = await api.dbIpWhois({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbIpWhois.json.gz";
  await writeFile(file, new Uint8Array(await blob.arrayBuffer()));
  console.log(`Saved ${blob.size} bytes to ${resolve(file)}`);
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
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)

package main

import (
	"context"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"

	whoisfreaks "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
	// Set the API key once on the context; every call made with ctx sends it.
	ctx := context.WithValue(context.Background(), whoisfreaks.ContextAPIKeys,
		map[string]whoisfreaks.APIKey{"ApiKeyAuth": {Key: os.Getenv("WHOISFREAKS_API_KEY")}})
	client := whoisfreaks.NewAPIClient(whoisfreaks.NewConfiguration())

	file, _, err := client.DatabasesIPWHOISAPI.DbIpWhois(ctx).Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbIpWhois.json.gz")
	if err != nil {
		log.Fatal(err)
	}
	defer out.Close()
	n, err := io.Copy(out, file)
	if err != nil {
		log.Fatal(err)
	}
	path, _ := filepath.Abs(out.Name())
	fmt.Printf("Saved %d bytes to %s\n", n, path)
}

```

</details>

---

## IP WHOIS Snapshot Status

`GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/whois`

IP WHOIS Snapshot Status. Returns the file/snapshot described by this operation.

**Parameters**

None. The API key is set once on the client.

**Response** (`SnapshotStatus`)

| Field | Type | Description |
|-------|------|-------------|
| `status` | string |  |
| `snapshot_creation_date` | string |  |
| `snapshot_name` | string |  |
| `snapshot_deletion_time` | string |  |
| `message` | string |  |


**Usage**

<details><summary>Python</summary>

```python
"""IP WHOIS Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/whois

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpWhoisStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPWHOISApi(client)

    # db_ip_whois_status takes no parameters.
    result = api.db_ip_whois_status()
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP WHOIS Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbIpWhoisStatus.ts
import { Configuration, DatabasesIPWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesIPWHOISApi(config);

// dbIpWhoisStatus() takes no parameters.
async function main(): Promise<void> {
  const result = await api.dbIpWhoisStatus();
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
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
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

	result, _, err := client.DatabasesIPWHOISAPI.DbIpWhoisStatus(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
