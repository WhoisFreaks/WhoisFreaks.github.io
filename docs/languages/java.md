# Java SDK

## About

The official **WhoisFreaks Java SDK**: a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from Java with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to Maven Central.

**Keywords:** java whois api, java whois sdk, whoisfreaks java, java domain lookup, java dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** Maven Central
- **Package:** `com.whoisfreaks:whoisfreaks`

## Install

```xml
<dependency>
  <groupId>com.whoisfreaks</groupId>
  <artifactId>whoisfreaks</artifactId>
  <version>0.24.0</version>
</dependency>
```

## Build from Source

Prefer to build the SDK yourself instead of installing from Maven Central? Clone the Java SDK repository and build it locally:

```bash
git clone https://github.com/WhoisFreaks/whoisfreaks-java
cd whoisfreaks-java
mvn clean install   # builds + installs to local ~/.m2
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

You need JDK 8 or later and Maven. Create the project directory:

```bash
mkdir -p whoisfreaks-test/src/main/java && cd whoisfreaks-test
```

Create `pom.xml`. The `exec.mainClass` property picks the class that `mvn exec:java` runs:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>whoisfreaks-test</artifactId>
  <version>1.0-SNAPSHOT</version>

  <properties>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <exec.mainClass>Main</exec.mainClass>
  </properties>

  <dependencies>
    <dependency>
      <groupId>com.whoisfreaks</groupId>
      <artifactId>whoisfreaks</artifactId>
      <version>0.24.0</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.0</version>
      </plugin>
    </plugins>
  </build>
</project>
```

Create `src/main/java/Main.java`:

```java
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.WhoisResponse;

public class Main {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call

        WhoisApi whois = new WhoisApi(client);
        // whoisLive(domainName, format); null format returns JSON
        WhoisResponse record = whois.whoisLive("whoisfreaks.com", null);
        System.out.println(record.getDomainName() + " expires " + record.getExpiryDate());
        System.out.println(record);
    }
}
```

Set your API key and run it:

```bash
export WHOISFREAKS_API_KEY="your_api_key"
mvn -q compile exec:java
```

To run one of the [runnable examples](../../examples/java/README.md), copy it into `src/main/java` and pass its class name, for example `mvn -q compile exec:java -Dexec.mainClass=WhoisLive`.

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

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

## Endpoints

All 60 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

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

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```java
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=BulkWhois
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkWhoisRequest;
import com.whoisfreaks.client.model.BulkWhoisResponse;

import java.util.Arrays;

public class BulkWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        WhoisApi api = new WhoisApi(client);

        BulkWhoisRequest body = new BulkWhoisRequest()
            .domainNames(Arrays.asList("whoisfreaks.com", "jfreaks.com"));
        // bulkWhois(bulkWhoisRequest, format); null leaves an optional parameter unset
        BulkWhoisResponse result = api.bulkWhois(body, null);
        System.out.println(result);
    }
}

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```java
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=WhoisHistory
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.WhoisHistoricalResponse;

public class WhoisHistory {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        WhoisApi api = new WhoisApi(client);

        // whoisHistory(domainName, format); null leaves an optional parameter unset
        WhoisHistoricalResponse result = api.whoisHistory("whoisfreaks.com", null);
        System.out.println(result);
    }
}

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```java
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=WhoisReverse
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.ReverseWhoisResponse;

public class WhoisReverse {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        WhoisApi api = new WhoisApi(client);

        // whoisReverse(keyword, page, format); null leaves an optional parameter unset
        ReverseWhoisResponse result = api.whoisReverse("whoisfreaks", 1, null);
        System.out.println(result);
    }
}

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```java
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsLive
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, optional)
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.DnsResponse;

public class DnsLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsLive(type, domainName, ipAddress, format); null leaves an optional parameter unset
        DnsResponse result = api.dnsLive("A,MX,TXT", "whoisfreaks.com", null, null);
        System.out.println(result);
    }
}

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```java
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsHistorical
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.HistoricalDnsResponse;

public class DnsHistorical {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsHistorical(domainName, type, page, format); null leaves an optional parameter unset
        HistoricalDnsResponse result = api.dnsHistorical("whoisfreaks.com", "A,MX,TXT", 1, null);
        System.out.println(result);
    }
}

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```java
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsReverse
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.ReverseDnsResponse;

