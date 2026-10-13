# Domain Reputation

*Section: API Solutions*

Real-time domain threat assessment and trust scoring

1 endpoint. Requests need your API key unless noted otherwise. See [Authentication](../authentication.md).

## Domain Reputation Lookup

`GET https://api.whoisfreaks.com/v1/domain/security`

Real-time domain threat assessment. Returns risk verdict, trust score, DGA analysis, threat intelligence matches, and security signals. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Default | Description |
|-----------|----|----------|------|---------|-------------|
| `domainName` | query | yes | string |  | The domain name to assess |
| `format` | query | no | string | `json` |  (one of: json, xml) |

**Response** (`DomainReputationResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `input` | DomainReputationInput |  |
| `assessed_at` | string |  |
| `version` | string |  |
| `processing_time_ms` | integer |  |
| `risk_category` | RiskCategory |  |
| `dga_score` | DgaScore |  |
| `trust_signals` | TrustSignals |  |
| `intelligence` | ReputationIntelligence |  |
| `evidence_summary` | EvidenceSummary |  |
| `errors` | array<string> |  |

<details><summary><code>DomainReputationInput</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domain` | string |  |

</details>

<details><summary><code>RiskCategory</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `verdict` | string |  |
| `confidence` | number |  |
| `primary_threat` | string |  |
| `severity` | string |  |
| `threat_types` | array<string> |  |
| `sources` | array<ThreatSource> |  |
| `pivot_matches` | array<PivotMatch> |  |

</details>

<details><summary><code>DgaScore</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `score` | number |  |
| `is_dga` | boolean |  |
| `model` | string |  |
| `features` | DgaFeatures |  |
| `interpretation` | string |  |

</details>

<details><summary><code>TrustSignals</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `trust_score` | integer |  |
| `trust_band` | string |  |
| `signals` | ReputationSignals |  |
| `indicators` | ReputationIndicators |  |

</details>

<details><summary><code>ReputationIntelligence</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `ioc_type` | string |  |
| `ioc_value` | string |  |
| `related_iocs` | array<RelatedIoc> |  |
| `feed_tags` | array<string> |  |
| `stix_pattern` | string |  |
| `recommended_action` | string |  |
| `first_seen` | string |  |
| `last_seen` | string |  |

</details>

<details><summary><code>EvidenceSummary</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `why_flagged` | array<string> |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Domain Reputation Lookup: GET https://api.whoisfreaks.com/v1/domain/security

Run it with your API key in the environment:
    WHOISFREAKS_API_KEY=your_api_key python DomainReputation.py
"""
import json
import os

import whoisfreaks

config = whoisfreaks.Configuration()
config.api_key["ApiKeyAuth"] = os.environ["WHOISFREAKS_API_KEY"]  # set once for every request

with whoisfreaks.ApiClient(config) as client:
    api = whoisfreaks.DomainReputationApi(client)

    # domain_reputation parameters:
    #   domain_name (str, required): The domain name to assess
    #   format (str, optional, keyword): one of json, xml; default "json"
    result = api.domain_reputation("amazon.com")
    print(json.dumps(result.to_dict(), indent=2))
```

</details>

<details><summary>TypeScript</summary>

```typescript
// Domain Reputation Lookup: GET https://api.whoisfreaks.com/v1/domain/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DomainReputation.ts
import { Configuration, DomainReputationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DomainReputationApi(config);

// domainReputation({ domainName, format? })
//   domainName (string, required): The domain name to assess
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.domainReputation({ domainName: "amazon.com" });
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
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
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

	result, _, err := client.DomainReputationAPI.DomainReputation(ctx).
		DomainName("amazon.com").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}

```

</details>

---
