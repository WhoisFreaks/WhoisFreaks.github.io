# Kotlin SDK

## About

The official **WhoisFreaks Kotlin SDK**: a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from Kotlin with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to Maven Central.

**Keywords:** kotlin whois api, kotlin whois sdk, whoisfreaks kotlin, kotlin domain lookup, kotlin dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** Maven Central
- **Package:** `com.whoisfreaks:whoisfreaks-kotlin`

## Install

```kotlin
implementation("com.whoisfreaks:whoisfreaks-kotlin:0.24.0")
```

## Build from Source

Prefer to build the SDK yourself instead of installing from Maven Central? Clone the Kotlin SDK repository and build it locally:

```bash
git clone https://github.com/WhoisFreaks/whoisfreaks-kotlin
cd whoisfreaks-kotlin
./gradlew build   # or: ./gradlew publishToMavenLocal
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

You need JDK 11 or later and [Gradle](https://gradle.org/install/) 8. Create the project directory:

```bash
mkdir -p whoisfreaks-test/src/main/kotlin && cd whoisfreaks-test
```

Create `settings.gradle.kts`:

```kotlin
rootProject.name = "whoisfreaks-test"
```

Create `build.gradle.kts`. The `mainClass` property picks the program that `gradle run` starts:

```kotlin
plugins {
    kotlin("jvm") version "2.0.21"
    application
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.whoisfreaks:whoisfreaks-kotlin:0.24.0")
}

application {
    mainClass.set(providers.gradleProperty("mainClass").orElse("MainKt"))
}
```

Create `src/main/kotlin/Main.kt`:

```kotlin
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call

    val record = WHOISApi().whoisLive("whoisfreaks.com")
    println("${record.domainName} expires ${record.expiryDate}")
    println(record)
}
```

Set your API key and run it:

```bash
export WHOISFREAKS_API_KEY="your_api_key"
gradle run
```

To run one of the [runnable examples](../../examples/kotlin/README.md), copy it into `src/main/kotlin` and pass its class name (file name plus `Kt`), for example `gradle run -PmainClass=WhoisLiveKt`.

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```kotlin
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Run it from the Getting Started project: gradle run -PmainClass=WhoisLiveKt
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required): Domain to look up.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = WHOISApi()

    val result = api.whoisLive("whoisfreaks.com")
    println(result)
}

```

## Endpoints

All 95 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```kotlin
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Run it from the Getting Started project: gradle run -PmainClass=WhoisLiveKt
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required): Domain to look up.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = WHOISApi()

    val result = api.whoisLive("whoisfreaks.com")
    println(result)
}

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```kotlin
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Run it from the Getting Started project: gradle run -PmainClass=BulkWhoisKt
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
//   - body: BulkWhoisRequest (required): request body object
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkWhoisRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = WHOISApi()

    val body = BulkWhoisRequest(domainNames = listOf("whoisfreaks.com", "jfreaks.com"))
    val result = api.bulkWhois(body)
    println(result)
}

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```kotlin
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Run it from the Getting Started project: gradle run -PmainClass=WhoisHistoryKt
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = WHOISApi()

    val result = api.whoisHistory("whoisfreaks.com")
    println(result)
}

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```kotlin
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Run it from the Getting Started project: gradle run -PmainClass=WhoisReverseKt
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = WHOISApi()

    val result = api.whoisReverse("whoisfreaks", page = 1)
    println(result)
}

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```kotlin
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Run it from the Getting Started project: gradle run -PmainClass=DnsLiveKt
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, optional): Domain to look up.
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val result = api.dnsLive("A,MX,TXT", domainName = "whoisfreaks.com")
    println(result)
}

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```kotlin
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Run it from the Getting Started project: gradle run -PmainClass=DnsHistoricalKt
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val result = api.dnsHistorical("whoisfreaks.com", "A,MX,TXT", page = 1)
    println(result)
}

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```kotlin
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Run it from the Getting Started project: gradle run -PmainClass=DnsReverseKt
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): Set true to match value exactly. Defaults to false, where value is treated as a pattern...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val result = api.dnsReverse("8.8.8.8", DNSApi.TypeDnsReverse.a, page = 1)
    println(result)
}

