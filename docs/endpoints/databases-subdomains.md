# Databases - Subdomains

*Section: Databases*

Subdomain database snapshots

3 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Subdomains Daily

`GET https://files.whoisfreaks.com/v3.2/download/dbupdate/daily/subdomains`

Subdomains Daily. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Subdomains Daily: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/daily/subdomains

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbSubdomainsDaily.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesSubdomainsApi(client)

    # db_subdomains_daily parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_subdomains_daily(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbSubdomainsDaily.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Subdomains Daily: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/daily/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbSubdomainsDaily.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesSubdomainsApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesSubdomainsApi(config);

// dbSubdomainsDaily({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbSubdomainsDaily({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbSubdomainsDaily.csv";
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
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest

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

	file, _, err := client.DatabasesSubdomainsAPI.DbSubdomainsDaily(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbSubdomainsDaily.csv")
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

## Subdomains Weekly

`GET https://files.whoisfreaks.com/v3.2/download/dbupdate/weekly/subdomains`

Subdomains Weekly. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Subdomains Weekly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/weekly/subdomains

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbSubdomainsWeekly.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesSubdomainsApi(client)

    # db_subdomains_weekly parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_subdomains_weekly(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbSubdomainsWeekly.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Subdomains Weekly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/weekly/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbSubdomainsWeekly.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesSubdomainsApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesSubdomainsApi(config);

// dbSubdomainsWeekly({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbSubdomainsWeekly({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbSubdomainsWeekly.csv";
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
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest

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

	file, _, err := client.DatabasesSubdomainsAPI.DbSubdomainsWeekly(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbSubdomainsWeekly.csv")
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

## Subdomains Monthly

`GET https://files.whoisfreaks.com/v3.2/download/dbupdate/monthly/subdomains`

Subdomains Monthly. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Subdomains Monthly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/monthly/subdomains

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbSubdomainsMonthly.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesSubdomainsApi(client)

    # db_subdomains_monthly parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_subdomains_monthly(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbSubdomainsMonthly.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Subdomains Monthly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/monthly/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbSubdomainsMonthly.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesSubdomainsApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesSubdomainsApi(config);

// dbSubdomainsMonthly({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbSubdomainsMonthly({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbSubdomainsMonthly.csv";
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
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest

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

	file, _, err := client.DatabasesSubdomainsAPI.DbSubdomainsMonthly(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbSubdomainsMonthly.csv")
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
