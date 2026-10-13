# JavaScript SDK

## About

The official **WhoisFreaks JavaScript SDK**: a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from JavaScript with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to npm.

**Keywords:** javascript whois api, javascript whois sdk, whoisfreaks javascript, javascript domain lookup, javascript dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** npm
- **Package:** `whoisfreaks-js`

## Install

```bash
npm install whoisfreaks-js
```

## Build from Source

Prefer to build the SDK yourself instead of installing from npm? Clone the JavaScript SDK repository and build it locally:

```bash
git clone https://github.com/WhoisFreaks/whoisfreaks-javascript
cd whoisfreaks-javascript
npm install
npm run build
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

1. Create a project and install the SDK (Node.js 18 or later):

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
npm init -y
npm install whoisfreaks-js
```

2. Create `main.js`:

```javascript
const { ApiClient, WHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new WHOISApi(client);

async function main() {
  const record = await api.whoisLive("whoisfreaks.com");
  console.log("Domain: ", record.domain_name);
  console.log("Created:", record.create_date);
  console.log("Expires:", record.expiry_date);
}

main().catch((err) => {
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

3. Set your API key and run it:

```bash
export WHOISFREAKS_API_KEY="your_api_key"   # PowerShell: $env:WHOISFREAKS_API_KEY="your_api_key"
node main.js
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

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

## Endpoints

