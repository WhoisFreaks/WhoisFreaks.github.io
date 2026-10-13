# Databases - Newly Registered

*Section: Databases*

Newly registered domain downloads

7 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Newly Registered gTLD (CSV)

`GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld`

Newly Registered gTLD (CSV). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | yes | boolean |  |  |
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |
| `tlds` | query | no | string |  |  |

**Usage**

<details><summary>Python</summary>

```python
"""Newly Registered gTLD (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyGtld.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_gtld parameters:
    #   whois (bool, required)
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    data = api.db_newly_gtld(True, var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbNewlyGtld.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Newly Registered gTLD (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbNewlyGtld.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesNewlyRegisteredApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesNewlyRegisteredApi(config);

// dbNewlyGtld({ whois, date?, tlds? })
//   whois (boolean, required)
//   date (Date, optional): yyyy-MM-dd; omit for latest
//   tlds (string, optional)
async function main(): Promise<void> {
  const blob = await api.dbNewlyGtld({ whois: true, date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbNewlyGtld.csv";
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
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)

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

	file, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyGtld(ctx).
		Whois(true).Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbNewlyGtld.csv")
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

## Newly Registered ccTLD (CSV)

`GET https://files.whoisfreaks.com/v3.1/download/domainer/cctld`

Newly Registered ccTLD (CSV). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | yes | boolean |  |  |
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |
| `tlds` | query | no | string |  |  |

**Usage**

<details><summary>Python</summary>

```python
"""Newly Registered ccTLD (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/cctld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyCctld.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_cctld parameters:
    #   whois (bool, required)
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    data = api.db_newly_cctld(True, var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbNewlyCctld.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Newly Registered ccTLD (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/cctld
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbNewlyCctld.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesNewlyRegisteredApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesNewlyRegisteredApi(config);

// dbNewlyCctld({ whois, date?, tlds? })
//   whois (boolean, required)
//   date (Date, optional): yyyy-MM-dd; omit for latest
//   tlds (string, optional)
async function main(): Promise<void> {
  const blob = await api.dbNewlyCctld({ whois: true, date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbNewlyCctld.csv";
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
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)

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

	file, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyCctld(ctx).
		Whois(true).Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbNewlyCctld.csv")
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

## Newly Registered gTLD Cleaned WHOIS (CSV)

`GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld/cleaned`

Newly Registered gTLD Cleaned WHOIS (CSV). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Newly Registered gTLD Cleaned WHOIS (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld/cleaned

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyGtldCleaned.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_gtld_cleaned parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_newly_gtld_cleaned(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbNewlyGtldCleaned.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Newly Registered gTLD Cleaned WHOIS (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld/cleaned
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbNewlyGtldCleaned.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesNewlyRegisteredApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesNewlyRegisteredApi(config);

// dbNewlyGtldCleaned({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbNewlyGtldCleaned({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbNewlyGtldCleaned.csv";
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
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
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

	file, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyGtldCleaned(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbNewlyGtldCleaned.csv")
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

## Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET https://files.whoisfreaks.com/v3.1/download/domainer/cctld/cleaned`

Newly Registered ccTLD Cleaned WHOIS (CSV). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Newly Registered ccTLD Cleaned WHOIS (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/cctld/cleaned

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyCctldCleaned.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_cctld_cleaned parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_newly_cctld_cleaned(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbNewlyCctldCleaned.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Newly Registered ccTLD Cleaned WHOIS (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/cctld/cleaned
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbNewlyCctldCleaned.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesNewlyRegisteredApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesNewlyRegisteredApi(config);

// dbNewlyCctldCleaned({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbNewlyCctldCleaned({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbNewlyCctldCleaned.csv";
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
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
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

	file, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyCctldCleaned(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbNewlyCctldCleaned.csv")
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

## Newly Registered gTLD (JSON)

`GET https://files.whoisfreaks.com/v3.1/domains/newly/gtld`

Newly Registered gTLD (JSON). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |
| `tlds` | query | no | string |  |  |

**Usage**

<details><summary>Python</summary>

```python
"""Newly Registered gTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/gtld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyGtldJson.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_gtld_json parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    domains = api.db_newly_gtld_json(var_date=date(2026, 10, 1))
    print(f"{len(domains)} domains")
    print("\n".join(domains[:10]))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Newly Registered gTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/gtld
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbNewlyGtldJson.ts
import { Configuration, DatabasesNewlyRegisteredApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesNewlyRegisteredApi(config);

// dbNewlyGtldJson({ date?, tlds? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
//   tlds (string, optional)
async function main(): Promise<void> {
  const domains = await api.dbNewlyGtldJson({ date: new Date("2026-10-01") });
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
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
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

	result, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyGtldJson(ctx).
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

## Newly Registered ccTLD (JSON)

`GET https://files.whoisfreaks.com/v3.1/domains/newly/cctld`

Newly Registered ccTLD (JSON). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |
| `tlds` | query | no | string |  |  |

**Usage**

<details><summary>Python</summary>

```python
"""Newly Registered ccTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/cctld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyCctldJson.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_cctld_json parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    #   tlds (str, optional, keyword)
    domains = api.db_newly_cctld_json(var_date=date(2026, 10, 1))
    print(f"{len(domains)} domains")
    print("\n".join(domains[:10]))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Newly Registered ccTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/cctld
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbNewlyCctldJson.ts
import { Configuration, DatabasesNewlyRegisteredApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesNewlyRegisteredApi(config);

// dbNewlyCctldJson({ date?, tlds? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
//   tlds (string, optional)
async function main(): Promise<void> {
  const domains = await api.dbNewlyCctldJson({ date: new Date("2026-10-01") });
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
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
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

	result, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyCctldJson(ctx).
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

## Newly Registered With DNS

`GET https://files.whoisfreaks.com/v3.1/download/domainer/newly/dns`

Newly Registered With DNS. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string (date) |  | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Newly Registered With DNS: GET https://files.whoisfreaks.com/v3.1/download/domainer/newly/dns

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DbNewlyDns.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesNewlyRegisteredApi(client)

    # db_newly_dns parameters:
    #   var_date (datetime.date, optional, keyword): yyyy-MM-dd; omit for latest
    data = api.db_newly_dns(var_date=date(2026, 10, 1))  # the file's raw bytes
    path = "DbNewlyDns.json"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Newly Registered With DNS: GET https://files.whoisfreaks.com/v3.1/download/domainer/newly/dns
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbNewlyDns.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesNewlyRegisteredApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesNewlyRegisteredApi(config);

// dbNewlyDns({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbNewlyDns({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbNewlyDns.json";
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
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
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

	file, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyDns(ctx).Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbNewlyDns.json")
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
