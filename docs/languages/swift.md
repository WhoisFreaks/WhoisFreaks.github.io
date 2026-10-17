# Swift SDK

## About

The official **WhoisFreaks Swift SDK**: a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from Swift with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to Swift PM.

**Keywords:** swift whois api, swift whois sdk, whoisfreaks swift, swift domain lookup, swift dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** Swift PM
- **Package:** `github.com/WhoisFreaks/whoisfreaks-swift`

## Install

```swift
.package(url: "https://github.com/WhoisFreaks/whoisfreaks-swift.git", from: "0.24.0")
```

## Build from Source

Prefer to build the SDK yourself instead of installing from Swift PM? Clone the Swift SDK repository and build it locally:

```bash
git clone https://github.com/WhoisFreaks/whoisfreaks-swift
cd whoisfreaks-swift
swift build
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

You need Swift 5.7 or later (Xcode 14+) on macOS 10.15 or later. The SDK uses async/await.

1. Create an executable package:

```bash
mkdir -p whoisfreaks-test/Sources/WhoisFreaksTest
cd whoisfreaks-test
```

2. Create `Package.swift` with the SDK as a dependency:

```swift
// swift-tools-version:5.7
import PackageDescription

let package = Package(
    name: "WhoisFreaksTest",
    platforms: [.macOS(.v10_15)],
    dependencies: [
        .package(url: "https://github.com/WhoisFreaks/whoisfreaks-swift.git", from: "0.24.0"),
    ],
    targets: [
        .executableTarget(
            name: "WhoisFreaksTest",
            dependencies: [.product(name: "WhoisFreaks", package: "whoisfreaks-swift")]
        ),
    ]
)
```

3. Create `Sources/WhoisFreaksTest/main.swift`:

```swift
import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

let record = try await WHOISAPI.whoisLive(domainName: "whoisfreaks.com")

print("Registrar:", record.domainRegistrar?.registrarName ?? "-")
print("Created:  ", record.createDate ?? "-")
print("Expires:  ", record.expiryDate ?? "-")
```

4. Set your API key and run it:

```bash
export WHOISFREAKS_API_KEY="your_api_key"
swift run
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

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

## Endpoints

All 60 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

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

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```swift
// Bulk WHOIS Lookup
//
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required): request body object
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

let request = BulkWhoisRequest(domainNames: ["whoisfreaks.com", "jfreaks.com"])

do {
    let result = try await WHOISAPI.bulkWhois(bulkWhoisRequest: request)
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

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```swift
// Historical WHOIS records for a domain
//
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await WHOISAPI.whoisHistory(domainName: "whoisfreaks.com")
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

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```swift
// Reverse WHOIS lookup by keyword
//
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await WHOISAPI.whoisReverse(keyword: "whoisfreaks", page: 1)
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

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```swift
// Live DNS Lookup
//
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, optional)
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DNSAPI.dnsLive(type: "A,MX,TXT", domainName: "whoisfreaks.com")
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

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```swift
// Historical DNS Lookup
//
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DNSAPI.dnsHistorical(domainName: "whoisfreaks.com", type: "A,MX,TXT", page: 1)
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

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```swift
// Reverse DNS Lookup
//
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DNSAPI.dnsReverse(value: "8.8.8.8", type: .a, page: 1)
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

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```swift
// Bulk DNS Lookup
//
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required): request body object
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

let request = DnsBulkRequest(domainNames: ["whoisfreaks.com", "example.com"])

do {
    let result = try await DNSAPI.dnsBulk(type: "A,MX,TXT", dnsBulkRequest: request)
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

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```swift
// Domain Availability Check with Suggestions
//
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DomainAvailabilityAPI.domainAvailabilityV2(domain: "google.com", sug: true, count: 5)
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

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```swift
// Bulk Domain Availability Check
//
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required): request body object
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

let request = BulkDomainAvailabilityRequest(domainNames: ["whoisfreaks.com", "example.com"])

do {
    let result = try await DomainAvailabilityAPI.bulkDomainAvailabilityV2(bulkDomainAvailabilityRequest: request)
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

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```swift
// Typosquatting Lookup
//
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await TyposquattingAPI.typosquatting(keyword: "whoisfreaks")
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

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```swift
// SSL Certificate Lookup
//
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await SSLAPI.sslLookup(domainName: "whoisfreaks.com")
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

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```swift
// IP Geolocation Lookup
//
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await GeolocationAPI.geolocation(ip: "8.8.8.8")
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

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```swift
// Bulk IP Geolocation
//
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required): request body object
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

let request = BulkGeolocationRequest(ips: ["8.8.8.8", "1.1.1.1"])

do {
    let result = try await GeolocationAPI.bulkGeolocation(bulkGeolocationRequest: request)
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

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```swift
// Subdomains Lookup
//
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await SubdomainsAPI.subdomains(domain: "whoisfreaks.com", page: 1)
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

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```swift
// IP Reputation Lookup
//
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await IPReputationAPI.ipReputation(ip: "8.8.8.8")
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

#### Bulk IP Reputation

`POST /v1.0/security`

```swift
// Bulk IP Reputation
//
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkGeolocationRequest (required): request body object
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