public class DnsReverse {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsReverse(value, type, exact, page, format); null leaves an optional parameter unset
        ReverseDnsResponse result = api.dnsReverse("8.8.8.8", "a", null, 1, null);
        System.out.println(result);
    }
}

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```java
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsBulk
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkDnsResponse;
import com.whoisfreaks.client.model.DnsBulkRequest;

import java.util.Arrays;

public class DnsBulk {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        DnsBulkRequest body = new DnsBulkRequest()
            .domainNames(Arrays.asList("whoisfreaks.com", "example.com"));
        // dnsBulk(type, dnsBulkRequest, format); null leaves an optional parameter unset
        BulkDnsResponse result = api.dnsBulk("A,MX,TXT", body, null);
        System.out.println(result);
    }
}

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```java
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DomainAvailabilityV2
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DomainAvailabilityApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.DomainAvailabilityResponse;

public class DomainAvailabilityV2 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DomainAvailabilityApi api = new DomainAvailabilityApi(client);

        // domainAvailabilityV2(domain, sug, count, format); null leaves an optional parameter unset
        DomainAvailabilityResponse result = api.domainAvailabilityV2("google.com", true, 5, null);
        System.out.println(result);
    }
}

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```java
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=BulkDomainAvailabilityV2
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DomainAvailabilityApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkDomainAvailabilityRequest;
import com.whoisfreaks.client.model.BulkDomainAvailabilityResponse;

import java.util.Arrays;

public class BulkDomainAvailabilityV2 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DomainAvailabilityApi api = new DomainAvailabilityApi(client);

        BulkDomainAvailabilityRequest body = new BulkDomainAvailabilityRequest()
            .domainNames(Arrays.asList("whoisfreaks.com", "example.com"));
        // bulkDomainAvailabilityV2(bulkDomainAvailabilityRequest, domain, format); null leaves an optional parameter unset
        BulkDomainAvailabilityResponse result = api.bulkDomainAvailabilityV2(body, null, null);
        System.out.println(result);
    }
}

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```java
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=Typosquatting
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.TyposquattingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.TyposquattingResponse;

public class Typosquatting {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        TyposquattingApi api = new TyposquattingApi(client);

        // typosquatting(keyword, pattern, pageToken); null leaves an optional parameter unset
        TyposquattingResponse result = api.typosquatting("whoisfreaks", null, null);
        System.out.println(result);
    }
}

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```java
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=SslLookup
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.SslApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SslResponse;

public class SslLookup {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        SslApi api = new SslApi(client);

        // sslLookup(domainName, chain, sslRaw, format); null leaves an optional parameter unset
        SslResponse result = api.sslLookup("whoisfreaks.com", null, null, null);
        System.out.println(result);
    }
}

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```java
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=Geolocation
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.GeolocationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.GeolocationResponse;

public class Geolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        GeolocationApi api = new GeolocationApi(client);

        GeolocationResponse result = api.geolocation("8.8.8.8");
        System.out.println(result);
    }
}

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```java
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=BulkGeolocation
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.GeolocationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkGeolocationRequest;
import com.whoisfreaks.client.model.GeolocationResponse;

import java.util.Arrays;
import java.util.List;

public class BulkGeolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        GeolocationApi api = new GeolocationApi(client);

        BulkGeolocationRequest body = new BulkGeolocationRequest()
            .ips(Arrays.asList("8.8.8.8", "1.1.1.1"));
        List<GeolocationResponse> result = api.bulkGeolocation(body);
        System.out.println(result);
    }
}

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```java
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=Subdomains
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.SubdomainsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SubdomainsResponse;

public class Subdomains {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        SubdomainsApi api = new SubdomainsApi(client);

        // subdomains(domain, after, before, status, page, format); null leaves an optional parameter unset
        SubdomainsResponse result = api.subdomains("whoisfreaks.com", null, null, null, 1, null);
        System.out.println(result);
    }
}

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```java
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=IpReputation
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.IpReputationResponse;

public class IpReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        IpReputationApi api = new IpReputationApi(client);

        IpReputationResponse result = api.ipReputation("8.8.8.8");
        System.out.println(result);
    }
}

```

#### Bulk IP Reputation

`POST /v1.0/security`

```java
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=BulkIpReputation
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkGeolocationRequest;
import com.whoisfreaks.client.model.IpReputationResponse;

import java.util.Arrays;
import java.util.List;

public class BulkIpReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        IpReputationApi api = new IpReputationApi(client);

        BulkGeolocationRequest body = new BulkGeolocationRequest()
            .ips(Arrays.asList("8.8.8.8", "1.1.1.1"));
        List<IpReputationResponse> result = api.bulkIpReputation(body);
        System.out.println(result);
    }
}

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```java
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DomainReputation
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DomainReputationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.DomainReputationResponse;

public class DomainReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DomainReputationApi api = new DomainReputationApi(client);

        // domainReputation(domainName, format); null leaves an optional parameter unset
        DomainReputationResponse result = api.domainReputation("amazon.com", null);
        System.out.println(result);
    }
}

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```java
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=AsnWhois
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AsnWhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.AsnWhoisResponse;

public class AsnWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        AsnWhoisApi api = new AsnWhoisApi(client);

        // asnWhois(asn, format); null leaves an optional parameter unset
        AsnWhoisResponse result = api.asnWhois("as15169", null);
        System.out.println(result);
    }
}

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```java
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=IpWhois
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpWhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.IpWhoisResponse;

