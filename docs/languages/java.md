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
//   - domainName (string, required): Domain to look up.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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

All 95 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```java
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=WhoisLive
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required): Domain to look up.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - domainName (string, optional): Domain to look up.
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - cnameDepth (integer, optional): How many CNAME links to follow before returning the records they point at. 0, the defau...
//   - relativeRecords (boolean, optional): Keeps the records picked up for other names along the way, such as a CNAME target's own...
//   - isAuthoritative (boolean, optional): Set true to read the records from the zone's own nameservers instead of a recursive res...
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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

        // dnsLive(type, domainName, ipAddress, cnameDepth, relativeRecords, isAuthoritative, format); null leaves an optional parameter unset
        DnsResponse result = api.dnsLive("A,MX,TXT", "whoisfreaks.com", null, null, null, null, null);
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
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): Set true to match value exactly. Defaults to false, where value is treated as a pattern...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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

#### Historical DNS Lookup (v2.2)

`GET /v2.2/dns/historical`

```java
// Runnable example: Historical DNS Lookup (v2.2) (GET /v2.2/dns/historical)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsHistoricalV22
// Parameters for dnsHistoricalV22 (GET /v2.2/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.HistoricalDnsResponseV2_2;

public class DnsHistoricalV22 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsHistoricalV22(domainName, type, page, sort, sortBy, format); null leaves an optional parameter unset
        HistoricalDnsResponseV2_2 result = api.dnsHistoricalV22("whoisfreaks.com", "A,MX,TXT", 1, null, null, null);
        System.out.println(result);
    }
}

```

#### Historical DNS Lookup (v2.3)

`GET /v2.3/dns/historical`

```java
// Runnable example: Historical DNS Lookup (v2.3) (GET /v2.3/dns/historical)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsHistoricalV23
// Parameters for dnsHistoricalV23 (GET /v2.3/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.HistoricalDnsResponseV2_2;

public class DnsHistoricalV23 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsHistoricalV23(domainName, type, page, sort, sortBy, format); null leaves an optional parameter unset
        HistoricalDnsResponseV2_2 result = api.dnsHistoricalV23("whoisfreaks.com", "A,MX,TXT", 1, null, null, null);
        System.out.println(result);
    }
}

```

#### Reverse DNS Lookup (v2.2)

`GET /v2.2/dns/reverse`

```java
// Runnable example: Reverse DNS Lookup (v2.2) (GET /v2.2/dns/reverse)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsReverseV22
// Parameters for dnsReverseV22 (GET /v2.2/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): When false the value is matched as a substring, which is far slower than an exact match...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.ReverseDnsResponseV2_2;

public class DnsReverseV22 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsReverseV22(value, type, exact, page, sort, sortBy, format); null leaves an optional parameter unset
        ReverseDnsResponseV2_2 result = api.dnsReverseV22("8.8.8.8", "a", null, 1, null, null, null);
        System.out.println(result);
    }
}

```

#### Reverse DNS Lookup (v2.3)

`GET /v2.3/dns/reverse`

```java
// Runnable example: Reverse DNS Lookup (v2.3) (GET /v2.3/dns/reverse)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsReverseV23
// Parameters for dnsReverseV23 (GET /v2.3/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): When false the value is matched as a substring, which is far slower than an exact match...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.ReverseDnsResponseV2_3;

public class DnsReverseV23 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsReverseV23(value, type, exact, page, sort, sortBy, format); null leaves an optional parameter unset
        ReverseDnsResponseV2_3 result = api.dnsReverseV23("8.8.8.8", "a", null, 1, null, null, null);
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
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - cname_depth (integer, optional): How many CNAME links to follow before returning the records they point at. 0, the defau...
//   - isAuthoritative (boolean, optional): Set true to read the records from each zone's own nameservers instead of a recursive re...
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
        // dnsBulk(type, dnsBulkRequest, cname_depth, isAuthoritative, format); null leaves an optional parameter unset
        BulkDnsResponse result = api.dnsBulk("A,MX,TXT", body, null, null, null);
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
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - keyword (string, optional): Brand or label to find typo variants for. Pass either keyword or pattern, not both.
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters. Pass either keyword or patter...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
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

