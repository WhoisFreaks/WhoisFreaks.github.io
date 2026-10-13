# Databases - IP Geolocation

*Section: Databases*

IP geolocation database snapshots

4 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## IP to Country Snapshot Status

`GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/country`

IP to Country Snapshot Status. Returns the file/snapshot described by this operation.

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
"""IP to Country Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/country

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpCountryStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPGeolocationApi(client)

    # db_ip_country_status takes no parameters.
    result = api.db_ip_country_status()
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP to Country Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/country
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbIpCountryStatus.ts
import { Configuration, DatabasesIPGeolocationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesIPGeolocationApi(config);

// dbIpCountryStatus() takes no parameters.
async function main(): Promise<void> {
  const result = await api.dbIpCountryStatus();
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
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
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

	result, _, err := client.DatabasesIPGeolocationAPI.DbIpCountryStatus(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## IP to Country Snapshot

`GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/country`

IP to Country Snapshot. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  |  |

**Usage**

<details><summary>Python</summary>

```python
"""IP to Country Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/country

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpCountry.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPGeolocationApi(client)

    # db_ip_country parameters:
    #   var_date (datetime.date, required)
    data = api.db_ip_country(date(2026, 10, 1))  # the file's raw bytes
    path = "DbIpCountry.zip"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP to Country Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/country
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbIpCountry.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesIPGeolocationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesIPGeolocationApi(config);

// dbIpCountry({ date })
//   date (Date, required)
async function main(): Promise<void> {
  const blob = await api.dbIpCountry({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbIpCountry.zip";
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
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
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

	file, _, err := client.DatabasesIPGeolocationAPI.DbIpCountry(ctx).Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbIpCountry.zip")
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

## IP to City Snapshot Status

`GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/city`

IP to City Snapshot Status. Returns the file/snapshot described by this operation.

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
"""IP to City Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/city

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpCityStatus.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPGeolocationApi(client)

    # db_ip_city_status takes no parameters.
    result = api.db_ip_city_status()
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP to City Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/city
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbIpCityStatus.ts
import { Configuration, DatabasesIPGeolocationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesIPGeolocationApi(config);

// dbIpCityStatus() takes no parameters.
async function main(): Promise<void> {
  const result = await api.dbIpCityStatus();
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
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
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

	result, _, err := client.DatabasesIPGeolocationAPI.DbIpCityStatus(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## IP to City Snapshot

`GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/city`

IP to City Snapshot. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  |  |

**Usage**

<details><summary>Python</summary>

```python
"""IP to City Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/city

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbIpCity.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesIPGeolocationApi(client)

    # db_ip_city parameters:
    #   var_date (datetime.date, required)
    data = api.db_ip_city(date(2026, 10, 1))  # the file's raw bytes
    path = "DbIpCity.zip"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// IP to City Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/city
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbIpCity.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesIPGeolocationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesIPGeolocationApi(config);

// dbIpCity({ date })
//   date (Date, required)
async function main(): Promise<void> {
  const blob = await api.dbIpCity({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbIpCity.zip";
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
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
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

	file, _, err := client.DatabasesIPGeolocationAPI.DbIpCity(ctx).Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbIpCity.zip")
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