public class IpWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        IpWhoisApi api = new IpWhoisApi(client);

        // ipWhois(ip, format); null leaves an optional parameter unset
        IpWhoisResponse result = api.ipWhois("8.8.8.8", null);
        System.out.println(result);
    }
}

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```java
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=RotateApiKey
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AccountApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

public class RotateApiKey {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        AccountApi api = new AccountApi(client);

        String newKey = api.rotateApiKey();
        // The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.
        System.out.println("New API key: " + newKey);
    }
}

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```java
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=AccountUsage
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AccountApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.AccountUsageResponse;

public class AccountUsage {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        AccountApi api = new AccountApi(client);

        AccountUsageResponse result = api.accountUsage();
        System.out.println(result);
    }
}

```

#### Database File Status (Public)

`GET /v3.4/status`

```java
// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DatabaseFileStatus
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; no API key required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AccountApi;

public class DatabaseFileStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        AccountApi api = new AccountApi(client);

        com.whoisfreaks.client.model.DatabaseFileStatus result = api.databaseFileStatus();
        System.out.println(result);
    }
}

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```java
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbNewlyGtld
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbNewlyGtld {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);

        // dbNewlyGtld(whois, date, tlds); null leaves an optional parameter unset
        File download = api.dbNewlyGtld(true, LocalDate.of(2026, 10, 1), null);
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbNewlyGtld.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```java
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbNewlyCctld
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbNewlyCctld {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);

        // dbNewlyCctld(whois, date, tlds); null leaves an optional parameter unset
        File download = api.dbNewlyCctld(true, LocalDate.of(2026, 10, 1), null);
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbNewlyCctld.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```java
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbNewlyGtldCleaned
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbNewlyGtldCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);

        File download = api.dbNewlyGtldCleaned(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbNewlyGtldCleaned.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```java
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbNewlyCctldCleaned
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbNewlyCctldCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);

        File download = api.dbNewlyCctldCleaned(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbNewlyCctldCleaned.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```java
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbNewlyGtldJson
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;
import java.util.List;

public class DbNewlyGtldJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);

        // dbNewlyGtldJson(date, tlds); null leaves an optional parameter unset
        List<String> result = api.dbNewlyGtldJson(LocalDate.of(2026, 10, 1), null);
        System.out.println(result);
    }
}

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```java
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbNewlyCctldJson
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;
import java.util.List;

public class DbNewlyCctldJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);

        // dbNewlyCctldJson(date, tlds); null leaves an optional parameter unset
        List<String> result = api.dbNewlyCctldJson(LocalDate.of(2026, 10, 1), null);
        System.out.println(result);
    }
}

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```java
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbNewlyDns
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbNewlyDns {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);

        File download = api.dbNewlyDns(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbNewlyDns.json");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```java
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbExpired
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbExpired {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);

        File download = api.dbExpired(true, LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbExpired.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```java
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbExpiredCleaned
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbExpiredCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);

        File download = api.dbExpiredCleaned(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbExpiredCleaned.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```java
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbDropped
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbDropped {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);

        File download = api.dbDropped(true, LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbDropped.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```java
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbDroppedJson
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;
import java.util.List;

public class DbDroppedJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);

        // dbDroppedJson(date, tlds); null leaves an optional parameter unset
        List<String> result = api.dbDroppedJson(LocalDate.of(2026, 10, 1), null);
        System.out.println(result);
    }
}

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```java
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbDroppedBacklinks
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbDroppedBacklinks {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);

        // dbDroppedBacklinks(whois, date); null leaves an optional parameter unset
        File download = api.dbDroppedBacklinks(null, LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbDroppedBacklinks.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```java
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbWhoisDaily
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesWhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbWhoisDaily {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesWhoisApi api = new DatabasesWhoisApi(client);

        File download = api.dbWhoisDaily(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbWhoisDaily.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```java
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbWhoisWeekly
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesWhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbWhoisWeekly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesWhoisApi api = new DatabasesWhoisApi(client);

        File download = api.dbWhoisWeekly(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbWhoisWeekly.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```java
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbWhoisMonthly
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesWhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbWhoisMonthly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesWhoisApi api = new DatabasesWhoisApi(client);

        File download = api.dbWhoisMonthly(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbWhoisMonthly.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```java
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbDnsDaily
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesDnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbDnsDaily {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesDnsApi api = new DatabasesDnsApi(client);

        File download = api.dbDnsDaily(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbDnsDaily.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```java
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbDnsWeekly
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesDnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbDnsWeekly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesDnsApi api = new DatabasesDnsApi(client);

        File download = api.dbDnsWeekly(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbDnsWeekly.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```java
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbDnsMonthly
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesDnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbDnsMonthly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesDnsApi api = new DatabasesDnsApi(client);

        File download = api.dbDnsMonthly(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbDnsMonthly.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```java
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbSubdomainsDaily
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesSubdomainsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbSubdomainsDaily {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesSubdomainsApi api = new DatabasesSubdomainsApi(client);

        File download = api.dbSubdomainsDaily(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbSubdomainsDaily.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```java
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbSubdomainsWeekly
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesSubdomainsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbSubdomainsWeekly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesSubdomainsApi api = new DatabasesSubdomainsApi(client);

        File download = api.dbSubdomainsWeekly(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbSubdomainsWeekly.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```java
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbSubdomainsMonthly
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesSubdomainsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbSubdomainsMonthly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesSubdomainsApi api = new DatabasesSubdomainsApi(client);

        File download = api.dbSubdomainsMonthly(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbSubdomainsMonthly.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```java
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbIpCountryStatus
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SnapshotStatus;

public class DbIpCountryStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);

        SnapshotStatus result = api.dbIpCountryStatus();
        System.out.println(result);
    }
}

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```java
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbIpCountry
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbIpCountry {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);

        File download = api.dbIpCountry(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbIpCountry.zip");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```java
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbIpCityStatus
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SnapshotStatus;

public class DbIpCityStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);

        SnapshotStatus result = api.dbIpCityStatus();
        System.out.println(result);
    }
}

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```java
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbIpCity
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbIpCity {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);

        File download = api.dbIpCity(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbIpCity.zip");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```java
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbAsnWhois
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesAsnWhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbAsnWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesAsnWhoisApi api = new DatabasesAsnWhoisApi(client);

        File download = api.dbAsnWhois(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbAsnWhois.json.gz");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```java
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbAsnWhoisStatus
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesAsnWhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SnapshotStatus;

public class DbAsnWhoisStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesAsnWhoisApi api = new DatabasesAsnWhoisApi(client);

        SnapshotStatus result = api.dbAsnWhoisStatus();
        System.out.println(result);
    }
}

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```java
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbIpWhois
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpWhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbIpWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesIpWhoisApi api = new DatabasesIpWhoisApi(client);

        File download = api.dbIpWhois(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbIpWhois.json.gz");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```java
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbIpWhoisStatus
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpWhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SnapshotStatus;

public class DbIpWhoisStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesIpWhoisApi api = new DatabasesIpWhoisApi(client);

        SnapshotStatus result = api.dbIpWhoisStatus();
        System.out.println(result);
    }
}

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```java
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbIpSecurity
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpSecurityApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbIpSecurity {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesIpSecurityApi api = new DatabasesIpSecurityApi(client);

        File download = api.dbIpSecurity(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbIpSecurity.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```java
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbIpSecurityStatus
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpSecurityApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SnapshotStatus;

