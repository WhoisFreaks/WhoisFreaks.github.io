# Authentication

Every WhoisFreaks API request needs an **API key**, passed as the `apiKey`
query parameter. The one exception is the public database file status check
(`GET /v3.4/status`). Each SDK exposes a configuration hook so you set the key
once and it is attached to every request automatically.

## Get an API key

New to WhoisFreaks? Follow the step-by-step guide, [Getting Started with WhoisFreaks: How to Sign Up and Get Your API Key](https://whoisfreaks.com/resources/tutorial/getting-started-with-whoisfreaks-how-to-sign-up-and-get-your-api-key), which walks through account creation and locating your key.

In short:

1. Sign in at <https://billing.whoisfreaks.com>.
2. Copy your API key from the dashboard.
3. Keep it secret. Do **not** commit it to source control; the examples read it
   from the `WHOISFREAKS_API_KEY` environment variable.

## Base URLs

| Purpose | Base URL |
|---------|----------|
| Live lookups, bulk lookups and account | `https://api.whoisfreaks.com` |
| Database downloads, threat feeds and database file status | `https://files.whoisfreaks.com` |

The SDKs pick the right host for each endpoint; every endpoint page shows its full URL.

## Setting the key per language

### Python

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

### JavaScript

```javascript
// Live WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/whois/live
// Run: WHOISFREAKS_API_KEY=your_api_key node WhoisLive.js
const { ApiClient, WHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new WHOISApi(client);

// whoisLive(domainName, opts)
//   domainName (string, required)
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.whoisLive("whoisfreaks.com");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### TypeScript

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

### Java

```java
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=WhoisLive
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.WhoisResponse;

public class WhoisLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        WhoisApi api = new WhoisApi(client);

        // whoisLive(domainName, format); null leaves an optional parameter unset
        WhoisResponse result = api.whoisLive("whoisfreaks.com", null);
        System.out.println(result);
    }
}

```

### Kotlin

```kotlin
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Run it from the Getting Started project: gradle run -PmainClass=WhoisLiveKt
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = WHOISApi()

    val result = api.whoisLive("whoisfreaks.com")
    println(result)
}

```

### C# / .NET

```csharp
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new WHOISApi(config);

WhoisResponse result = api.WhoisLive("whoisfreaks.com");
Console.WriteLine(result.ToJson());

```

### Ruby

```ruby
# Live WHOIS Lookup
#
# Parameters for whoisLive (GET /v2.0/whois/live):
#   - domain_name (string, required)
#   - format (string (one of: json, xml), optional)

require "json"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::WHOISApi.new

begin
  result = api.whois_live("whoisfreaks.com")
  puts JSON.pretty_generate(result.to_hash)
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end

```

### Go

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

### Swift

```swift
// Live WHOIS Lookup
//
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await WHOISAPI.whoisLive(domainName: "whoisfreaks.com")
    print(String(decoding: try CodableHelper.jsonEncoder.encode(result), as: UTF8.self))
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

### PHP

```php
<?php
// Live WHOIS Lookup
//
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\WHOISApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new WHOISApi(new Client(), $config);

try {
    $result = $api->whoisLive('whoisfreaks.com');
    echo $result, PHP_EOL;  // models print as JSON
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}

```
