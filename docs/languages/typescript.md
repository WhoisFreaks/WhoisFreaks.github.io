# TypeScript SDK

## About

The official **WhoisFreaks TypeScript SDK**: a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from TypeScript with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to npm.

**Keywords:** typescript whois api, typescript whois sdk, whoisfreaks typescript, typescript domain lookup, typescript dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** npm
- **Package:** `whoisfreaks`

## Install

```bash
npm install whoisfreaks
```

## Build from Source

Prefer to build the SDK yourself instead of installing from npm? Clone the TypeScript SDK repository and build it locally:

```bash
git clone https://github.com/WhoisFreaks/whoisfreaks-typescript
cd whoisfreaks-typescript
npm install
npm run build
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

1. Create a project and install the SDK (Node.js 18 or later), plus [tsx](https://tsx.is) to run TypeScript files directly:

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
npm init -y
npm install whoisfreaks
npm install -D tsx @types/node
```

2. Create `main.ts`:

```typescript
import { Configuration, WHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new WHOISApi(config);

async function main(): Promise<void> {
  const record = await api.whoisLive({ domainName: "whoisfreaks.com" });
  console.log("Domain: ", record.domain_name);
  console.log("Created:", record.create_date);
  console.log("Expires:", record.expiry_date);
}

main().catch(async (err: unknown) => {
  if (err instanceof ResponseError) {
    console.error(`HTTP ${err.response.status}: ${await err.response.text()}`);
  } else {
    console.error(err);
  }
  process.exitCode = 1;
});
```

3. Set your API key and run it:

```bash
export WHOISFREAKS_API_KEY="your_api_key"   # PowerShell: $env:WHOISFREAKS_API_KEY="your_api_key"
npx tsx main.ts
```

`tsx` runs the file without a separate compile step. To type-check as well, add the compiler and run it in strict mode:

```bash
npm install -D typescript
npx tsc --noEmit --strict --module nodenext --types node main.ts
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

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

## Endpoints

All 60 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

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

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```typescript
// Bulk WHOIS Lookup: POST https://api.whoisfreaks.com/v2.0/bulkwhois/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkWhois.ts
import { Configuration, WHOISApi, ResponseError, type BulkWhoisRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new WHOISApi(config);

// bulkWhois({ bulkWhoisRequest, format? })
//   bulkWhoisRequest (BulkWhoisRequest, required): request body
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const body: BulkWhoisRequest = { domainNames: ["whoisfreaks.com", "jfreaks.com"] };
  const result = await api.bulkWhois({ bulkWhoisRequest: body });
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

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```typescript
// Historical WHOIS records for a domain: GET https://api.whoisfreaks.com/v2.0/whois/history
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx WhoisHistory.ts
import { Configuration, WHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new WHOISApi(config);

// whoisHistory({ domainName, format? })
//   domainName (string, required): Domain to fetch historical WHOIS records for
//   format ("json" | "xml", optional)
async function main(): Promise<void> {
  const result = await api.whoisHistory({ domainName: "whoisfreaks.com" });
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

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```typescript
// Reverse WHOIS lookup by keyword: GET https://api.whoisfreaks.com/v2.0/whois/reverse
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx WhoisReverse.ts
import { Configuration, WHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new WHOISApi(config);

// whoisReverse({ keyword, page?, format? })
//   keyword (string, required): Keyword to search across WHOIS records
//   page (number, optional): Page number
//   format ("json" | "xml", optional)
async function main(): Promise<void> {
  const result = await api.whoisReverse({ keyword: "whoisfreaks", page: 1 });
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

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```typescript
// Live DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsLive.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsLive({ type, domainName?, ipAddress?, format? })
//   type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME; default "all"
//   domainName (string, optional)
//   ipAddress (string, optional): Use for PTR lookups
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.dnsLive({ type: "A,MX,TXT", domainName: "whoisfreaks.com" });
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

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```typescript
// Historical DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/historical
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsHistorical.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsHistorical({ domainName, type, page?, format? })
//   domainName (string, required)
//   type (string, required): default "all"
//   page (number, optional): default 1
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.dnsHistorical({ domainName: "whoisfreaks.com", type: "A,MX,TXT", page: 1 });
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

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```typescript
// Reverse DNS Lookup: GET https://api.whoisfreaks.com/v2.1/dns/reverse
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsReverse.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsReverse({ value, type, exact?, page?, format? })
//   value (string, required): IP, CIDR, or record value
//   type ("a" | "mx" | "cname" | "ns" | "aaaa" | "txt" | "soa", required)
//   exact (boolean, optional): default true
//   page (number, optional): default 1
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.dnsReverse({ value: "8.8.8.8", type: "a", page: 1 });
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

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```typescript
// Bulk DNS Lookup: POST https://api.whoisfreaks.com/v2.0/dns/bulk/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsBulk.ts
import { Configuration, DNSApi, ResponseError, type DnsBulkRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsBulk({ type, dnsBulkRequest, format? })
//   type (string, required): default "all"
//   dnsBulkRequest (DnsBulkRequest, required): request body
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const body: DnsBulkRequest = { domainNames: ["whoisfreaks.com", "example.com"] };
  const result = await api.dnsBulk({ type: "A,MX,TXT", dnsBulkRequest: body });
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

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```typescript
// Domain Availability Check with Suggestions: GET https://api.whoisfreaks.com/v2.0/domain/availability
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DomainAvailabilityV2.ts
import { Configuration, DomainAvailabilityApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DomainAvailabilityApi(config);

// domainAvailabilityV2({ domain, sug?, count?, format? })
//   domain (string, required): The domain name to check
//   sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain; default false
//   count (number, optional): Number of TLD suggestions to return when sug=true. Maximum is 100; default 5
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.domainAvailabilityV2({ domain: "google.com", sug: true, count: 5 });
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

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```typescript
// Bulk Domain Availability Check: POST https://api.whoisfreaks.com/v2.0/domain/availability
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkDomainAvailabilityV2.ts
import { Configuration, DomainAvailabilityApi, ResponseError, type BulkDomainAvailabilityRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DomainAvailabilityApi(config);

// bulkDomainAvailabilityV2({ bulkDomainAvailabilityRequest, domain?, format? })
//   bulkDomainAvailabilityRequest (BulkDomainAvailabilityRequest, required): request body
//   domain (string, optional): Required for TLD-mode bulk check (base domain)
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const body: BulkDomainAvailabilityRequest = { domainNames: ["whoisfreaks.com", "example.com"] };
  const result = await api.bulkDomainAvailabilityV2({ bulkDomainAvailabilityRequest: body });
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

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```typescript
// Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/domain/typos
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx Typosquatting.ts
import { Configuration, TyposquattingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new TyposquattingApi(config);

// typosquatting({ keyword?, pattern?, pageToken? })
//   keyword (string, optional)
//   pattern (string, optional)
//   pageToken (string, optional)
async function main(): Promise<void> {
  const result = await api.typosquatting({ keyword: "whoisfreaks" });
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

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```typescript
// SSL Certificate Lookup: GET https://api.whoisfreaks.com/v1.0/ssl/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx SslLookup.ts
import { Configuration, SSLApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new SSLApi(config);

// sslLookup({ domainName, chain?, sslRaw?, format? })
//   domainName (string, required)
//   chain (boolean, optional): default false
//   sslRaw (boolean, optional): default false
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.sslLookup({ domainName: "whoisfreaks.com" });
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

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```typescript
// IP Geolocation Lookup: GET https://api.whoisfreaks.com/v1.0/geolocation
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx Geolocation.ts
import { Configuration, GeolocationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new GeolocationApi(config);

// geolocation({ ip })
//   ip (string, required)
async function main(): Promise<void> {
  const result = await api.geolocation({ ip: "8.8.8.8" });
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

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```typescript
// Bulk IP Geolocation: POST https://api.whoisfreaks.com/v1.0/geolocation
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkGeolocation.ts
import { Configuration, GeolocationApi, ResponseError, type BulkGeolocationRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new GeolocationApi(config);

// bulkGeolocation({ bulkGeolocationRequest })
//   bulkGeolocationRequest (BulkGeolocationRequest, required): request body
async function main(): Promise<void> {
  const body: BulkGeolocationRequest = { ips: ["8.8.8.8", "1.1.1.1"] };
  const results = await api.bulkGeolocation({ bulkGeolocationRequest: body });
  console.log(JSON.stringify(results, null, 2));
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

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```typescript
// Subdomains Lookup: GET https://api.whoisfreaks.com/v1.0/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx Subdomains.ts
import { Configuration, SubdomainsApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new SubdomainsApi(config);

// subdomains({ domain, after?, before?, status?, page?, format? })
//   domain (string, required)
//   after (Date, optional)
//   before (Date, optional)
//   status ("active" | "inactive", optional)
//   page (number, optional): default 1
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.subdomains({ domain: "whoisfreaks.com", page: 1 });
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

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```typescript
// IP Reputation Lookup: GET https://api.whoisfreaks.com/v1.0/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx IpReputation.ts
import { Configuration, IPReputationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new IPReputationApi(config);

// ipReputation({ ip })
//   ip (string, required)
async function main(): Promise<void> {
  const result = await api.ipReputation({ ip: "8.8.8.8" });
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

#### Bulk IP Reputation

`POST /v1.0/security`

```typescript
// Bulk IP Reputation: POST https://api.whoisfreaks.com/v1.0/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkIpReputation.ts
import { Configuration, IPReputationApi, ResponseError, type BulkGeolocationRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new IPReputationApi(config);

// bulkIpReputation({ bulkGeolocationRequest })
//   bulkGeolocationRequest (BulkGeolocationRequest, required): request body
async function main(): Promise<void> {
  const body: BulkGeolocationRequest = { ips: ["8.8.8.8", "1.1.1.1"] };
  const results = await api.bulkIpReputation({ bulkGeolocationRequest: body });
  console.log(JSON.stringify(results, null, 2));
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

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

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

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```typescript
// ASN WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/asn-whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx AsnWhois.ts
import { Configuration, ASNWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new ASNWHOISApi(config);

// asnWhois({ asn, format? })
//   asn (string, required)
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.asnWhois({ asn: "as15169" });
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

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```typescript
// IP WHOIS Lookup: GET https://api.whoisfreaks.com/v1.0/ip-whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx IpWhois.ts
import { Configuration, IPWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new IPWHOISApi(config);

// ipWhois({ ip, format? })
//   ip (string, required)
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.ipWhois({ ip: "8.8.8.8" });
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

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```typescript
// Rotate API Key: GET https://api.whoisfreaks.com/v1.0/api-key/rotate
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx RotateApiKey.ts
import { Configuration, AccountApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new AccountApi(config);

// rotateApiKey() takes no parameters.
async function main(): Promise<void> {
  const newKey = await api.rotateApiKey(); // use this key from now on
  console.log("New API key:", newKey);
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

#### Account Usage

`GET /v1.0/whoisapi/usage`

```typescript
// Account Usage: GET https://api.whoisfreaks.com/v1.0/whoisapi/usage
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx AccountUsage.ts
import { Configuration, AccountApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new AccountApi(config);

// accountUsage() takes no parameters.
async function main(): Promise<void> {
  const result = await api.accountUsage();
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

#### Database File Status (Public)

`GET /v3.4/status`

```typescript
// Database File Status (Public): GET https://files.whoisfreaks.com/v3.4/status
// Run (public endpoint, no API key needed): npx tsx DatabaseFileStatus.ts
import { AccountApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new AccountApi();

// databaseFileStatus() takes no parameters.
async function main(): Promise<void> {
  const result = await api.databaseFileStatus();
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

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

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

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

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

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

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

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

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

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

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

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

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

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

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

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

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

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

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

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

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

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

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

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

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

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```typescript
// WHOIS Database Daily: GET https://files.whoisfreaks.com/v3.3/download/dbupdate/daily/domains/whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbWhoisDaily.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesWHOISApi(config);

// dbWhoisDaily({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbWhoisDaily({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbWhoisDaily.csv";
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

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```typescript
// WHOIS Database Weekly: GET https://files.whoisfreaks.com/v3.3/download/dbupdate/weekly/domains/whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbWhoisWeekly.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesWHOISApi(config);

// dbWhoisWeekly({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbWhoisWeekly({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbWhoisWeekly.csv";
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

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```typescript
// WHOIS Database Monthly: GET https://files.whoisfreaks.com/v3.3/download/dbupdate/monthly/domains/whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbWhoisMonthly.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesWHOISApi(config);

// dbWhoisMonthly({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbWhoisMonthly({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbWhoisMonthly.csv";
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

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```typescript
// DNS Database Daily: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/daily/dns
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbDnsDaily.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesDNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesDNSApi(config);

// dbDnsDaily({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbDnsDaily({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbDnsDaily.csv";
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

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```typescript
// DNS Database Weekly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/weekly/dns
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbDnsWeekly.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesDNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesDNSApi(config);

// dbDnsWeekly({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbDnsWeekly({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbDnsWeekly.csv";
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

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```typescript
// DNS Database Monthly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/monthly/dns
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbDnsMonthly.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesDNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesDNSApi(config);

// dbDnsMonthly({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbDnsMonthly({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbDnsMonthly.csv";
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

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

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

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

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

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

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

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

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

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

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

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

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

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

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

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```typescript
// ASN WHOIS Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/asn/whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbAsnWhois.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesASNWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesASNWHOISApi(config);

// dbAsnWhois({ date })
//   date (Date, required)
async function main(): Promise<void> {
  const blob = await api.dbAsnWhois({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbAsnWhois.json.gz";
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

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```typescript
// ASN WHOIS Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/asn/whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbAsnWhoisStatus.ts
import { Configuration, DatabasesASNWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesASNWHOISApi(config);

// dbAsnWhoisStatus() takes no parameters.
async function main(): Promise<void> {
  const result = await api.dbAsnWhoisStatus();
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

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

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

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

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

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

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

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

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

### Databases - Threat Feed

#### Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

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

#### Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

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

#### Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

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

#### Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

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

#### Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

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

#### Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

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