public class DbIpSecurityStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesIpSecurityApi api = new DatabasesIpSecurityApi(client);

        SnapshotStatus result = api.dbIpSecurityStatus();
        System.out.println(result);
    }
}

```

### Databases - Threat Feed

#### Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

```java
// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DownloadThreatFeedPhishing
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class DownloadThreatFeedPhishing {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);

        File download = api.downloadThreatFeedPhishing("2026-10-01");
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DownloadThreatFeedPhishing.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

```java
// Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DownloadThreatFeedPhishingSample
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class DownloadThreatFeedPhishingSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);

        File download = api.downloadThreatFeedPhishingSample();
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DownloadThreatFeedPhishingSample.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

```java
// Runnable example: Download the daily malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DownloadThreatFeedMalware
// Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class DownloadThreatFeedMalware {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);

        File download = api.downloadThreatFeedMalware("2026-10-01");
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DownloadThreatFeedMalware.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

```java
// Runnable example: Download a sample of the malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware/sample)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DownloadThreatFeedMalwareSample
// Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class DownloadThreatFeedMalwareSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);

        File download = api.downloadThreatFeedMalwareSample();
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DownloadThreatFeedMalwareSample.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

```java
// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DownloadThreatFeedSpam
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class DownloadThreatFeedSpam {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);

        File download = api.downloadThreatFeedSpam("2026-10-01");
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DownloadThreatFeedSpam.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```

#### Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

```java
// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DownloadThreatFeedSpamSample
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class DownloadThreatFeedSpamSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);

        File download = api.downloadThreatFeedSpamSample();
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DownloadThreatFeedSpamSample.csv");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}

```
