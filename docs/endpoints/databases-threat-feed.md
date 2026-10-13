# Databases - Threat Feed

*Section: Databases*

Daily phishing, malware and spam threat feeds

6 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Download the daily phishing threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing`

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string |  | Feed date (yyyy-MM-dd); omit for the full dump of the feed |

**Usage**

<details><summary>Python</summary>

```python
"""Download the daily phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedPhishing.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_phishing parameters:
    #   var_date (str, optional, keyword): Feed date (yyyy-MM-dd); omit for the full dump of the feed
    data = api.download_threat_feed_phishing(var_date="2026-10-01")  # the file's raw bytes
    path = "DownloadThreatFeedPhishing.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Download the daily phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DownloadThreatFeedPhishing.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesThreatFeedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesThreatFeedApi(config);

// downloadThreatFeedPhishing({ date? })
//   date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
async function main(): Promise<void> {
  const blob = await api.downloadThreatFeedPhishing({ date: "2026-10-01" }); // a Blob with the file's bytes
  const file = "DownloadThreatFeedPhishing.csv";
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
// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed

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

	file, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedPhishing(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DownloadThreatFeedPhishing.csv")
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

## Download a sample of the phishing threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing/sample`

**Parameters**

None. The API key is set once on the client.

**Usage**

<details><summary>Python</summary>

```python
"""Download a sample of the phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing/sample

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedPhishingSample.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_phishing_sample takes no parameters.
    data = api.download_threat_feed_phishing_sample()  # the file's raw bytes
    path = "DownloadThreatFeedPhishingSample.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Download a sample of the phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing/sample
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DownloadThreatFeedPhishingSample.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesThreatFeedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesThreatFeedApi(config);

// downloadThreatFeedPhishingSample() takes no parameters.
async function main(): Promise<void> {
  const blob = await api.downloadThreatFeedPhishingSample(); // a Blob with the file's bytes
  const file = "DownloadThreatFeedPhishingSample.csv";
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
// Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)

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

	file, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedPhishingSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DownloadThreatFeedPhishingSample.csv")
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

## Download the daily malware threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/download/threat-feed/malware`

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string |  | Feed date (yyyy-MM-dd); omit for the full dump of the feed |

**Usage**

<details><summary>Python</summary>

```python
"""Download the daily malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/malware

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedMalware.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_malware parameters:
    #   var_date (str, optional, keyword): Feed date (yyyy-MM-dd); omit for the full dump of the feed
    data = api.download_threat_feed_malware(var_date="2026-10-01")  # the file's raw bytes
    path = "DownloadThreatFeedMalware.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Download the daily malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/malware
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DownloadThreatFeedMalware.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesThreatFeedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesThreatFeedApi(config);

// downloadThreatFeedMalware({ date? })
//   date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
async function main(): Promise<void> {
  const blob = await api.downloadThreatFeedMalware({ date: "2026-10-01" }); // a Blob with the file's bytes
  const file = "DownloadThreatFeedMalware.csv";
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
// Runnable example: Download the daily malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed

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

	file, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedMalware(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DownloadThreatFeedMalware.csv")
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

## Download a sample of the malware threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/download/threat-feed/malware/sample`

**Parameters**

None. The API key is set once on the client.

**Usage**

<details><summary>Python</summary>

```python
"""Download a sample of the malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/malware/sample

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedMalwareSample.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_malware_sample takes no parameters.
    data = api.download_threat_feed_malware_sample()  # the file's raw bytes
    path = "DownloadThreatFeedMalwareSample.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Download a sample of the malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/malware/sample
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DownloadThreatFeedMalwareSample.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesThreatFeedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesThreatFeedApi(config);

// downloadThreatFeedMalwareSample() takes no parameters.
async function main(): Promise<void> {
  const blob = await api.downloadThreatFeedMalwareSample(); // a Blob with the file's bytes
  const file = "DownloadThreatFeedMalwareSample.csv";
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
// Runnable example: Download a sample of the malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware/sample)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
//   (no parameters; the API key is set on the client)

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

	file, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedMalwareSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DownloadThreatFeedMalwareSample.csv")
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

## Download the daily spam threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam`

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | no | string |  | Feed date (yyyy-MM-dd); omit for the full dump of the feed |

**Usage**

<details><summary>Python</summary>

```python
"""Download the daily spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedSpam.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_spam parameters:
    #   var_date (str, optional, keyword): Feed date (yyyy-MM-dd); omit for the full dump of the feed
    data = api.download_threat_feed_spam(var_date="2026-10-01")  # the file's raw bytes
    path = "DownloadThreatFeedSpam.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Download the daily spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DownloadThreatFeedSpam.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesThreatFeedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesThreatFeedApi(config);

// downloadThreatFeedSpam({ date? })
//   date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
async function main(): Promise<void> {
  const blob = await api.downloadThreatFeedSpam({ date: "2026-10-01" }); // a Blob with the file's bytes
  const file = "DownloadThreatFeedSpam.csv";
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
// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed

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

	file, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedSpam(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DownloadThreatFeedSpam.csv")
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

## Download a sample of the spam threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam/sample`

**Parameters**

None. The API key is set once on the client.

**Usage**

<details><summary>Python</summary>

```python
"""Download a sample of the spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam/sample

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DownloadThreatFeedSpamSample.py
"""
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesThreatFeedApi(client)

    # download_threat_feed_spam_sample takes no parameters.
    data = api.download_threat_feed_spam_sample()  # the file's raw bytes
    path = "DownloadThreatFeedSpamSample.csv"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Saved {len(data)} bytes to {os.path.abspath(path)}")
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Download a sample of the spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam/sample
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DownloadThreatFeedSpamSample.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesThreatFeedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesThreatFeedApi(config);

// downloadThreatFeedSpamSample() takes no parameters.
async function main(): Promise<void> {
  const blob = await api.downloadThreatFeedSpamSample(); // a Blob with the file's bytes
  const file = "DownloadThreatFeedSpamSample.csv";
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
// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)

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

	file, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedSpamSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DownloadThreatFeedSpamSample.csv")
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