#### Subdomain Typosquatting Lookup

`GET /v3.0/subdomains/typos`

```java
// Runnable example: Subdomain Typosquatting Lookup (GET /v3.0/subdomains/typos)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=SubdomainTyposquatting
// Parameters for subdomainTyposquatting (GET /v3.0/subdomains/typos):
//   - keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits and hyphe...
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one. At most 2...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
//   - fetch_size (integer, optional): Subdomains per page. 100 when the parameter is left out, and values above 10000 are cap...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.TyposquattingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.TyposquatSubdomainsResponse;

public class SubdomainTyposquatting {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        TyposquattingApi api = new TyposquattingApi(client);

        // subdomainTyposquatting(keyword, pattern, pageToken, fetch_size); null leaves an optional parameter unset
        TyposquatSubdomainsResponse result = api.subdomainTyposquatting("paypal", null, null, null);
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
//   - domainName (string, required): Domain to look up.
//   - chain (boolean, optional): Set true to return the full certificate chain, ordered from the end-user certificate to...
//   - sslRaw (boolean, optional): Set true to include the raw OpenSSL response for the domain. Defaults to false.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - ip (string, required): IP address to look up.
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
//   - domain (string, required): Domain whose subdomains you want.
//   - after (string, optional): Only return records created after this date, in YYYY-MM-DD format. Defaults to the olde...
//   - before (string, optional): Only return records created before this date, in YYYY-MM-DD format. Defaults to today, ...
//   - status (string (one of: active, inactive), optional): Limit results to active or inactive subdomains. Both are returned when the parameter is...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - ip (string, required): IP address to look up.
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

#### IP Reputation Lookup (v2.0)

`GET /v2.0/security`

```java
// Runnable example: IP Reputation Lookup (v2.0) (GET /v2.0/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=IpReputationV2
// Parameters for ipReputationV2 (GET /v2.0/security):
//   - ip (string, required): IP address to look up.
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.IpReputationResponse;

public class IpReputationV2 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        IpReputationApi api = new IpReputationApi(client);

        IpReputationResponse result = api.ipReputationV2("8.8.8.8");
        System.out.println(result);
    }
}

```

#### Bulk IP Reputation (v2.0)

`POST /v2.0/security`

```java
// Runnable example: Bulk IP Reputation (v2.0) (POST /v2.0/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=BulkIpReputationV2
// Parameters for bulkIpReputationV2 (POST /v2.0/security):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkGeolocationRequest;
import com.whoisfreaks.client.model.IpReputationResponse;

import java.util.Arrays;
import java.util.List;

public class BulkIpReputationV2 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        IpReputationApi api = new IpReputationApi(client);

        BulkGeolocationRequest body = new BulkGeolocationRequest()
            .ips(Arrays.asList("1.1.1.1", "2.2.2.2", "8.8.8.8"));
        List<IpReputationResponse> result = api.bulkIpReputationV2(body);
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
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - asn (string, required): Autonomous system number to look up, with or without the AS prefix.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - ip (string, required): IP address to look up.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
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
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
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
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
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
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
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
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
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
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
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
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
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
//   - whois (boolean, optional): Set true for the file with full WHOIS records, false for domain names only.
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
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
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
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
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
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
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
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
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
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
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

### Databases - Streaming

#### Stream the daily phishing threat feed (CSV)

`GET /v3.4/stream/threat-feed/phishing`

