# Databases - Streaming

*Section: Databases*

Stream database files and threat feeds as plain CSV text instead of downloading a gzip file

28 endpoints. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Stream the daily phishing threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/phishing`

Streams the daily phishing threat feed for a given date. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream the daily phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/phishing

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamThreatFeedPhishing.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_threat_feed_phishing parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_threat_feed_phishing(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream the daily phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/phishing
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamThreatFeedPhishing.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamThreatFeedPhishing({ date, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamThreatFeedPhishing({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream the daily phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamThreatFeedPhishing (GET /v3.4/stream/threat-feed/phishing):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamThreatFeedPhishing(ctx).
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

## Stream a sample of the phishing threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/phishing/sample`

Public endpoint: no API key required.

Streams a fixed sample of the phishing threat feed. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of the phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/phishing/sample

Run it (public endpoint, no API key needed):
    python StreamThreatFeedPhishingSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_threat_feed_phishing_sample parameters:
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_threat_feed_phishing_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of the phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/phishing/sample
// Run (public endpoint, no API key needed): npx tsx StreamThreatFeedPhishingSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamThreatFeedPhishingSample({ offset?, limit? })
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamThreatFeedPhishingSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of the phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing/sample)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamThreatFeedPhishingSample (GET /v3.4/stream/threat-feed/phishing/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamThreatFeedPhishingSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Stream the daily malware threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/malware`

Streams the daily malware threat feed for a given date. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream the daily malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/malware

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamThreatFeedMalware.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_threat_feed_malware parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_threat_feed_malware(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream the daily malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/malware
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamThreatFeedMalware.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamThreatFeedMalware({ date, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamThreatFeedMalware({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream the daily malware threat feed (CSV) (GET /v3.4/stream/threat-feed/malware)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamThreatFeedMalware (GET /v3.4/stream/threat-feed/malware):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamThreatFeedMalware(ctx).
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

## Stream a sample of the malware threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/malware/sample`

Public endpoint: no API key required.

Streams a fixed sample of the malware threat feed. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of the malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/malware/sample

Run it (public endpoint, no API key needed):
    python StreamThreatFeedMalwareSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_threat_feed_malware_sample parameters:
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_threat_feed_malware_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of the malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/malware/sample
// Run (public endpoint, no API key needed): npx tsx StreamThreatFeedMalwareSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamThreatFeedMalwareSample({ offset?, limit? })
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamThreatFeedMalwareSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of the malware threat feed (CSV) (GET /v3.4/stream/threat-feed/malware/sample)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamThreatFeedMalwareSample (GET /v3.4/stream/threat-feed/malware/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamThreatFeedMalwareSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Stream the daily spam threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/spam`

Streams the daily spam threat feed for a given date. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream the daily spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/spam

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamThreatFeedSpam.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_threat_feed_spam parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_threat_feed_spam(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream the daily spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/spam
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamThreatFeedSpam.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamThreatFeedSpam({ date, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamThreatFeedSpam({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream the daily spam threat feed (CSV) (GET /v3.4/stream/threat-feed/spam)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamThreatFeedSpam (GET /v3.4/stream/threat-feed/spam):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamThreatFeedSpam(ctx).
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

## Stream a sample of the spam threat feed (CSV)

`GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/spam/sample`

Public endpoint: no API key required.

Streams a fixed sample of the spam threat feed. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of the spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/spam/sample

Run it (public endpoint, no API key needed):
    python StreamThreatFeedSpamSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_threat_feed_spam_sample parameters:
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_threat_feed_spam_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of the spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/spam/sample
// Run (public endpoint, no API key needed): npx tsx StreamThreatFeedSpamSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamThreatFeedSpamSample({ offset?, limit? })
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamThreatFeedSpamSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of the spam threat feed (CSV) (GET /v3.4/stream/threat-feed/spam/sample)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamThreatFeedSpamSample (GET /v3.4/stream/threat-feed/spam/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamThreatFeedSpamSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Stream newly registered gTLD domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld`

Streams the daily file of newly registered gTLD domains for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream newly registered gTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerGtld.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_gtld parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_gtld(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream newly registered gTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerGtld.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerGtld({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerGtld({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/gtld)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerGtld (GET /v3.3/stream/domainer/gtld):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerGtld(ctx).
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

## Stream cleaned newly registered gTLD domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld/cleaned`

Streams the daily file of cleaned newly registered gTLD domains for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream cleaned newly registered gTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld/cleaned

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerGtldCleaned.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_gtld_cleaned parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_gtld_cleaned(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream cleaned newly registered gTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld/cleaned
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerGtldCleaned.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerGtldCleaned({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerGtldCleaned({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream cleaned newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/gtld/cleaned)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerGtldCleaned (GET /v3.3/stream/domainer/gtld/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerGtldCleaned(ctx).
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

## Stream cleaned newly registered gTLD domains with an email (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld/cleaned/email`

Streams the daily file of cleaned newly registered gTLD domains with an email for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream cleaned newly registered gTLD domains with an email (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld/cleaned/email

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerGtldCleanedEmail.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_gtld_cleaned_email parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_gtld_cleaned_email(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream cleaned newly registered gTLD domains with an email (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld/cleaned/email
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerGtldCleanedEmail.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerGtldCleanedEmail({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerGtldCleanedEmail({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream cleaned newly registered gTLD domains with an email (CSV) (GET /v3.3/stream/domainer/gtld/cleaned/email)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerGtldCleanedEmail (GET /v3.3/stream/domainer/gtld/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerGtldCleanedEmail(ctx).
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

## Stream cleaned newly registered gTLD domains with a phone (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld/cleaned/phone`

Streams the daily file of cleaned newly registered gTLD domains with a phone for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream cleaned newly registered gTLD domains with a phone (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld/cleaned/phone

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerGtldCleanedPhone.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_gtld_cleaned_phone parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_gtld_cleaned_phone(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream cleaned newly registered gTLD domains with a phone (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld/cleaned/phone
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerGtldCleanedPhone.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerGtldCleanedPhone({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerGtldCleanedPhone({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream cleaned newly registered gTLD domains with a phone (CSV) (GET /v3.3/stream/domainer/gtld/cleaned/phone)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerGtldCleanedPhone (GET /v3.3/stream/domainer/gtld/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerGtldCleanedPhone(ctx).
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

## Stream newly registered ccTLD domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld`

Streams the daily file of newly registered ccTLD domains for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream newly registered ccTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerCctld.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_cctld parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_cctld(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream newly registered ccTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerCctld.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerCctld({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerCctld({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/cctld)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerCctld (GET /v3.3/stream/domainer/cctld):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerCctld(ctx).
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

## Stream cleaned newly registered ccTLD domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld/cleaned`

Streams the daily file of cleaned newly registered ccTLD domains for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream cleaned newly registered ccTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld/cleaned

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerCctldCleaned.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_cctld_cleaned parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_cctld_cleaned(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream cleaned newly registered ccTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld/cleaned
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerCctldCleaned.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerCctldCleaned({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerCctldCleaned({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream cleaned newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/cctld/cleaned)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerCctldCleaned (GET /v3.3/stream/domainer/cctld/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerCctldCleaned(ctx).
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

## Stream cleaned newly registered ccTLD domains with an email (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld/cleaned/email`

Streams the daily file of cleaned newly registered ccTLD domains with an email for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream cleaned newly registered ccTLD domains with an email (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld/cleaned/email

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerCctldCleanedEmail.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_cctld_cleaned_email parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_cctld_cleaned_email(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream cleaned newly registered ccTLD domains with an email (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld/cleaned/email
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerCctldCleanedEmail.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerCctldCleanedEmail({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerCctldCleanedEmail({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream cleaned newly registered ccTLD domains with an email (CSV) (GET /v3.3/stream/domainer/cctld/cleaned/email)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerCctldCleanedEmail (GET /v3.3/stream/domainer/cctld/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerCctldCleanedEmail(ctx).
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

## Stream cleaned newly registered ccTLD domains with a phone (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld/cleaned/phone`

Streams the daily file of cleaned newly registered ccTLD domains with a phone for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream cleaned newly registered ccTLD domains with a phone (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld/cleaned/phone

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerCctldCleanedPhone.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_cctld_cleaned_phone parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_cctld_cleaned_phone(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream cleaned newly registered ccTLD domains with a phone (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld/cleaned/phone
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerCctldCleanedPhone.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerCctldCleanedPhone({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerCctldCleanedPhone({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream cleaned newly registered ccTLD domains with a phone (CSV) (GET /v3.3/stream/domainer/cctld/cleaned/phone)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerCctldCleanedPhone (GET /v3.3/stream/domainer/cctld/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerCctldCleanedPhone(ctx).
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

## Stream expiring domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired`

Streams the daily file of expiring domains for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerExpired.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_expired parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_expired(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerExpired.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerExpired({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerExpired({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream expiring domains (CSV) (GET /v3.3/stream/domainer/expired)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerExpired (GET /v3.3/stream/domainer/expired):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerExpired(ctx).
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

## Stream cleaned expiring domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired/cleaned`

Streams the daily file of cleaned expiring domains for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream cleaned expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired/cleaned

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerExpiredCleaned.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_expired_cleaned parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_expired_cleaned(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream cleaned expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired/cleaned
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerExpiredCleaned.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerExpiredCleaned({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerExpiredCleaned({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream cleaned expiring domains (CSV) (GET /v3.3/stream/domainer/expired/cleaned)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerExpiredCleaned (GET /v3.3/stream/domainer/expired/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerExpiredCleaned(ctx).
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

## Stream cleaned expiring domains with an email (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired/cleaned/email`

Streams the daily file of cleaned expiring domains with an email for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream cleaned expiring domains with an email (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired/cleaned/email

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerExpiredCleanedEmail.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_expired_cleaned_email parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_expired_cleaned_email(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream cleaned expiring domains with an email (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired/cleaned/email
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerExpiredCleanedEmail.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerExpiredCleanedEmail({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerExpiredCleanedEmail({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream cleaned expiring domains with an email (CSV) (GET /v3.3/stream/domainer/expired/cleaned/email)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerExpiredCleanedEmail (GET /v3.3/stream/domainer/expired/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerExpiredCleanedEmail(ctx).
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

## Stream cleaned expiring domains with a phone (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired/cleaned/phone`

Streams the daily file of cleaned expiring domains with a phone for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream cleaned expiring domains with a phone (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired/cleaned/phone

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerExpiredCleanedPhone.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_expired_cleaned_phone parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_expired_cleaned_phone(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream cleaned expiring domains with a phone (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/expired/cleaned/phone
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerExpiredCleanedPhone.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerExpiredCleanedPhone({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerExpiredCleanedPhone({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream cleaned expiring domains with a phone (CSV) (GET /v3.3/stream/domainer/expired/cleaned/phone)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerExpiredCleanedPhone (GET /v3.3/stream/domainer/expired/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerExpiredCleanedPhone(ctx).
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

## Stream dropped domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/dropped`

Streams the daily file of dropped domains for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream dropped domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/dropped

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerDropped.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_dropped parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_dropped(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream dropped domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/dropped
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerDropped.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerDropped({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerDropped({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream dropped domains (CSV) (GET /v3.3/stream/domainer/dropped)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerDropped (GET /v3.3/stream/domainer/dropped):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerDropped(ctx).
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

## Stream dropped domains with backlinks (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/dropped/backlinks`

Streams the daily file of dropped domains with backlinks for a given date. Pass whois=true for the full WHOIS record with a CSV header, or whois=false for domain names only. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `date` | query | yes | string (date) |  | yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints. |
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream dropped domains with backlinks (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/dropped/backlinks

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python StreamDomainerDroppedBacklinks.py
"""
import os
from datetime import date

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_dropped_backlinks parameters:
    #   var_date (datetime.date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_dropped_backlinks(date(2026, 10, 1))  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream dropped domains with backlinks (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/dropped/backlinks
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerDroppedBacklinks.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerDroppedBacklinks({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerDroppedBacklinks({ date: new Date("2026-10-01") }); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream dropped domains with backlinks (CSV) (GET /v3.3/stream/domainer/dropped/backlinks)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerDroppedBacklinks (GET /v3.3/stream/domainer/dropped/backlinks):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerDroppedBacklinks(ctx).
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

## Stream a sample of newly registered gTLD domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/gtld`

Public endpoint: no API key required.

Streams a fixed sample of newly registered gTLD domains. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of newly registered gTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/gtld

Run it (public endpoint, no API key needed):
    python StreamDomainerGtldSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_gtld_sample parameters:
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_gtld_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of newly registered gTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/gtld
// Run (public endpoint, no API key needed): npx tsx StreamDomainerGtldSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerGtldSample({ whois?, offset?, limit? })
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerGtldSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/sample/gtld)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerGtldSample (GET /v3.3/stream/domainer/sample/gtld):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerGtldSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Stream a sample of cleaned newly registered gTLD domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/gtld/cleaned`

Public endpoint: no API key required.

Streams a fixed sample of cleaned newly registered gTLD domains. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of cleaned newly registered gTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/gtld/cleaned

Run it (public endpoint, no API key needed):
    python StreamDomainerGtldCleanedSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_gtld_cleaned_sample parameters:
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_gtld_cleaned_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of cleaned newly registered gTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/gtld/cleaned
// Run (public endpoint, no API key needed): npx tsx StreamDomainerGtldCleanedSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerGtldCleanedSample({ whois?, offset?, limit? })
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerGtldCleanedSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of cleaned newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/sample/gtld/cleaned)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerGtldCleanedSample (GET /v3.3/stream/domainer/sample/gtld/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerGtldCleanedSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Stream a sample of newly registered ccTLD domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/cctld`

Public endpoint: no API key required.

Streams a fixed sample of newly registered ccTLD domains. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of newly registered ccTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/cctld

Run it (public endpoint, no API key needed):
    python StreamDomainerCctldSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_cctld_sample parameters:
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_cctld_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of newly registered ccTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/cctld
// Run (public endpoint, no API key needed): npx tsx StreamDomainerCctldSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerCctldSample({ whois?, offset?, limit? })
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerCctldSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/sample/cctld)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerCctldSample (GET /v3.3/stream/domainer/sample/cctld):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerCctldSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Stream a sample of cleaned newly registered ccTLD domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/cctld/cleaned`

Public endpoint: no API key required.

Streams a fixed sample of cleaned newly registered ccTLD domains. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of cleaned newly registered ccTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/cctld/cleaned

Run it (public endpoint, no API key needed):
    python StreamDomainerCctldCleanedSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_cctld_cleaned_sample parameters:
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_cctld_cleaned_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of cleaned newly registered ccTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/cctld/cleaned
// Run (public endpoint, no API key needed): npx tsx StreamDomainerCctldCleanedSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerCctldCleanedSample({ whois?, offset?, limit? })
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerCctldCleanedSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of cleaned newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/sample/cctld/cleaned)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerCctldCleanedSample (GET /v3.3/stream/domainer/sample/cctld/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerCctldCleanedSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Stream a sample of expiring domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/expired`

Public endpoint: no API key required.

Streams a fixed sample of expiring domains. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/expired

Run it (public endpoint, no API key needed):
    python StreamDomainerExpiredSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_expired_sample parameters:
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_expired_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/expired
// Run (public endpoint, no API key needed): npx tsx StreamDomainerExpiredSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerExpiredSample({ whois?, offset?, limit? })
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerExpiredSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of expiring domains (CSV) (GET /v3.3/stream/domainer/sample/expired)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerExpiredSample (GET /v3.3/stream/domainer/sample/expired):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerExpiredSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Stream a sample of cleaned expiring domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/expired/cleaned`

Public endpoint: no API key required.

Streams a fixed sample of cleaned expiring domains. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of cleaned expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/expired/cleaned

Run it (public endpoint, no API key needed):
    python StreamDomainerExpiredCleanedSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_expired_cleaned_sample parameters:
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_expired_cleaned_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of cleaned expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/expired/cleaned
// Run (public endpoint, no API key needed): npx tsx StreamDomainerExpiredCleanedSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerExpiredCleanedSample({ whois?, offset?, limit? })
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerExpiredCleanedSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of cleaned expiring domains (CSV) (GET /v3.3/stream/domainer/sample/expired/cleaned)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerExpiredCleanedSample (GET /v3.3/stream/domainer/sample/expired/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerExpiredCleanedSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Stream a sample of dropped domains (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/dropped`

Public endpoint: no API key required.

Streams a fixed sample of dropped domains. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of dropped domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/dropped

Run it (public endpoint, no API key needed):
    python StreamDomainerDroppedSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_dropped_sample parameters:
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_dropped_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of dropped domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/dropped
// Run (public endpoint, no API key needed): npx tsx StreamDomainerDroppedSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerDroppedSample({ whois?, offset?, limit? })
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerDroppedSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of dropped domains (CSV) (GET /v3.3/stream/domainer/sample/dropped)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerDroppedSample (GET /v3.3/stream/domainer/sample/dropped):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerDroppedSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---

## Stream a sample of dropped domains with backlinks (CSV)

`GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/dropped/backlinks`

Public endpoint: no API key required.

Streams a fixed sample of dropped domains with backlinks. No API key and no date are needed, so it is the quickest way to check the schema. Rows are streamed as plain uncompressed CSV text, so a parser can start on the first row while the rest is still arriving. Use offset and limit to walk the file in pages.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `whois` | query | no | boolean | `false` | true streams the full WHOIS record per domain with a CSV header row; false streams only the domain names, one per line and with no header. The cleaned file types exist only in the WHOIS form, so pass true for those. |
| `offset` | query | no | integer (int64) |  | Data rows to skip from the start of the file. The header row is never counted. Rows are skipped by reading forward, so a large offset costs more than a small one. |
| `limit` | query | no | integer (int64) |  | Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on its own. |

**Usage**

<details><summary>Python</summary>

```python
"""Stream a sample of dropped domains with backlinks (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/dropped/backlinks

Run it (public endpoint, no API key needed):
    python StreamDomainerDroppedBacklinksSample.py
"""

import whoisfreaks

config = whoisfreaks.Configuration()
# Public endpoint: no API key needed.

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DatabasesStreamingApi(client)

    # stream_domainer_dropped_backlinks_sample parameters:
    #   whois (bool, optional, keyword): true streams the full WHOIS record per domain with a CSV header row; false st...; default False
    #   offset (int, optional, keyword): Data rows to skip from the start of the file. The header row is never counted...
    #   limit (int, optional, keyword): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
    csv_text = api.stream_domainer_dropped_backlinks_sample()  # plain CSV text, already decompressed
    print(csv_text)
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Stream a sample of dropped domains with backlinks (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/dropped/backlinks
// Run (public endpoint, no API key needed): npx tsx StreamDomainerDroppedBacklinksSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerDroppedBacklinksSample({ whois?, offset?, limit? })
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerDroppedBacklinksSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
// Runnable example: Stream a sample of dropped domains with backlinks (CSV) (GET /v3.3/stream/domainer/sample/dropped/backlinks)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamDomainerDroppedBacklinksSample (GET /v3.3/stream/domainer/sample/dropped/backlinks):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

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

	result, _, err := client.DatabasesStreamingAPI.StreamDomainerDroppedBacklinksSample(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