```

#### Historical DNS Lookup (v2.2)

`GET /v2.2/dns/historical`

```kotlin
// Runnable example: Historical DNS Lookup (v2.2) (GET /v2.2/dns/historical)
// Run it from the Getting Started project: gradle run -PmainClass=DnsHistoricalV22Kt
// Parameters for dnsHistoricalV22 (GET /v2.2/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val result = api.dnsHistoricalV22("whoisfreaks.com", "A,MX,TXT", page = 1)
    println(result)
}

```

#### Historical DNS Lookup (v2.3)

`GET /v2.3/dns/historical`

```kotlin
// Runnable example: Historical DNS Lookup (v2.3) (GET /v2.3/dns/historical)
// Run it from the Getting Started project: gradle run -PmainClass=DnsHistoricalV23Kt
// Parameters for dnsHistoricalV23 (GET /v2.3/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val result = api.dnsHistoricalV23("whoisfreaks.com", "A,MX,TXT", page = 1)
    println(result)
}

```

#### Reverse DNS Lookup (v2.2)

`GET /v2.2/dns/reverse`

```kotlin
// Runnable example: Reverse DNS Lookup (v2.2) (GET /v2.2/dns/reverse)
// Run it from the Getting Started project: gradle run -PmainClass=DnsReverseV22Kt
// Parameters for dnsReverseV22 (GET /v2.2/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): When false the value is matched as a substring, which is far slower than an exact match...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val result = api.dnsReverseV22("8.8.8.8", DNSApi.TypeDnsReverseV22.a, page = 1)
    println(result)
}

```

#### Reverse DNS Lookup (v2.3)

`GET /v2.3/dns/reverse`

```kotlin
// Runnable example: Reverse DNS Lookup (v2.3) (GET /v2.3/dns/reverse)
// Run it from the Getting Started project: gradle run -PmainClass=DnsReverseV23Kt
// Parameters for dnsReverseV23 (GET /v2.3/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): When false the value is matched as a substring, which is far slower than an exact match...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val result = api.dnsReverseV23("8.8.8.8", DNSApi.TypeDnsReverseV23.a, page = 1)
    println(result)
}

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```kotlin
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Run it from the Getting Started project: gradle run -PmainClass=DnsBulkKt
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
//   - body: DnsBulkRequest (required): request body object
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.DnsBulkRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val body = DnsBulkRequest(domainNames = listOf("whoisfreaks.com", "example.com"))
    val result = api.dnsBulk("A,MX,TXT", body)
    println(result)
}

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```kotlin
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Run it from the Getting Started project: gradle run -PmainClass=DomainAvailabilityV2Kt
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.DomainAvailabilityApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DomainAvailabilityApi()

    val result = api.domainAvailabilityV2("google.com", sug = true, count = 5)
    println(result)
}

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```kotlin
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Run it from the Getting Started project: gradle run -PmainClass=BulkDomainAvailabilityV2Kt
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
//   - body: BulkDomainAvailabilityRequest (required): request body object
import com.whoisfreaks.client.apis.DomainAvailabilityApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkDomainAvailabilityRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DomainAvailabilityApi()

    val body = BulkDomainAvailabilityRequest(domainNames = listOf("whoisfreaks.com", "example.com"))
    val result = api.bulkDomainAvailabilityV2(body)
    println(result)
}

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```kotlin
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Run it from the Getting Started project: gradle run -PmainClass=TyposquattingKt
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional): Brand or label to find typo variants for. Pass either keyword or pattern, not both.
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters. Pass either keyword or patter...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
import com.whoisfreaks.client.apis.TyposquattingApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = TyposquattingApi()

    val result = api.typosquatting(keyword = "whoisfreaks")
    println(result)
}