```java
// Runnable example: Stream the daily phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamThreatFeedPhishing
// Parameters for streamThreatFeedPhishing (GET /v3.4/stream/threat-feed/phishing):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamThreatFeedPhishing {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamThreatFeedPhishing(date, offset, limit); null leaves an optional parameter unset
        String result = api.streamThreatFeedPhishing(LocalDate.of(2026, 10, 1), null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of the phishing threat feed (CSV)

`GET /v3.4/stream/threat-feed/phishing/sample`

```java
// Runnable example: Stream a sample of the phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing/sample)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamThreatFeedPhishingSample
// Parameters for streamThreatFeedPhishingSample (GET /v3.4/stream/threat-feed/phishing/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamThreatFeedPhishingSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamThreatFeedPhishingSample(offset, limit); null leaves an optional parameter unset
        String result = api.streamThreatFeedPhishingSample(null, null);
        System.out.println(result);
    }
}

```

#### Stream the daily malware threat feed (CSV)

`GET /v3.4/stream/threat-feed/malware`

```java
// Runnable example: Stream the daily malware threat feed (CSV) (GET /v3.4/stream/threat-feed/malware)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamThreatFeedMalware
// Parameters for streamThreatFeedMalware (GET /v3.4/stream/threat-feed/malware):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamThreatFeedMalware {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamThreatFeedMalware(date, offset, limit); null leaves an optional parameter unset
        String result = api.streamThreatFeedMalware(LocalDate.of(2026, 10, 1), null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of the malware threat feed (CSV)

`GET /v3.4/stream/threat-feed/malware/sample`

```java
// Runnable example: Stream a sample of the malware threat feed (CSV) (GET /v3.4/stream/threat-feed/malware/sample)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamThreatFeedMalwareSample
// Parameters for streamThreatFeedMalwareSample (GET /v3.4/stream/threat-feed/malware/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamThreatFeedMalwareSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamThreatFeedMalwareSample(offset, limit); null leaves an optional parameter unset
        String result = api.streamThreatFeedMalwareSample(null, null);
        System.out.println(result);
    }
}

```

#### Stream the daily spam threat feed (CSV)

`GET /v3.4/stream/threat-feed/spam`

```java
// Runnable example: Stream the daily spam threat feed (CSV) (GET /v3.4/stream/threat-feed/spam)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamThreatFeedSpam
// Parameters for streamThreatFeedSpam (GET /v3.4/stream/threat-feed/spam):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamThreatFeedSpam {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamThreatFeedSpam(date, offset, limit); null leaves an optional parameter unset
        String result = api.streamThreatFeedSpam(LocalDate.of(2026, 10, 1), null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of the spam threat feed (CSV)

`GET /v3.4/stream/threat-feed/spam/sample`

```java
// Runnable example: Stream a sample of the spam threat feed (CSV) (GET /v3.4/stream/threat-feed/spam/sample)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamThreatFeedSpamSample
// Parameters for streamThreatFeedSpamSample (GET /v3.4/stream/threat-feed/spam/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamThreatFeedSpamSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamThreatFeedSpamSample(offset, limit); null leaves an optional parameter unset
        String result = api.streamThreatFeedSpamSample(null, null);
        System.out.println(result);
    }
}

```

#### Stream newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/gtld`

```java
// Runnable example: Stream newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/gtld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerGtld
// Parameters for streamDomainerGtld (GET /v3.3/stream/domainer/gtld):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerGtld {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerGtld(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerGtld(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream cleaned newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/gtld/cleaned`

```java
// Runnable example: Stream cleaned newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/gtld/cleaned)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerGtldCleaned
// Parameters for streamDomainerGtldCleaned (GET /v3.3/stream/domainer/gtld/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerGtldCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerGtldCleaned(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerGtldCleaned(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream cleaned newly registered gTLD domains with an email (CSV)

`GET /v3.3/stream/domainer/gtld/cleaned/email`

```java
// Runnable example: Stream cleaned newly registered gTLD domains with an email (CSV) (GET /v3.3/stream/domainer/gtld/cleaned/email)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerGtldCleanedEmail
// Parameters for streamDomainerGtldCleanedEmail (GET /v3.3/stream/domainer/gtld/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerGtldCleanedEmail {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerGtldCleanedEmail(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerGtldCleanedEmail(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream cleaned newly registered gTLD domains with a phone (CSV)

`GET /v3.3/stream/domainer/gtld/cleaned/phone`

