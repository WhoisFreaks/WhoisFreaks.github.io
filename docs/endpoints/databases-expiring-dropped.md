# Databases - Expiring & Dropped

*Section: Databases*

Expiring and dropped domain downloads

5 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Expiring Domains

`GET https://files.whoisfreaks.com/v3.1/download/domainer/expired`

Expiring Domains. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | yes | boolean |  |  |
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Expiring Domains: GET https://files.whoisfreaks.com/v3.1/download/domainer/expired

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbExpired.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesExpiringDroppedApi(client)

    # db_expired parameters:
    #   whois (bool, required)
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_expired(True, var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbExpired.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Expiring Domains: GET https://files.whoisfreaks.com/v3.1/download/domainer/expired
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbExpired.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesExpiringDroppedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesExpiringDroppedApi(config);

// dbExpired({ whois, date? })
//   whois (boolean, required)
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbExpired({ whois: true, date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbExpired.csv";
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
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
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

	file, _, err := client.DatabasesExpiringDroppedAPI.DbExpired(ctx).
		Whois(true).Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbExpired.csv")
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

## Expiring Cleaned WHOIS

`GET https://files.whoisfreaks.com/v3.1/download/domainer/expired/cleaned`

Expiring Cleaned WHOIS. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Expiring Cleaned WHOIS: GET https://files.whoisfreaks.com/v3.1/download/domainer/expired/cleaned

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbExpiredCleaned.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesExpiringDroppedApi(client)

    # db_expired_cleaned parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_expired_cleaned(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbExpiredCleaned.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Expiring Cleaned WHOIS: GET https://files.whoisfreaks.com/v3.1/download/domainer/expired/cleaned
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbExpiredCleaned.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesExpiringDroppedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesExpiringDroppedApi(config);

// dbExpiredCleaned({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbExpiredCleaned({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbExpiredCleaned.csv";
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
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
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

	file, _, err := client.DatabasesExpiringDroppedAPI.DbExpiredCleaned(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbExpiredCleaned.csv")
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

## Dropped Domains

`GET https://files.whoisfreaks.com/v3.1/download/domainer/dropped`

Dropped Domains. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | yes | boolean |  |  |
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Dropped Domains: GET https://files.whoisfreaks.com/v3.1/download/domainer/dropped

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbDropped.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesExpiringDroppedApi(client)

    # db_dropped parameters:
    #   whois (bool, required)
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_dropped(True, var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbDropped.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Dropped Domains: GET https://files.whoisfreaks.com/v3.1/download/domainer/dropped
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbDropped.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesExpiringDroppedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesExpiringDroppedApi(config);

// dbDropped({ whois, date? })
//   whois (boolean, required)
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbDropped({ whois: true, date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbDropped.csv";
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
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - whois (boolean, required)
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

	file, _, err := client.DatabasesExpiringDroppedAPI.DbDropped(ctx).
		Whois(true).Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbDropped.csv")
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

## Dropped Domains (JSON)

`GET https://files.whoisfreaks.com/v3.1/domains/dropped`

Dropped Domains (JSON). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |
| `tlds` | query | no | string |  |  |

**Usage**

<details><summary>Python</summary>

```python
"""Dropped Domains (JSON): GET https://files.whoisfreaks.com/v3.1/domains/dropped

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbDroppedJson.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesExpiringDroppedApi(client)

    # db_dropped_json parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    domains = api.db_dropped_json(var_date=date(2026, 10, 1))
    print(f"{len(domains)} domains")
    print("\n".join(domains[:10]))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Dropped Domains (JSON): GET https://files.whoisfreaks.com/v3.1/domains/dropped
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbDroppedJson.ts
import { Configuration, DatabasesExpiringDroppedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesExpiringDroppedApi(config);

// dbDroppedJson({ date?, tlds? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
//   tlds (string, optional)
async function main(): Promise<void> {
  const domains = await api.dbDroppedJson({ date: new Date("2026-10-01") });
  console.log(`${domains.length} domains`);
  console.log(domains.slice(0, 10).join("\n"));
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
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)

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

	result, _, err := client.DatabasesExpiringDroppedAPI.DbDroppedJson(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Dropped With Backlinks

`GET https://files.whoisfreaks.com/v3.3/download/domainer/dropped/backlinks`

Dropped With Backlinks. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | no | boolean |  |  |
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Dropped With Backlinks: GET https://files.whoisfreaks.com/v3.3/download/domainer/dropped/backlinks

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbDroppedBacklinks.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesExpiringDroppedApi(client)

    # db_dropped_backlinks parameters:
    #   whois (bool, optional, keyword)
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_dropped_backlinks(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbDroppedBacklinks.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Dropped With Backlinks: GET https://files.whoisfreaks.com/v3.3/download/domainer/dropped/backlinks
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbDroppedBacklinks.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesExpiringDroppedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesExpiringDroppedApi(config);

// dbDroppedBacklinks({ whois?, date? })
//   whois (boolean, optional)
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbDroppedBacklinks({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbDroppedBacklinks.csv";
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
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional)
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

	file, _, err := client.DatabasesExpiringDroppedAPI.DbDroppedBacklinks(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbDroppedBacklinks.csv")
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