```

#### Subdomain Typosquatting Lookup

`GET /v3.0/subdomains/typos`

```kotlin
// Runnable example: Subdomain Typosquatting Lookup (GET /v3.0/subdomains/typos)
// Run it from the Getting Started project: gradle run -PmainClass=SubdomainTyposquattingKt
// Parameters for subdomainTyposquatting (GET /v3.0/subdomains/typos):
//   - keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits and hyphe...
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one. At most 2...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
//   - fetch_size (integer, optional): Subdomains per page. 100 when the parameter is left out, and values above 10000 are cap...
import com.whoisfreaks.client.apis.TyposquattingApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = TyposquattingApi()

    val result = api.subdomainTyposquatting(keyword = "paypal")
    println(result)
}

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```kotlin
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Run it from the Getting Started project: gradle run -PmainClass=SslLookupKt
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required): Domain to look up.
//   - chain (boolean, optional): Set true to return the full certificate chain, ordered from the end-user certificate to...
//   - sslRaw (boolean, optional): Set true to include the raw OpenSSL response for the domain. Defaults to false.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.SSLApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = SSLApi()

    val result = api.sslLookup("whoisfreaks.com")
    println(result)
}

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```kotlin
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Run it from the Getting Started project: gradle run -PmainClass=GeolocationKt
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required): IP address to look up.
import com.whoisfreaks.client.apis.GeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = GeolocationApi()

    val result = api.geolocation("8.8.8.8")
    println(result)
}

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```kotlin
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Run it from the Getting Started project: gradle run -PmainClass=BulkGeolocationKt
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.apis.GeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkGeolocationRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = GeolocationApi()

    val body = BulkGeolocationRequest(ips = listOf("8.8.8.8", "1.1.1.1"))
    val result = api.bulkGeolocation(body)
    println(result)
}

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```kotlin
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Run it from the Getting Started project: gradle run -PmainClass=SubdomainsKt
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required): Domain whose subdomains you want.
//   - after (string, optional): Only return records created after this date, in YYYY-MM-DD format. Defaults to the olde...
//   - before (string, optional): Only return records created before this date, in YYYY-MM-DD format. Defaults to today, ...
//   - status (string (one of: active, inactive), optional): Limit results to active or inactive subdomains. Both are returned when the parameter is...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.SubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = SubdomainsApi()

    val result = api.subdomains("whoisfreaks.com", page = 1)
    println(result)
}

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```kotlin
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Run it from the Getting Started project: gradle run -PmainClass=IpReputationKt
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required): IP address to look up.
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = IPReputationApi()

    val result = api.ipReputation("8.8.8.8")
    println(result)
}

```

#### Bulk IP Reputation

`POST /v1.0/security`

```kotlin
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Run it from the Getting Started project: gradle run -PmainClass=BulkIpReputationKt
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkGeolocationRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = IPReputationApi()

    val body = BulkGeolocationRequest(ips = listOf("8.8.8.8", "1.1.1.1"))
    val result = api.bulkIpReputation(body)
    println(result)
}

```

#### IP Reputation Lookup (v2.0)

`GET /v2.0/security`

```kotlin
// Runnable example: IP Reputation Lookup (v2.0) (GET /v2.0/security)
// Run it from the Getting Started project: gradle run -PmainClass=IpReputationV2Kt
// Parameters for ipReputationV2 (GET /v2.0/security):
//   - ip (string, required): IP address to look up.
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = IPReputationApi()

    val result = api.ipReputationV2("8.8.8.8")
    println(result)
}

```

#### Bulk IP Reputation (v2.0)

`POST /v2.0/security`

```kotlin
// Runnable example: Bulk IP Reputation (v2.0) (POST /v2.0/security)
// Run it from the Getting Started project: gradle run -PmainClass=BulkIpReputationV2Kt
// Parameters for bulkIpReputationV2 (POST /v2.0/security):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkGeolocationRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = IPReputationApi()

    val body = BulkGeolocationRequest(ips = listOf("1.1.1.1", "2.2.2.2", "8.8.8.8"))
    val result = api.bulkIpReputationV2(body)
    println(result)
}

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```kotlin
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Run it from the Getting Started project: gradle run -PmainClass=DomainReputationKt
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.DomainReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DomainReputationApi()

    val result = api.domainReputation("amazon.com")
    println(result)
}

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```kotlin
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Run it from the Getting Started project: gradle run -PmainClass=AsnWhoisKt
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required): Autonomous system number to look up, with or without the AS prefix.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.ASNWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = ASNWHOISApi()

    val result = api.asnWhois("as15169")
    println(result)
}

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```kotlin
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Run it from the Getting Started project: gradle run -PmainClass=IpWhoisKt
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required): IP address to look up.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.IPWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = IPWHOISApi()

    val result = api.ipWhois("8.8.8.8")
    println(result)
}

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```kotlin
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Run it from the Getting Started project: gradle run -PmainClass=RotateApiKeyKt
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.AccountApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = AccountApi()

    val newKey = api.rotateApiKey()
    // The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.
    println("New API key: $newKey")
}

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```kotlin
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Run it from the Getting Started project: gradle run -PmainClass=AccountUsageKt
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.AccountApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = AccountApi()

    val result = api.accountUsage()
    println(result)
}