```java
// Runnable example: Stream cleaned newly registered gTLD domains with a phone (CSV) (GET /v3.3/stream/domainer/gtld/cleaned/phone)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerGtldCleanedPhone
// Parameters for streamDomainerGtldCleanedPhone (GET /v3.3/stream/domainer/gtld/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerGtldCleanedPhone {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerGtldCleanedPhone(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerGtldCleanedPhone(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/cctld`

```java
// Runnable example: Stream newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/cctld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerCctld
// Parameters for streamDomainerCctld (GET /v3.3/stream/domainer/cctld):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerCctld {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerCctld(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerCctld(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream cleaned newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/cctld/cleaned`

```java
// Runnable example: Stream cleaned newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/cctld/cleaned)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerCctldCleaned
// Parameters for streamDomainerCctldCleaned (GET /v3.3/stream/domainer/cctld/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerCctldCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerCctldCleaned(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerCctldCleaned(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream cleaned newly registered ccTLD domains with an email (CSV)

`GET /v3.3/stream/domainer/cctld/cleaned/email`

```java
// Runnable example: Stream cleaned newly registered ccTLD domains with an email (CSV) (GET /v3.3/stream/domainer/cctld/cleaned/email)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerCctldCleanedEmail
// Parameters for streamDomainerCctldCleanedEmail (GET /v3.3/stream/domainer/cctld/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerCctldCleanedEmail {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerCctldCleanedEmail(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerCctldCleanedEmail(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream cleaned newly registered ccTLD domains with a phone (CSV)

`GET /v3.3/stream/domainer/cctld/cleaned/phone`

```java
// Runnable example: Stream cleaned newly registered ccTLD domains with a phone (CSV) (GET /v3.3/stream/domainer/cctld/cleaned/phone)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerCctldCleanedPhone
// Parameters for streamDomainerCctldCleanedPhone (GET /v3.3/stream/domainer/cctld/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerCctldCleanedPhone {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerCctldCleanedPhone(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerCctldCleanedPhone(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream expiring domains (CSV)

`GET /v3.3/stream/domainer/expired`

```java
// Runnable example: Stream expiring domains (CSV) (GET /v3.3/stream/domainer/expired)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerExpired
// Parameters for streamDomainerExpired (GET /v3.3/stream/domainer/expired):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerExpired {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerExpired(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerExpired(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream cleaned expiring domains (CSV)

`GET /v3.3/stream/domainer/expired/cleaned`

```java
// Runnable example: Stream cleaned expiring domains (CSV) (GET /v3.3/stream/domainer/expired/cleaned)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerExpiredCleaned
// Parameters for streamDomainerExpiredCleaned (GET /v3.3/stream/domainer/expired/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerExpiredCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerExpiredCleaned(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerExpiredCleaned(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream cleaned expiring domains with an email (CSV)

`GET /v3.3/stream/domainer/expired/cleaned/email`

```java
// Runnable example: Stream cleaned expiring domains with an email (CSV) (GET /v3.3/stream/domainer/expired/cleaned/email)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerExpiredCleanedEmail
// Parameters for streamDomainerExpiredCleanedEmail (GET /v3.3/stream/domainer/expired/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerExpiredCleanedEmail {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerExpiredCleanedEmail(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerExpiredCleanedEmail(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream cleaned expiring domains with a phone (CSV)

`GET /v3.3/stream/domainer/expired/cleaned/phone`

```java
// Runnable example: Stream cleaned expiring domains with a phone (CSV) (GET /v3.3/stream/domainer/expired/cleaned/phone)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerExpiredCleanedPhone
// Parameters for streamDomainerExpiredCleanedPhone (GET /v3.3/stream/domainer/expired/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerExpiredCleanedPhone {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerExpiredCleanedPhone(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerExpiredCleanedPhone(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream dropped domains (CSV)

`GET /v3.3/stream/domainer/dropped`

```java
// Runnable example: Stream dropped domains (CSV) (GET /v3.3/stream/domainer/dropped)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerDropped
// Parameters for streamDomainerDropped (GET /v3.3/stream/domainer/dropped):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerDropped {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerDropped(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerDropped(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream dropped domains with backlinks (CSV)

