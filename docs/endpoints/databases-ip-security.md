# Databases - IP Security

*Section: Databases*

IP security database snapshots

2 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## IP Security Snapshot

`GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/security`

IP Security Snapshot. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  |  |

**Usage**

<details><summary>Python</summary>

```python
"""IP Security Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpSecurity.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPSecurityApi(client)

    # db_ip_security parameters:
    #   var_date (datetime.date, required)
    data = api.db_ip_security(date(2026, 10, 1))  # the file's raw bytes
    path = "DbIpSecurity.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP Security Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbIpSecurity.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesIPSecurityApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesIPSecurityApi(config);

// dbIpSecurity({ date })
//   date (Date, required)
async function main(): Promise<void> {
  const blob = await api.dbIpSecurity({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbIpSecurity.csv";
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
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
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

	file, _, err := client.DatabasesIPSecurityAPI.DbIpSecurity(ctx).Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbIpSecurity.csv")
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

## IP Security Snapshot Status

`GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/security`

IP Security Snapshot Status. Returns the file/snapshot described by this operation.

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
"""IP Security Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpSecurityStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPSecurityApi(client)

    # db_ip_security_status takes no parameters.
    result = api.db_ip_security_status()
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP Security Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbIpSecurityStatus.ts
import { Configuration, DatabasesIPSecurityApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesIPSecurityApi(config);

// dbIpSecurityStatus() takes no parameters.
async function main(): Promise<void> {
  const result = await api.dbIpSecurityStatus();
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
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
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

	result, _, err := client.DatabasesIPSecurityAPI.DbIpSecurityStatus(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