```

#### Database File Status (Public)

`GET /v3.4/status`

```kotlin
// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Run it from the Getting Started project: gradle run -PmainClass=DatabaseFileStatusKt
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; no API key required)
import com.whoisfreaks.client.apis.AccountApi

fun main() {
    // Public endpoint: no API key needed.
    val api = AccountApi()

    val result = api.databaseFileStatus()
    println(result)
}

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```kotlin
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Run it from the Getting Started project: gradle run -PmainClass=DbNewlyGtldKt
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesNewlyRegisteredApi()

    val download = api.dbNewlyGtld(true, date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbNewlyGtld.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```kotlin
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Run it from the Getting Started project: gradle run -PmainClass=DbNewlyCctldKt
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesNewlyRegisteredApi()

    val download = api.dbNewlyCctld(true, date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbNewlyCctld.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```kotlin
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=DbNewlyGtldCleanedKt
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesNewlyRegisteredApi()

    val download = api.dbNewlyGtldCleaned(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbNewlyGtldCleaned.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```kotlin
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=DbNewlyCctldCleanedKt
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesNewlyRegisteredApi()

    val download = api.dbNewlyCctldCleaned(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbNewlyCctldCleaned.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```kotlin
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Run it from the Getting Started project: gradle run -PmainClass=DbNewlyGtldJsonKt
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesNewlyRegisteredApi()

    val result = api.dbNewlyGtldJson(date = LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```kotlin
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Run it from the Getting Started project: gradle run -PmainClass=DbNewlyCctldJsonKt
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesNewlyRegisteredApi()

    val result = api.dbNewlyCctldJson(date = LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```kotlin
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Run it from the Getting Started project: gradle run -PmainClass=DbNewlyDnsKt
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesNewlyRegisteredApi()

    val download = api.dbNewlyDns(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbNewlyDns.json"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```kotlin
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Run it from the Getting Started project: gradle run -PmainClass=DbExpiredKt
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesExpiringDroppedApi()

    val download = api.dbExpired(true, date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbExpired.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```kotlin
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=DbExpiredCleanedKt
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesExpiringDroppedApi()

    val download = api.dbExpiredCleaned(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbExpiredCleaned.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```kotlin
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Run it from the Getting Started project: gradle run -PmainClass=DbDroppedKt
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesExpiringDroppedApi()

    val download = api.dbDropped(true, date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbDropped.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```kotlin
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Run it from the Getting Started project: gradle run -PmainClass=DbDroppedJsonKt
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesExpiringDroppedApi()

    val result = api.dbDroppedJson(date = LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```kotlin
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Run it from the Getting Started project: gradle run -PmainClass=DbDroppedBacklinksKt
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesExpiringDroppedApi()

    val download = api.dbDroppedBacklinks(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbDroppedBacklinks.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```kotlin
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Run it from the Getting Started project: gradle run -PmainClass=DbWhoisDailyKt
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesWHOISApi()

    val download = api.dbWhoisDaily(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbWhoisDaily.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```kotlin
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Run it from the Getting Started project: gradle run -PmainClass=DbWhoisWeeklyKt
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesWHOISApi()

    val download = api.dbWhoisWeekly(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbWhoisWeekly.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```kotlin
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Run it from the Getting Started project: gradle run -PmainClass=DbWhoisMonthlyKt
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesWHOISApi()

    val download = api.dbWhoisMonthly(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbWhoisMonthly.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```kotlin
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Run it from the Getting Started project: gradle run -PmainClass=DbDnsDailyKt
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesDNSApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesDNSApi()

    val download = api.dbDnsDaily(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbDnsDaily.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```kotlin
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Run it from the Getting Started project: gradle run -PmainClass=DbDnsWeeklyKt
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesDNSApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesDNSApi()

    val download = api.dbDnsWeekly(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbDnsWeekly.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```kotlin
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Run it from the Getting Started project: gradle run -PmainClass=DbDnsMonthlyKt
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesDNSApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesDNSApi()

    val download = api.dbDnsMonthly(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbDnsMonthly.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```kotlin
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Run it from the Getting Started project: gradle run -PmainClass=DbSubdomainsDailyKt
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesSubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesSubdomainsApi()

    val download = api.dbSubdomainsDaily(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbSubdomainsDaily.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```kotlin
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Run it from the Getting Started project: gradle run -PmainClass=DbSubdomainsWeeklyKt
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesSubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesSubdomainsApi()

    val download = api.dbSubdomainsWeekly(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbSubdomainsWeekly.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```kotlin
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Run it from the Getting Started project: gradle run -PmainClass=DbSubdomainsMonthlyKt
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesSubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesSubdomainsApi()

    val download = api.dbSubdomainsMonthly(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbSubdomainsMonthly.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```kotlin
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpCountryStatusKt
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPGeolocationApi()

    val result = api.dbIpCountryStatus()
    println(result)
}

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```kotlin
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpCountryKt
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPGeolocationApi()

    val download = api.dbIpCountry(LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbIpCountry.zip"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```kotlin
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpCityStatusKt
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPGeolocationApi()

    val result = api.dbIpCityStatus()
    println(result)
}

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```kotlin
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpCityKt
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPGeolocationApi()

    val download = api.dbIpCity(LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbIpCity.zip"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```kotlin
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Run it from the Getting Started project: gradle run -PmainClass=DbAsnWhoisKt
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
import com.whoisfreaks.client.apis.DatabasesASNWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesASNWHOISApi()

    val download = api.dbAsnWhois(LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbAsnWhois.json.gz"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```kotlin
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Run it from the Getting Started project: gradle run -PmainClass=DbAsnWhoisStatusKt
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesASNWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesASNWHOISApi()

    val result = api.dbAsnWhoisStatus()
    println(result)
}

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```kotlin
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpWhoisKt
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
import com.whoisfreaks.client.apis.DatabasesIPWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPWHOISApi()

    val download = api.dbIpWhois(LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbIpWhois.json.gz"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```kotlin
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpWhoisStatusKt
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPWHOISApi()

    val result = api.dbIpWhoisStatus()
    println(result)
}

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```kotlin
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpSecurityKt
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
import com.whoisfreaks.client.apis.DatabasesIPSecurityApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPSecurityApi()

    val download = api.dbIpSecurity(LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbIpSecurity.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```kotlin
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpSecurityStatusKt
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPSecurityApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPSecurityApi()

    val result = api.dbIpSecurityStatus()
    println(result)
}

```

### Databases - Threat Feed

#### Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

```kotlin
// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Run it from the Getting Started project: gradle run -PmainClass=DownloadThreatFeedPhishingKt
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
import com.whoisfreaks.client.apis.DatabasesThreatFeedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesThreatFeedApi()

    val download = api.downloadThreatFeedPhishing(date = "2026-10-01")
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DownloadThreatFeedPhishing.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

```kotlin
// Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
// Run it from the Getting Started project: gradle run -PmainClass=DownloadThreatFeedPhishingSampleKt
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesThreatFeedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesThreatFeedApi()

    val download = api.downloadThreatFeedPhishingSample()
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DownloadThreatFeedPhishingSample.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

```kotlin
// Runnable example: Download the daily malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware)
// Run it from the Getting Started project: gradle run -PmainClass=DownloadThreatFeedMalwareKt
// Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
import com.whoisfreaks.client.apis.DatabasesThreatFeedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesThreatFeedApi()

    val download = api.downloadThreatFeedMalware(date = "2026-10-01")
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DownloadThreatFeedMalware.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

```kotlin
// Runnable example: Download a sample of the malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware/sample)
// Run it from the Getting Started project: gradle run -PmainClass=DownloadThreatFeedMalwareSampleKt
// Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesThreatFeedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesThreatFeedApi()

    val download = api.downloadThreatFeedMalwareSample()
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DownloadThreatFeedMalwareSample.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

```kotlin
// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Run it from the Getting Started project: gradle run -PmainClass=DownloadThreatFeedSpamKt
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
import com.whoisfreaks.client.apis.DatabasesThreatFeedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesThreatFeedApi()

    val download = api.downloadThreatFeedSpam(date = "2026-10-01")
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DownloadThreatFeedSpam.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

#### Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

```kotlin
// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Run it from the Getting Started project: gradle run -PmainClass=DownloadThreatFeedSpamSampleKt
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesThreatFeedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesThreatFeedApi()

    val download = api.downloadThreatFeedSpamSample()
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DownloadThreatFeedSpamSample.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}

```

### Databases - Streaming

#### Stream the daily phishing threat feed (CSV)

`GET /v3.4/stream/threat-feed/phishing`

```kotlin
// Runnable example: Stream the daily phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing)
// Run it from the Getting Started project: gradle run -PmainClass=StreamThreatFeedPhishingKt
// Parameters for streamThreatFeedPhishing (GET /v3.4/stream/threat-feed/phishing):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamThreatFeedPhishing(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream a sample of the phishing threat feed (CSV)

`GET /v3.4/stream/threat-feed/phishing/sample`

```kotlin
// Runnable example: Stream a sample of the phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing/sample)
// Run it from the Getting Started project: gradle run -PmainClass=StreamThreatFeedPhishingSampleKt
// Parameters for streamThreatFeedPhishingSample (GET /v3.4/stream/threat-feed/phishing/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamThreatFeedPhishingSample()
    println(result)
}

```

#### Stream the daily malware threat feed (CSV)

`GET /v3.4/stream/threat-feed/malware`

```kotlin
// Runnable example: Stream the daily malware threat feed (CSV) (GET /v3.4/stream/threat-feed/malware)
// Run it from the Getting Started project: gradle run -PmainClass=StreamThreatFeedMalwareKt
// Parameters for streamThreatFeedMalware (GET /v3.4/stream/threat-feed/malware):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamThreatFeedMalware(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream a sample of the malware threat feed (CSV)

`GET /v3.4/stream/threat-feed/malware/sample`

```kotlin
// Runnable example: Stream a sample of the malware threat feed (CSV) (GET /v3.4/stream/threat-feed/malware/sample)
// Run it from the Getting Started project: gradle run -PmainClass=StreamThreatFeedMalwareSampleKt
// Parameters for streamThreatFeedMalwareSample (GET /v3.4/stream/threat-feed/malware/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamThreatFeedMalwareSample()
    println(result)
}

```

#### Stream the daily spam threat feed (CSV)

`GET /v3.4/stream/threat-feed/spam`

```kotlin
// Runnable example: Stream the daily spam threat feed (CSV) (GET /v3.4/stream/threat-feed/spam)
// Run it from the Getting Started project: gradle run -PmainClass=StreamThreatFeedSpamKt
// Parameters for streamThreatFeedSpam (GET /v3.4/stream/threat-feed/spam):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamThreatFeedSpam(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream a sample of the spam threat feed (CSV)

`GET /v3.4/stream/threat-feed/spam/sample`

```kotlin
// Runnable example: Stream a sample of the spam threat feed (CSV) (GET /v3.4/stream/threat-feed/spam/sample)
// Run it from the Getting Started project: gradle run -PmainClass=StreamThreatFeedSpamSampleKt
// Parameters for streamThreatFeedSpamSample (GET /v3.4/stream/threat-feed/spam/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamThreatFeedSpamSample()
    println(result)
}

```

#### Stream newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/gtld`

```kotlin
// Runnable example: Stream newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/gtld)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerGtldKt
// Parameters for streamDomainerGtld (GET /v3.3/stream/domainer/gtld):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerGtld(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream cleaned newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/gtld/cleaned`

```kotlin
// Runnable example: Stream cleaned newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/gtld/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerGtldCleanedKt
// Parameters for streamDomainerGtldCleaned (GET /v3.3/stream/domainer/gtld/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerGtldCleaned(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream cleaned newly registered gTLD domains with an email (CSV)

`GET /v3.3/stream/domainer/gtld/cleaned/email`

```kotlin
// Runnable example: Stream cleaned newly registered gTLD domains with an email (CSV) (GET /v3.3/stream/domainer/gtld/cleaned/email)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerGtldCleanedEmailKt
// Parameters for streamDomainerGtldCleanedEmail (GET /v3.3/stream/domainer/gtld/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerGtldCleanedEmail(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream cleaned newly registered gTLD domains with a phone (CSV)

`GET /v3.3/stream/domainer/gtld/cleaned/phone`

```kotlin
// Runnable example: Stream cleaned newly registered gTLD domains with a phone (CSV) (GET /v3.3/stream/domainer/gtld/cleaned/phone)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerGtldCleanedPhoneKt
// Parameters for streamDomainerGtldCleanedPhone (GET /v3.3/stream/domainer/gtld/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerGtldCleanedPhone(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/cctld`

```kotlin
// Runnable example: Stream newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/cctld)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerCctldKt
// Parameters for streamDomainerCctld (GET /v3.3/stream/domainer/cctld):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerCctld(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream cleaned newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/cctld/cleaned`

```kotlin
// Runnable example: Stream cleaned newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/cctld/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerCctldCleanedKt
// Parameters for streamDomainerCctldCleaned (GET /v3.3/stream/domainer/cctld/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerCctldCleaned(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream cleaned newly registered ccTLD domains with an email (CSV)

`GET /v3.3/stream/domainer/cctld/cleaned/email`

```kotlin
// Runnable example: Stream cleaned newly registered ccTLD domains with an email (CSV) (GET /v3.3/stream/domainer/cctld/cleaned/email)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerCctldCleanedEmailKt
// Parameters for streamDomainerCctldCleanedEmail (GET /v3.3/stream/domainer/cctld/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerCctldCleanedEmail(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream cleaned newly registered ccTLD domains with a phone (CSV)

`GET /v3.3/stream/domainer/cctld/cleaned/phone`

```kotlin
// Runnable example: Stream cleaned newly registered ccTLD domains with a phone (CSV) (GET /v3.3/stream/domainer/cctld/cleaned/phone)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerCctldCleanedPhoneKt
// Parameters for streamDomainerCctldCleanedPhone (GET /v3.3/stream/domainer/cctld/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerCctldCleanedPhone(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream expiring domains (CSV)

`GET /v3.3/stream/domainer/expired`

```kotlin
// Runnable example: Stream expiring domains (CSV) (GET /v3.3/stream/domainer/expired)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerExpiredKt
// Parameters for streamDomainerExpired (GET /v3.3/stream/domainer/expired):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerExpired(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream cleaned expiring domains (CSV)

`GET /v3.3/stream/domainer/expired/cleaned`

```kotlin
// Runnable example: Stream cleaned expiring domains (CSV) (GET /v3.3/stream/domainer/expired/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerExpiredCleanedKt
// Parameters for streamDomainerExpiredCleaned (GET /v3.3/stream/domainer/expired/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerExpiredCleaned(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream cleaned expiring domains with an email (CSV)

`GET /v3.3/stream/domainer/expired/cleaned/email`

```kotlin
// Runnable example: Stream cleaned expiring domains with an email (CSV) (GET /v3.3/stream/domainer/expired/cleaned/email)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerExpiredCleanedEmailKt
// Parameters for streamDomainerExpiredCleanedEmail (GET /v3.3/stream/domainer/expired/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerExpiredCleanedEmail(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream cleaned expiring domains with a phone (CSV)

`GET /v3.3/stream/domainer/expired/cleaned/phone`

```kotlin
// Runnable example: Stream cleaned expiring domains with a phone (CSV) (GET /v3.3/stream/domainer/expired/cleaned/phone)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerExpiredCleanedPhoneKt
// Parameters for streamDomainerExpiredCleanedPhone (GET /v3.3/stream/domainer/expired/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerExpiredCleanedPhone(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream dropped domains (CSV)

`GET /v3.3/stream/domainer/dropped`

```kotlin
// Runnable example: Stream dropped domains (CSV) (GET /v3.3/stream/domainer/dropped)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerDroppedKt
// Parameters for streamDomainerDropped (GET /v3.3/stream/domainer/dropped):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerDropped(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream dropped domains with backlinks (CSV)

`GET /v3.3/stream/domainer/dropped/backlinks`

```kotlin
// Runnable example: Stream dropped domains with backlinks (CSV) (GET /v3.3/stream/domainer/dropped/backlinks)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerDroppedBacklinksKt
// Parameters for streamDomainerDroppedBacklinks (GET /v3.3/stream/domainer/dropped/backlinks):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerDroppedBacklinks(LocalDate.of(2026, 10, 1))
    println(result)
}

```

#### Stream a sample of newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/gtld`

```kotlin
// Runnable example: Stream a sample of newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/sample/gtld)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerGtldSampleKt
// Parameters for streamDomainerGtldSample (GET /v3.3/stream/domainer/sample/gtld):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerGtldSample()
    println(result)
}

```

#### Stream a sample of cleaned newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/gtld/cleaned`

```kotlin
// Runnable example: Stream a sample of cleaned newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/sample/gtld/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerGtldCleanedSampleKt
// Parameters for streamDomainerGtldCleanedSample (GET /v3.3/stream/domainer/sample/gtld/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerGtldCleanedSample()
    println(result)
}

```

#### Stream a sample of newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/cctld`

```kotlin
// Runnable example: Stream a sample of newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/sample/cctld)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerCctldSampleKt
// Parameters for streamDomainerCctldSample (GET /v3.3/stream/domainer/sample/cctld):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerCctldSample()
    println(result)
}

```

#### Stream a sample of cleaned newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/cctld/cleaned`

```kotlin
// Runnable example: Stream a sample of cleaned newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/sample/cctld/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerCctldCleanedSampleKt
// Parameters for streamDomainerCctldCleanedSample (GET /v3.3/stream/domainer/sample/cctld/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerCctldCleanedSample()
    println(result)
}

```

#### Stream a sample of expiring domains (CSV)

`GET /v3.3/stream/domainer/sample/expired`

```kotlin
// Runnable example: Stream a sample of expiring domains (CSV) (GET /v3.3/stream/domainer/sample/expired)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerExpiredSampleKt
// Parameters for streamDomainerExpiredSample (GET /v3.3/stream/domainer/sample/expired):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerExpiredSample()
    println(result)
}

```

#### Stream a sample of cleaned expiring domains (CSV)

`GET /v3.3/stream/domainer/sample/expired/cleaned`

```kotlin
// Runnable example: Stream a sample of cleaned expiring domains (CSV) (GET /v3.3/stream/domainer/sample/expired/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerExpiredCleanedSampleKt
// Parameters for streamDomainerExpiredCleanedSample (GET /v3.3/stream/domainer/sample/expired/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerExpiredCleanedSample()
    println(result)
}

```

#### Stream a sample of dropped domains (CSV)

`GET /v3.3/stream/domainer/sample/dropped`

```kotlin
// Runnable example: Stream a sample of dropped domains (CSV) (GET /v3.3/stream/domainer/sample/dropped)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerDroppedSampleKt
// Parameters for streamDomainerDroppedSample (GET /v3.3/stream/domainer/sample/dropped):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerDroppedSample()
    println(result)
}

```

#### Stream a sample of dropped domains with backlinks (CSV)

`GET /v3.3/stream/domainer/sample/dropped/backlinks`

```kotlin
// Runnable example: Stream a sample of dropped domains with backlinks (CSV) (GET /v3.3/stream/domainer/sample/dropped/backlinks)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerDroppedBacklinksSampleKt
// Parameters for streamDomainerDroppedBacklinksSample (GET /v3.3/stream/domainer/sample/dropped/backlinks):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerDroppedBacklinksSample()
    println(result)
}

```