let request = BulkGeolocationRequest(ips: ["8.8.8.8", "1.1.1.1"])

do {
    let result = try await IPReputationAPI.bulkIpReputation(bulkGeolocationRequest: request)
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

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```swift
// Domain Reputation Lookup
//
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DomainReputationAPI.domainReputation(domainName: "amazon.com")
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

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```swift
// ASN WHOIS Lookup
//
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await ASNWHOISAPI.asnWhois(asn: "as15169")
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

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```swift
// IP WHOIS Lookup
//
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await IPWHOISAPI.ipWhois(ip: "8.8.8.8")
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

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```swift
// Rotate API Key
//
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let newKey = try await AccountAPI.rotateApiKey()
    // The old key stops working now: store the new one before making more calls.
    print("New API key: \(newKey)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```swift
// Account Usage
//
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await AccountAPI.accountUsage()
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

#### Database File Status (Public)

`GET /v3.4/status`

```swift
// Database File Status (Public)
//
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; no API key required)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]
// (This endpoint is public, so the key is not sent with this request.)

do {
    let result = try await AccountAPI.databaseFileStatus()
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

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```swift
// Newly Registered gTLD (CSV)
//
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesNewlyRegisteredAPI.dbNewlyGtld(whois: true, date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbNewlyGtld.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```swift
// Newly Registered ccTLD (CSV)
//
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesNewlyRegisteredAPI.dbNewlyCctld(whois: true, date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbNewlyCctld.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```swift
// Newly Registered gTLD Cleaned WHOIS (CSV)
//
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesNewlyRegisteredAPI.dbNewlyGtldCleaned(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbNewlyGtldCleaned.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```swift
// Newly Registered ccTLD Cleaned WHOIS (CSV)
//
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesNewlyRegisteredAPI.dbNewlyCctldCleaned(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbNewlyCctldCleaned.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```swift
// Newly Registered gTLD (JSON)
//
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let domains = try await DatabasesNewlyRegisteredAPI.dbNewlyGtldJson(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    print(domains.joined(separator: "\n"))
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```swift
// Newly Registered ccTLD (JSON)
//
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let domains = try await DatabasesNewlyRegisteredAPI.dbNewlyCctldJson(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    print(domains.joined(separator: "\n"))
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```swift
// Newly Registered With DNS
//
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesNewlyRegisteredAPI.dbNewlyDns(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbNewlyDns.json")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```swift
// Expiring Domains
//
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesExpiringDroppedAPI.dbExpired(whois: true, date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbExpired.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```swift
// Expiring Cleaned WHOIS
//
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesExpiringDroppedAPI.dbExpiredCleaned(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbExpiredCleaned.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```swift
// Dropped Domains
//
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesExpiringDroppedAPI.dbDropped(whois: true, date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbDropped.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```swift
// Dropped Domains (JSON)
//
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let domains = try await DatabasesExpiringDroppedAPI.dbDroppedJson(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    print(domains.joined(separator: "\n"))
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```swift
// Dropped With Backlinks
//
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesExpiringDroppedAPI.dbDroppedBacklinks(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbDroppedBacklinks.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```swift
// WHOIS Database Daily
//
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesWHOISAPI.dbWhoisDaily(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbWhoisDaily.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```swift
// WHOIS Database Weekly
//
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesWHOISAPI.dbWhoisWeekly(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbWhoisWeekly.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```swift
// WHOIS Database Monthly
//
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesWHOISAPI.dbWhoisMonthly(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbWhoisMonthly.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```swift
// DNS Database Daily
//
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesDNSAPI.dbDnsDaily(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbDnsDaily.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```swift
// DNS Database Weekly
//
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesDNSAPI.dbDnsWeekly(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbDnsWeekly.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```swift
// DNS Database Monthly
//
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesDNSAPI.dbDnsMonthly(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbDnsMonthly.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```swift
// Subdomains Daily
//
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesSubdomainsAPI.dbSubdomainsDaily(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbSubdomainsDaily.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```swift
// Subdomains Weekly
//
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesSubdomainsAPI.dbSubdomainsWeekly(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbSubdomainsWeekly.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```swift
// Subdomains Monthly
//
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesSubdomainsAPI.dbSubdomainsMonthly(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbSubdomainsMonthly.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```swift
// IP to Country Snapshot Status
//
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DatabasesIPGeolocationAPI.dbIpCountryStatus()
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

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```swift
// IP to Country Snapshot
//
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesIPGeolocationAPI.dbIpCountry(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbIpCountry.zip")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```swift
// IP to City Snapshot Status
//
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DatabasesIPGeolocationAPI.dbIpCityStatus()
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

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```swift
// IP to City Snapshot
//
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesIPGeolocationAPI.dbIpCity(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbIpCity.zip")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```swift
// ASN WHOIS Snapshot
//
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesASNWHOISAPI.dbAsnWhois(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbAsnWhois.json.gz")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```swift
// ASN WHOIS Snapshot Status
//
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DatabasesASNWHOISAPI.dbAsnWhoisStatus()
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

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```swift
// IP WHOIS Snapshot
//
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesIPWHOISAPI.dbIpWhois(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbIpWhois.json.gz")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```swift
// IP WHOIS Snapshot Status
//
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DatabasesIPWHOISAPI.dbIpWhoisStatus()
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

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```swift
// IP Security Snapshot
//
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesIPSecurityAPI.dbIpSecurity(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbIpSecurity.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```swift
// IP Security Snapshot Status
//
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DatabasesIPSecurityAPI.dbIpSecurityStatus()
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

### Databases - Threat Feed

#### Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

```swift
// Download the daily phishing threat feed (CSV)
//
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesThreatFeedAPI.downloadThreatFeedPhishing(date: "2026-10-01")
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DownloadThreatFeedPhishing.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

```swift
// Download a sample of the phishing threat feed (CSV)
//
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesThreatFeedAPI.downloadThreatFeedPhishingSample()
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DownloadThreatFeedPhishingSample.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

```swift
// Download the daily malware threat feed (CSV)
//
// Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesThreatFeedAPI.downloadThreatFeedMalware(date: "2026-10-01")
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DownloadThreatFeedMalware.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

```swift
// Download a sample of the malware threat feed (CSV)
//
// Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
//   (no parameters; the API key is set on the client)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesThreatFeedAPI.downloadThreatFeedMalwareSample()
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DownloadThreatFeedMalwareSample.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

```swift
// Download the daily spam threat feed (CSV)
//
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesThreatFeedAPI.downloadThreatFeedSpam(date: "2026-10-01")
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DownloadThreatFeedSpam.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```

#### Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

```swift
// Download a sample of the spam threat feed (CSV)
//
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesThreatFeedAPI.downloadThreatFeedSpamSample()
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DownloadThreatFeedSpamSample.csv")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}

```