All 60 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

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

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```javascript
// Bulk WHOIS Lookup: POST https://api.whoisfreaks.com/v2.0/bulkwhois/live
// Run: WHOISFREAKS_API_KEY=your_api_key node BulkWhois.js
const { ApiClient, WHOISApi, BulkWhoisRequest } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new WHOISApi(client);

// bulkWhois(bulkWhoisRequest, opts)
//   bulkWhoisRequest (BulkWhoisRequest, required): request body
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const body = BulkWhoisRequest.constructFromObject({ domainNames: ["whoisfreaks.com", "jfreaks.com"] });
  const result = await api.bulkWhois(body);
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```javascript
// Historical WHOIS records for a domain: GET https://api.whoisfreaks.com/v2.0/whois/history
// Run: WHOISFREAKS_API_KEY=your_api_key node WhoisHistory.js
const { ApiClient, WHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new WHOISApi(client);

// whoisHistory(domainName, opts)
//   domainName (string, required): Domain to fetch historical WHOIS records for
//   opts.format (string, optional): one of json, xml
async function main() {
  const result = await api.whoisHistory("whoisfreaks.com");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```javascript
// Reverse WHOIS lookup by keyword: GET https://api.whoisfreaks.com/v2.0/whois/reverse
// Run: WHOISFREAKS_API_KEY=your_api_key node WhoisReverse.js
const { ApiClient, WHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new WHOISApi(client);

// whoisReverse(keyword, opts)
//   keyword (string, required): Keyword to search across WHOIS records
//   opts.page (number, optional): Page number
//   opts.format (string, optional): one of json, xml
async function main() {
  const result = await api.whoisReverse("whoisfreaks", { page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```javascript
// Live DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/live
// Run: WHOISFREAKS_API_KEY=your_api_key node DnsLive.js
const { ApiClient, DNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DNSApi(client);

// dnsLive(type, opts)
//   type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME; default "all"
//   opts.domainName (string, optional)
//   opts.ipAddress (string, optional): Use for PTR lookups
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.dnsLive("A,MX,TXT", { domainName: "whoisfreaks.com" });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```javascript
// Historical DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/historical
// Run: WHOISFREAKS_API_KEY=your_api_key node DnsHistorical.js
const { ApiClient, DNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DNSApi(client);

// dnsHistorical(domainName, type, opts)
//   domainName (string, required)
//   type (string, required): default "all"
//   opts.page (number, optional): default 1
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.dnsHistorical("whoisfreaks.com", "A,MX,TXT", { page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```javascript
// Reverse DNS Lookup: GET https://api.whoisfreaks.com/v2.1/dns/reverse
// Run: WHOISFREAKS_API_KEY=your_api_key node DnsReverse.js
const { ApiClient, DNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DNSApi(client);

// dnsReverse(value, type, opts)
//   value (string, required): IP, CIDR, or record value
//   type (string, required): one of a, mx, cname, ns, aaaa, txt, soa
//   opts.exact (boolean, optional): default true
//   opts.page (number, optional): default 1
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.dnsReverse("8.8.8.8", "a", { page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```javascript
// Bulk DNS Lookup: POST https://api.whoisfreaks.com/v2.0/dns/bulk/live
// Run: WHOISFREAKS_API_KEY=your_api_key node DnsBulk.js
const { ApiClient, DNSApi, DnsBulkRequest } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DNSApi(client);

// dnsBulk(type, dnsBulkRequest, opts)
//   type (string, required): default "all"
//   dnsBulkRequest (DnsBulkRequest, required): request body
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const body = DnsBulkRequest.constructFromObject({ domainNames: ["whoisfreaks.com", "example.com"] });
  const result = await api.dnsBulk("A,MX,TXT", body);
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```javascript
// Domain Availability Check with Suggestions: GET https://api.whoisfreaks.com/v2.0/domain/availability
// Run: WHOISFREAKS_API_KEY=your_api_key node DomainAvailabilityV2.js
const { ApiClient, DomainAvailabilityApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DomainAvailabilityApi(client);

// domainAvailabilityV2(domain, opts)
//   domain (string, required): The domain name to check
//   opts.sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain; default false
//   opts.count (number, optional): Number of TLD suggestions to return when sug=true. Maximum is 100; default 5
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.domainAvailabilityV2("google.com", { sug: true, count: 5 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```javascript
// Bulk Domain Availability Check: POST https://api.whoisfreaks.com/v2.0/domain/availability
// Run: WHOISFREAKS_API_KEY=your_api_key node BulkDomainAvailabilityV2.js
const { ApiClient, DomainAvailabilityApi, BulkDomainAvailabilityRequest } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DomainAvailabilityApi(client);

// bulkDomainAvailabilityV2(bulkDomainAvailabilityRequest, opts)
//   bulkDomainAvailabilityRequest (BulkDomainAvailabilityRequest, required): request body
//   opts.domain (string, optional): Required for TLD-mode bulk check (base domain)
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const body = BulkDomainAvailabilityRequest.constructFromObject({ domainNames: ["whoisfreaks.com", "example.com"] });
  const result = await api.bulkDomainAvailabilityV2(body);
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```javascript
// Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/domain/typos
// Run: WHOISFREAKS_API_KEY=your_api_key node Typosquatting.js
const { ApiClient, TyposquattingApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new TyposquattingApi(client);

// typosquatting(opts)
//   opts.keyword (string, optional)
//   opts.pattern (string, optional)
//   opts.pageToken (string, optional)
async function main() {
  const result = await api.typosquatting({ keyword: "whoisfreaks" });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```javascript
// SSL Certificate Lookup: GET https://api.whoisfreaks.com/v1.0/ssl/live
// Run: WHOISFREAKS_API_KEY=your_api_key node SslLookup.js
const { ApiClient, SSLApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new SSLApi(client);

// sslLookup(domainName, opts)
//   domainName (string, required)
//   opts.chain (boolean, optional): default false
//   opts.sslRaw (boolean, optional): default false
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.sslLookup("whoisfreaks.com");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```javascript
// IP Geolocation Lookup: GET https://api.whoisfreaks.com/v1.0/geolocation
// Run: WHOISFREAKS_API_KEY=your_api_key node Geolocation.js
const { ApiClient, GeolocationApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new GeolocationApi(client);

// geolocation(ip)
//   ip (string, required)
async function main() {
  const result = await api.geolocation("8.8.8.8");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```javascript
// Bulk IP Geolocation: POST https://api.whoisfreaks.com/v1.0/geolocation
// Run: WHOISFREAKS_API_KEY=your_api_key node BulkGeolocation.js
const { ApiClient, GeolocationApi, BulkGeolocationRequest } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new GeolocationApi(client);

// bulkGeolocation(bulkGeolocationRequest)
//   bulkGeolocationRequest (BulkGeolocationRequest, required): request body
async function main() {
  const body = BulkGeolocationRequest.constructFromObject({ ips: ["8.8.8.8", "1.1.1.1"] });
  const results = await api.bulkGeolocation(body);
  console.log(JSON.stringify(results, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```javascript
// Subdomains Lookup: GET https://api.whoisfreaks.com/v1.0/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key node Subdomains.js
const { ApiClient, SubdomainsApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new SubdomainsApi(client);

// subdomains(domain, opts)
//   domain (string, required)
//   opts.after (string, "yyyy-MM-dd", optional)
//   opts.before (string, "yyyy-MM-dd", optional)
//   opts.status (string, optional): one of active, inactive
//   opts.page (number, optional): default 1
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.subdomains("whoisfreaks.com", { page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```javascript
// IP Reputation Lookup: GET https://api.whoisfreaks.com/v1.0/security
// Run: WHOISFREAKS_API_KEY=your_api_key node IpReputation.js
const { ApiClient, IPReputationApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new IPReputationApi(client);

// ipReputation(ip)
//   ip (string, required)
async function main() {
  const result = await api.ipReputation("8.8.8.8");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Bulk IP Reputation

`POST /v1.0/security`

```javascript
// Bulk IP Reputation: POST https://api.whoisfreaks.com/v1.0/security
// Run: WHOISFREAKS_API_KEY=your_api_key node BulkIpReputation.js
const { ApiClient, IPReputationApi, BulkGeolocationRequest } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new IPReputationApi(client);

// bulkIpReputation(bulkGeolocationRequest)
//   bulkGeolocationRequest (BulkGeolocationRequest, required): request body
async function main() {
  const body = BulkGeolocationRequest.constructFromObject({ ips: ["8.8.8.8", "1.1.1.1"] });
  const results = await api.bulkIpReputation(body);
  console.log(JSON.stringify(results, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```javascript
// Domain Reputation Lookup: GET https://api.whoisfreaks.com/v1/domain/security
// Run: WHOISFREAKS_API_KEY=your_api_key node DomainReputation.js
const { ApiClient, DomainReputationApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DomainReputationApi(client);

// domainReputation(domainName, opts)
//   domainName (string, required): The domain name to assess
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.domainReputation("amazon.com");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```javascript
// ASN WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/asn-whois
// Run: WHOISFREAKS_API_KEY=your_api_key node AsnWhois.js
const { ApiClient, ASNWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new ASNWHOISApi(client);

// asnWhois(asn, opts)
//   asn (string, required)
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.asnWhois("as15169");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```javascript
// IP WHOIS Lookup: GET https://api.whoisfreaks.com/v1.0/ip-whois
// Run: WHOISFREAKS_API_KEY=your_api_key node IpWhois.js
const { ApiClient, IPWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new IPWHOISApi(client);

// ipWhois(ip, opts)
//   ip (string, required)
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.ipWhois("8.8.8.8");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```javascript
// Rotate API Key: GET https://api.whoisfreaks.com/v1.0/api-key/rotate
// Run: WHOISFREAKS_API_KEY=your_api_key node RotateApiKey.js
const { ApiClient, AccountApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new AccountApi(client);

// rotateApiKey() takes no parameters.
async function main() {
  const newKey = await api.rotateApiKey(); // use this key from now on
  console.log("New API key:", newKey);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```javascript
// Account Usage: GET https://api.whoisfreaks.com/v1.0/whoisapi/usage
// Run: WHOISFREAKS_API_KEY=your_api_key node AccountUsage.js
const { ApiClient, AccountApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new AccountApi(client);

// accountUsage() takes no parameters.
async function main() {
  const result = await api.accountUsage();
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Database File Status (Public)

`GET /v3.4/status`

```javascript
// Database File Status (Public): GET https://files.whoisfreaks.com/v3.4/status
// Run (public endpoint, no API key needed): node DatabaseFileStatus.js
const { AccountApi } = require("whoisfreaks-js");

// Public endpoint: no API key needed.
const api = new AccountApi();

// databaseFileStatus() takes no parameters.
async function main() {
  const result = await api.databaseFileStatus();
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```javascript
// Newly Registered gTLD (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld
// Run: WHOISFREAKS_API_KEY=your_api_key node DbNewlyGtld.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesNewlyRegisteredApi(client);

// dbNewlyGtld(whois, opts)
//   whois (boolean, required)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
//   opts.tlds (string, optional)
async function main() {
  const data = await api.dbNewlyGtld(true, { date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbNewlyGtld.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```javascript
// Newly Registered ccTLD (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/cctld
// Run: WHOISFREAKS_API_KEY=your_api_key node DbNewlyCctld.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesNewlyRegisteredApi(client);

// dbNewlyCctld(whois, opts)
//   whois (boolean, required)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
//   opts.tlds (string, optional)
async function main() {
  const data = await api.dbNewlyCctld(true, { date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbNewlyCctld.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```javascript
// Newly Registered gTLD Cleaned WHOIS (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld/cleaned
// Run: WHOISFREAKS_API_KEY=your_api_key node DbNewlyGtldCleaned.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesNewlyRegisteredApi(client);

// dbNewlyGtldCleaned(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbNewlyGtldCleaned({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbNewlyGtldCleaned.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```javascript
// Newly Registered ccTLD Cleaned WHOIS (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/cctld/cleaned
// Run: WHOISFREAKS_API_KEY=your_api_key node DbNewlyCctldCleaned.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesNewlyRegisteredApi(client);

// dbNewlyCctldCleaned(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbNewlyCctldCleaned({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbNewlyCctldCleaned.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```javascript
// Newly Registered gTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/gtld
// Run: WHOISFREAKS_API_KEY=your_api_key node DbNewlyGtldJson.js
const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesNewlyRegisteredApi(client);

// dbNewlyGtldJson(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
//   opts.tlds (string, optional)
async function main() {
  const domains = await api.dbNewlyGtldJson({ date: "2026-10-01" });
  console.log(`${domains.length} domains`);
  console.log(domains.slice(0, 10).join("\n"));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```javascript
// Newly Registered ccTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/cctld
// Run: WHOISFREAKS_API_KEY=your_api_key node DbNewlyCctldJson.js
const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesNewlyRegisteredApi(client);

// dbNewlyCctldJson(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
//   opts.tlds (string, optional)
async function main() {
  const domains = await api.dbNewlyCctldJson({ date: "2026-10-01" });
  console.log(`${domains.length} domains`);
  console.log(domains.slice(0, 10).join("\n"));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```javascript
// Newly Registered With DNS: GET https://files.whoisfreaks.com/v3.1/download/domainer/newly/dns
// Run: WHOISFREAKS_API_KEY=your_api_key node DbNewlyDns.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesNewlyRegisteredApi(client);

// dbNewlyDns(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbNewlyDns({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbNewlyDns.json";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```javascript
// Expiring Domains: GET https://files.whoisfreaks.com/v3.1/download/domainer/expired
// Run: WHOISFREAKS_API_KEY=your_api_key node DbExpired.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesExpiringDroppedApi(client);

// dbExpired(whois, opts)
//   whois (boolean, required)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbExpired(true, { date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbExpired.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```javascript
// Expiring Cleaned WHOIS: GET https://files.whoisfreaks.com/v3.1/download/domainer/expired/cleaned
// Run: WHOISFREAKS_API_KEY=your_api_key node DbExpiredCleaned.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesExpiringDroppedApi(client);

// dbExpiredCleaned(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbExpiredCleaned({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbExpiredCleaned.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```javascript
// Dropped Domains: GET https://files.whoisfreaks.com/v3.1/download/domainer/dropped
// Run: WHOISFREAKS_API_KEY=your_api_key node DbDropped.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesExpiringDroppedApi(client);

// dbDropped(whois, opts)
//   whois (boolean, required)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbDropped(true, { date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbDropped.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```javascript
// Dropped Domains (JSON): GET https://files.whoisfreaks.com/v3.1/domains/dropped
// Run: WHOISFREAKS_API_KEY=your_api_key node DbDroppedJson.js
const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesExpiringDroppedApi(client);

// dbDroppedJson(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
//   opts.tlds (string, optional)
async function main() {
  const domains = await api.dbDroppedJson({ date: "2026-10-01" });
  console.log(`${domains.length} domains`);
  console.log(domains.slice(0, 10).join("\n"));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```javascript
// Dropped With Backlinks: GET https://files.whoisfreaks.com/v3.3/download/domainer/dropped/backlinks
// Run: WHOISFREAKS_API_KEY=your_api_key node DbDroppedBacklinks.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesExpiringDroppedApi(client);

// dbDroppedBacklinks(opts)
//   opts.whois (boolean, optional)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbDroppedBacklinks({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbDroppedBacklinks.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```javascript
// WHOIS Database Daily: GET https://files.whoisfreaks.com/v3.3/download/dbupdate/daily/domains/whois
// Run: WHOISFREAKS_API_KEY=your_api_key node DbWhoisDaily.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesWHOISApi(client);

// dbWhoisDaily(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbWhoisDaily({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbWhoisDaily.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```javascript
// WHOIS Database Weekly: GET https://files.whoisfreaks.com/v3.3/download/dbupdate/weekly/domains/whois
// Run: WHOISFREAKS_API_KEY=your_api_key node DbWhoisWeekly.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesWHOISApi(client);

// dbWhoisWeekly(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbWhoisWeekly({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbWhoisWeekly.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```javascript
// WHOIS Database Monthly: GET https://files.whoisfreaks.com/v3.3/download/dbupdate/monthly/domains/whois
// Run: WHOISFREAKS_API_KEY=your_api_key node DbWhoisMonthly.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesWHOISApi(client);

// dbWhoisMonthly(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbWhoisMonthly({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbWhoisMonthly.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```javascript
// DNS Database Daily: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/daily/dns
// Run: WHOISFREAKS_API_KEY=your_api_key node DbDnsDaily.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesDNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesDNSApi(client);

// dbDnsDaily(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbDnsDaily({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbDnsDaily.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```javascript
// DNS Database Weekly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/weekly/dns
// Run: WHOISFREAKS_API_KEY=your_api_key node DbDnsWeekly.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesDNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesDNSApi(client);

// dbDnsWeekly(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbDnsWeekly({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbDnsWeekly.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```javascript
// DNS Database Monthly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/monthly/dns
// Run: WHOISFREAKS_API_KEY=your_api_key node DbDnsMonthly.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesDNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesDNSApi(client);

// dbDnsMonthly(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbDnsMonthly({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbDnsMonthly.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```javascript
// Subdomains Daily: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/daily/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key node DbSubdomainsDaily.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesSubdomainsApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesSubdomainsApi(client);

// dbSubdomainsDaily(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbSubdomainsDaily({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbSubdomainsDaily.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```javascript
// Subdomains Weekly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/weekly/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key node DbSubdomainsWeekly.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesSubdomainsApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesSubdomainsApi(client);

// dbSubdomainsWeekly(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbSubdomainsWeekly({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbSubdomainsWeekly.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```javascript
// Subdomains Monthly: GET https://files.whoisfreaks.com/v3.2/download/dbupdate/monthly/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key node DbSubdomainsMonthly.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesSubdomainsApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesSubdomainsApi(client);

// dbSubdomainsMonthly(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbSubdomainsMonthly({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbSubdomainsMonthly.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```javascript
// IP to Country Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/country
// Run: WHOISFREAKS_API_KEY=your_api_key node DbIpCountryStatus.js
const { ApiClient, DatabasesIPGeolocationApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesIPGeolocationApi(client);

// dbIpCountryStatus() takes no parameters.
async function main() {
  const result = await api.dbIpCountryStatus();
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```javascript
// IP to Country Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/country
// Run: WHOISFREAKS_API_KEY=your_api_key node DbIpCountry.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesIPGeolocationApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesIPGeolocationApi(client);

// dbIpCountry(date)
//   date (string, "yyyy-MM-dd", required)
async function main() {
  const data = await api.dbIpCountry("2026-10-01"); // a Buffer with the file's bytes
  const file = "DbIpCountry.zip";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```javascript
// IP to City Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/city
// Run: WHOISFREAKS_API_KEY=your_api_key node DbIpCityStatus.js
const { ApiClient, DatabasesIPGeolocationApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesIPGeolocationApi(client);

// dbIpCityStatus() takes no parameters.
async function main() {
  const result = await api.dbIpCityStatus();
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```javascript
// IP to City Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/city
// Run: WHOISFREAKS_API_KEY=your_api_key node DbIpCity.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesIPGeolocationApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesIPGeolocationApi(client);

// dbIpCity(date)
//   date (string, "yyyy-MM-dd", required)
async function main() {
  const data = await api.dbIpCity("2026-10-01"); // a Buffer with the file's bytes
  const file = "DbIpCity.zip";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```javascript
// ASN WHOIS Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/asn/whois
// Run: WHOISFREAKS_API_KEY=your_api_key node DbAsnWhois.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesASNWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesASNWHOISApi(client);

// dbAsnWhois(date)
//   date (string, "yyyy-MM-dd", required)
async function main() {
  const data = await api.dbAsnWhois("2026-10-01"); // a Buffer with the file's bytes
  const file = "DbAsnWhois.json.gz";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```javascript
// ASN WHOIS Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/asn/whois
// Run: WHOISFREAKS_API_KEY=your_api_key node DbAsnWhoisStatus.js
const { ApiClient, DatabasesASNWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesASNWHOISApi(client);

// dbAsnWhoisStatus() takes no parameters.
async function main() {
  const result = await api.dbAsnWhoisStatus();
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```javascript
// IP WHOIS Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/whois
// Run: WHOISFREAKS_API_KEY=your_api_key node DbIpWhois.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesIPWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesIPWHOISApi(client);

// dbIpWhois(date)
//   date (string, "yyyy-MM-dd", required)
async function main() {
  const data = await api.dbIpWhois("2026-10-01"); // a Buffer with the file's bytes
  const file = "DbIpWhois.json.gz";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```javascript
// IP WHOIS Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/whois
// Run: WHOISFREAKS_API_KEY=your_api_key node DbIpWhoisStatus.js
const { ApiClient, DatabasesIPWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesIPWHOISApi(client);

// dbIpWhoisStatus() takes no parameters.
async function main() {
  const result = await api.dbIpWhoisStatus();
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```javascript
// IP Security Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/ip/security
// Run: WHOISFREAKS_API_KEY=your_api_key node DbIpSecurity.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesIPSecurityApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesIPSecurityApi(client);

// dbIpSecurity(date)
//   date (string, "yyyy-MM-dd", required)
async function main() {
  const data = await api.dbIpSecurity("2026-10-01"); // a Buffer with the file's bytes
  const file = "DbIpSecurity.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```javascript
// IP Security Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/security
// Run: WHOISFREAKS_API_KEY=your_api_key node DbIpSecurityStatus.js
const { ApiClient, DatabasesIPSecurityApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesIPSecurityApi(client);

// dbIpSecurityStatus() takes no parameters.
async function main() {
  const result = await api.dbIpSecurityStatus();
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

### Databases - Threat Feed

#### Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

```javascript
// Download the daily phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing
// Run: WHOISFREAKS_API_KEY=your_api_key node DownloadThreatFeedPhishing.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesThreatFeedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesThreatFeedApi(client);

// downloadThreatFeedPhishing(opts)
//   opts.date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
async function main() {
  const data = await api.downloadThreatFeedPhishing({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DownloadThreatFeedPhishing.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

```javascript
// Download a sample of the phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing/sample
// Run: WHOISFREAKS_API_KEY=your_api_key node DownloadThreatFeedPhishingSample.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesThreatFeedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesThreatFeedApi(client);

// downloadThreatFeedPhishingSample() takes no parameters.
async function main() {
  const data = await api.downloadThreatFeedPhishingSample(); // a Buffer with the file's bytes
  const file = "DownloadThreatFeedPhishingSample.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

```javascript
// Download the daily malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/malware
// Run: WHOISFREAKS_API_KEY=your_api_key node DownloadThreatFeedMalware.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesThreatFeedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesThreatFeedApi(client);

// downloadThreatFeedMalware(opts)
//   opts.date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
async function main() {
  const data = await api.downloadThreatFeedMalware({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DownloadThreatFeedMalware.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

```javascript
// Download a sample of the malware threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/malware/sample
// Run: WHOISFREAKS_API_KEY=your_api_key node DownloadThreatFeedMalwareSample.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesThreatFeedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesThreatFeedApi(client);

// downloadThreatFeedMalwareSample() takes no parameters.
async function main() {
  const data = await api.downloadThreatFeedMalwareSample(); // a Buffer with the file's bytes
  const file = "DownloadThreatFeedMalwareSample.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

```javascript
// Download the daily spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam
// Run: WHOISFREAKS_API_KEY=your_api_key node DownloadThreatFeedSpam.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesThreatFeedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesThreatFeedApi(client);

// downloadThreatFeedSpam(opts)
//   opts.date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
async function main() {
  const data = await api.downloadThreatFeedSpam({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DownloadThreatFeedSpam.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```

#### Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

```javascript
// Download a sample of the spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/spam/sample
// Run: WHOISFREAKS_API_KEY=your_api_key node DownloadThreatFeedSpamSample.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesThreatFeedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesThreatFeedApi(client);

// downloadThreatFeedSpamSample() takes no parameters.
async function main() {
  const data = await api.downloadThreatFeedSpamSample(); // a Buffer with the file's bytes
  const file = "DownloadThreatFeedSpamSample.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
```