`GET /v3.3/stream/domainer/dropped/backlinks`

```java
// Runnable example: Stream dropped domains with backlinks (CSV) (GET /v3.3/stream/domainer/dropped/backlinks)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerDroppedBacklinks
// Parameters for streamDomainerDroppedBacklinks (GET /v3.3/stream/domainer/dropped/backlinks):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerDroppedBacklinks {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerDroppedBacklinks(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerDroppedBacklinks(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/gtld`

```java
// Runnable example: Stream a sample of newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/sample/gtld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerGtldSample
// Parameters for streamDomainerGtldSample (GET /v3.3/stream/domainer/sample/gtld):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamDomainerGtldSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerGtldSample(whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerGtldSample(null, null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of cleaned newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/gtld/cleaned`

```java
// Runnable example: Stream a sample of cleaned newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/sample/gtld/cleaned)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerGtldCleanedSample
// Parameters for streamDomainerGtldCleanedSample (GET /v3.3/stream/domainer/sample/gtld/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamDomainerGtldCleanedSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerGtldCleanedSample(whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerGtldCleanedSample(null, null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/cctld`

```java
// Runnable example: Stream a sample of newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/sample/cctld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerCctldSample
// Parameters for streamDomainerCctldSample (GET /v3.3/stream/domainer/sample/cctld):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamDomainerCctldSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerCctldSample(whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerCctldSample(null, null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of cleaned newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/cctld/cleaned`

```java
// Runnable example: Stream a sample of cleaned newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/sample/cctld/cleaned)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerCctldCleanedSample
// Parameters for streamDomainerCctldCleanedSample (GET /v3.3/stream/domainer/sample/cctld/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamDomainerCctldCleanedSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerCctldCleanedSample(whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerCctldCleanedSample(null, null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of expiring domains (CSV)

`GET /v3.3/stream/domainer/sample/expired`

```java
// Runnable example: Stream a sample of expiring domains (CSV) (GET /v3.3/stream/domainer/sample/expired)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerExpiredSample
// Parameters for streamDomainerExpiredSample (GET /v3.3/stream/domainer/sample/expired):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamDomainerExpiredSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerExpiredSample(whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerExpiredSample(null, null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of cleaned expiring domains (CSV)

`GET /v3.3/stream/domainer/sample/expired/cleaned`

```java
// Runnable example: Stream a sample of cleaned expiring domains (CSV) (GET /v3.3/stream/domainer/sample/expired/cleaned)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerExpiredCleanedSample
// Parameters for streamDomainerExpiredCleanedSample (GET /v3.3/stream/domainer/sample/expired/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamDomainerExpiredCleanedSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerExpiredCleanedSample(whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerExpiredCleanedSample(null, null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of dropped domains (CSV)

`GET /v3.3/stream/domainer/sample/dropped`

```java
// Runnable example: Stream a sample of dropped domains (CSV) (GET /v3.3/stream/domainer/sample/dropped)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerDroppedSample
// Parameters for streamDomainerDroppedSample (GET /v3.3/stream/domainer/sample/dropped):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamDomainerDroppedSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerDroppedSample(whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerDroppedSample(null, null, null);
        System.out.println(result);
    }
}

```

#### Stream a sample of dropped domains with backlinks (CSV)

`GET /v3.3/stream/domainer/sample/dropped/backlinks`

```java
// Runnable example: Stream a sample of dropped domains with backlinks (CSV) (GET /v3.3/stream/domainer/sample/dropped/backlinks)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerDroppedBacklinksSample
// Parameters for streamDomainerDroppedBacklinksSample (GET /v3.3/stream/domainer/sample/dropped/backlinks):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamDomainerDroppedBacklinksSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerDroppedBacklinksSample(whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerDroppedBacklinksSample(null, null, null);
        System.out.println(result);
    }
}

```
