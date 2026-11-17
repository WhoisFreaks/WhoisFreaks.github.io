# C# / .NET SDK

## About

The official **WhoisFreaks C# / .NET SDK**: a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from C# / .NET with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to NuGet.

**Keywords:** c# / .net whois api, c# / .net whois sdk, whoisfreaks c# / .net, c# / .net domain lookup, c# / .net dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** NuGet
- **Package:** `WhoisFreaks`

## Install

```bash
dotnet add package WhoisFreaks
```

## Build from Source

Prefer to build the SDK yourself instead of installing from NuGet? Clone the C# / .NET SDK repository and build it locally:

```bash
git clone https://github.com/WhoisFreaks/whoisfreaks-csharp
cd whoisfreaks-csharp
dotnet build   # or: dotnet pack -c Release
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

You need the .NET 8 SDK or later. Create a console app and add the package:

```bash
dotnet new console -o whoisfreaks-test
cd whoisfreaks-test
dotnet add package WhoisFreaks --version 0.24.0
```

Replace `Program.cs` with:

```csharp
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call

var whois = new WHOISApi(config);
WhoisResponse record = whois.WhoisLive("whoisfreaks.com");
Console.WriteLine($"{record.DomainName} expires {record.ExpiryDate}");
Console.WriteLine(record.ToJson());
```

Set your API key and run it:

```bash
export WHOISFREAKS_API_KEY="your_api_key"
dotnet run
```

To run one of the [runnable examples](../../examples/csharp/README.md), use it as `Program.cs` and run `dotnet run` again.

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```csharp
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required): Domain to look up.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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

## Endpoints

All 95 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```csharp
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required): Domain to look up.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```csharp
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
//   - body: BulkWhoisRequest (required): request body object
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new WHOISApi(config);

var body = new BulkWhoisRequest(domainNames: new List<string> { "whoisfreaks.com", "jfreaks.com" });
BulkWhoisResponse result = api.BulkWhois(body);
Console.WriteLine(result.ToJson());

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```csharp
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new WHOISApi(config);

WhoisHistoricalResponse result = api.WhoisHistory("whoisfreaks.com");
Console.WriteLine(result.ToJson());

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```csharp
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new WHOISApi(config);

ReverseWhoisResponse result = api.WhoisReverse("whoisfreaks", page: 1);
Console.WriteLine(result.ToJson());

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```csharp
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, optional): Domain to look up.
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - cnameDepth (integer, optional): How many CNAME links to follow before returning the records they point at. 0, the defau...
//   - relativeRecords (boolean, optional): Keeps the records picked up for other names along the way, such as a CNAME target's own...
//   - isAuthoritative (boolean, optional): Set true to read the records from the zone's own nameservers instead of a recursive res...
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DNSApi(config);

DnsResponse result = api.DnsLive("A,MX,TXT", domainName: "whoisfreaks.com");
Console.WriteLine(result.ToJson());

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```csharp
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DNSApi(config);

HistoricalDnsResponse result = api.DnsHistorical("whoisfreaks.com", "A,MX,TXT", page: 1);
Console.WriteLine(result.ToJson());

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```csharp
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): Set true to match value exactly. Defaults to false, where value is treated as a pattern...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DNSApi(config);

ReverseDnsResponse result = api.DnsReverse("8.8.8.8", "a", page: 1);
Console.WriteLine(result.ToJson());

```

#### Historical DNS Lookup (v2.2)

`GET /v2.2/dns/historical`

```csharp
// Runnable example: Historical DNS Lookup (v2.2) (GET /v2.2/dns/historical)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsHistoricalV22 (GET /v2.2/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DNSApi(config);

HistoricalDnsResponseV2_2 result = api.DnsHistoricalV22("whoisfreaks.com", "A,MX,TXT", page: 1);
Console.WriteLine(result.ToJson());

```

#### Historical DNS Lookup (v2.3)

`GET /v2.3/dns/historical`

```csharp
// Runnable example: Historical DNS Lookup (v2.3) (GET /v2.3/dns/historical)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsHistoricalV23 (GET /v2.3/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DNSApi(config);

HistoricalDnsResponseV2_2 result = api.DnsHistoricalV23("whoisfreaks.com", "A,MX,TXT", page: 1);
Console.WriteLine(result.ToJson());

```

#### Reverse DNS Lookup (v2.2)

`GET /v2.2/dns/reverse`

```csharp
// Runnable example: Reverse DNS Lookup (v2.2) (GET /v2.2/dns/reverse)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsReverseV22 (GET /v2.2/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): When false the value is matched as a substring, which is far slower than an exact match...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DNSApi(config);

ReverseDnsResponseV2_2 result = api.DnsReverseV22("8.8.8.8", "a", page: 1);
Console.WriteLine(result.ToJson());

```

#### Reverse DNS Lookup (v2.3)

`GET /v2.3/dns/reverse`

```csharp
// Runnable example: Reverse DNS Lookup (v2.3) (GET /v2.3/dns/reverse)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsReverseV23 (GET /v2.3/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required): DNS record type to search by.
//   - exact (boolean, optional): When false the value is matched as a substring, which is far slower than an exact match...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DNSApi(config);

ReverseDnsResponseV2_3 result = api.DnsReverseV23("8.8.8.8", "a", page: 1);
Console.WriteLine(result.ToJson());

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```csharp
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - cname_depth (integer, optional): How many CNAME links to follow before returning the records they point at. 0, the defau...
//   - isAuthoritative (boolean, optional): Set true to read the records from each zone's own nameservers instead of a recursive re...
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
//   - body: DnsBulkRequest (required): request body object
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DNSApi(config);

var body = new DnsBulkRequest(domainNames: new List<string> { "whoisfreaks.com", "example.com" });
BulkDnsResponse result = api.DnsBulk("A,MX,TXT", body);
Console.WriteLine(result.ToJson());

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```csharp
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DomainAvailabilityApi(config);

DomainAvailabilityResponse result = api.DomainAvailabilityV2("google.com", sug: true, count: 5);
Console.WriteLine(result.ToJson());

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```csharp
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
//   - body: BulkDomainAvailabilityRequest (required): request body object
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DomainAvailabilityApi(config);

var body = new BulkDomainAvailabilityRequest(domainNames: new List<string> { "whoisfreaks.com", "example.com" });
BulkDomainAvailabilityResponse result = api.BulkDomainAvailabilityV2(body);
Console.WriteLine(result.ToJson());

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```csharp
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional): Brand or label to find typo variants for. Pass either keyword or pattern, not both.
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters. Pass either keyword or patter...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new TyposquattingApi(config);

TyposquattingResponse result = api.Typosquatting(keyword: "whoisfreaks");
Console.WriteLine(result.ToJson());

```

#### Subdomain Typosquatting Lookup

`GET /v3.0/subdomains/typos`

```csharp
// Runnable example: Subdomain Typosquatting Lookup (GET /v3.0/subdomains/typos)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for subdomainTyposquatting (GET /v3.0/subdomains/typos):
//   - keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits and hyphe...
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one. At most 2...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
//   - fetch_size (integer, optional): Subdomains per page. 100 when the parameter is left out, and values above 10000 are cap...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new TyposquattingApi(config);

TyposquatSubdomainsResponse result = api.SubdomainTyposquatting(keyword: "paypal");
Console.WriteLine(result.ToJson());

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```csharp
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required): Domain to look up.
//   - chain (boolean, optional): Set true to return the full certificate chain, ordered from the end-user certificate to...
//   - sslRaw (boolean, optional): Set true to include the raw OpenSSL response for the domain. Defaults to false.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new SSLApi(config);

SslResponse result = api.SslLookup("whoisfreaks.com");
Console.WriteLine(result.ToJson());

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```csharp
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required): IP address to look up.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new GeolocationApi(config);

GeolocationResponse result = api.Geolocation("8.8.8.8");
Console.WriteLine(result.ToJson());

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```csharp
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required): request body object
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new GeolocationApi(config);

var body = new BulkGeolocationRequest(ips: new List<string> { "8.8.8.8", "1.1.1.1" });
List<GeolocationResponse> result = api.BulkGeolocation(body);
foreach (var item in result)
{
    Console.WriteLine(item.ToJson());
}

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```csharp
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required): Domain whose subdomains you want.
//   - after (string, optional): Only return records created after this date, in YYYY-MM-DD format. Defaults to the olde...
//   - before (string, optional): Only return records created before this date, in YYYY-MM-DD format. Defaults to today, ...
//   - status (string (one of: active, inactive), optional): Limit results to active or inactive subdomains. Both are returned when the parameter is...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new SubdomainsApi(config);

SubdomainsResponse result = api.Subdomains("whoisfreaks.com", page: 1);
Console.WriteLine(result.ToJson());

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```csharp
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required): IP address to look up.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new IPReputationApi(config);

IpReputationResponse result = api.IpReputation("8.8.8.8");
Console.WriteLine(result.ToJson());

```

#### Bulk IP Reputation

`POST /v1.0/security`

```csharp
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkGeolocationRequest (required): request body object
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new IPReputationApi(config);

var body = new BulkGeolocationRequest(ips: new List<string> { "8.8.8.8", "1.1.1.1" });
List<IpReputationResponse> result = api.BulkIpReputation(body);
foreach (var item in result)
{
    Console.WriteLine(item.ToJson());
}

```

#### IP Reputation Lookup (v2.0)

`GET /v2.0/security`

```csharp
// Runnable example: IP Reputation Lookup (v2.0) (GET /v2.0/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for ipReputationV2 (GET /v2.0/security):
//   - ip (string, required): IP address to look up.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new IPReputationApi(config);

IpReputationResponse result = api.IpReputationV2("8.8.8.8");
Console.WriteLine(result.ToJson());

```

#### Bulk IP Reputation (v2.0)

`POST /v2.0/security`

```csharp
// Runnable example: Bulk IP Reputation (v2.0) (POST /v2.0/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for bulkIpReputationV2 (POST /v2.0/security):
//   - body: BulkGeolocationRequest (required): request body object
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new IPReputationApi(config);

var body = new BulkGeolocationRequest(ips: new List<string> { "1.1.1.1", "2.2.2.2", "8.8.8.8" });
List<IpReputationResponse> result = api.BulkIpReputationV2(body);
foreach (var item in result)
{
    Console.WriteLine(item.ToJson());
}

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```csharp
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DomainReputationApi(config);

DomainReputationResponse result = api.DomainReputation("amazon.com");
Console.WriteLine(result.ToJson());

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```csharp
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required): Autonomous system number to look up, with or without the AS prefix.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new ASNWHOISApi(config);

AsnWhoisResponse result = api.AsnWhois("as15169");
Console.WriteLine(result.ToJson());

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```csharp
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required): IP address to look up.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new IPWHOISApi(config);

IpWhoisResponse result = api.IpWhois("8.8.8.8");
Console.WriteLine(result.ToJson());

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```csharp
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new AccountApi(config);

string newKey = api.RotateApiKey();
// The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.
Console.WriteLine($"New API key: {newKey}");

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```csharp
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new AccountApi(config);

AccountUsageResponse result = api.AccountUsage();
Console.WriteLine(result.ToJson());

```

#### Database File Status (Public)

`GET /v3.4/status`

```csharp
// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; no API key required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new AccountApi(config);

DatabaseFileStatus result = api.DatabaseFileStatus();
Console.WriteLine(result.ToJson());

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```csharp
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesNewlyRegisteredApi(config);

FileParameter download = api.DbNewlyGtld(true, date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbNewlyGtld.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```csharp
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesNewlyRegisteredApi(config);

FileParameter download = api.DbNewlyCctld(true, date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbNewlyCctld.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```csharp
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesNewlyRegisteredApi(config);

FileParameter download = api.DbNewlyGtldCleaned(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbNewlyGtldCleaned.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```csharp
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesNewlyRegisteredApi(config);

FileParameter download = api.DbNewlyCctldCleaned(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbNewlyCctldCleaned.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```csharp
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesNewlyRegisteredApi(config);

List<string> result = api.DbNewlyGtldJson(date: new DateOnly(2026, 10, 1));
foreach (var item in result)
{
    Console.WriteLine(item);
}

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```csharp
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesNewlyRegisteredApi(config);

List<string> result = api.DbNewlyCctldJson(date: new DateOnly(2026, 10, 1));
foreach (var item in result)
{
    Console.WriteLine(item);
}

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```csharp
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesNewlyRegisteredApi(config);

FileParameter download = api.DbNewlyDns(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbNewlyDns.json");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```csharp
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesExpiringDroppedApi(config);

FileParameter download = api.DbExpired(true, date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbExpired.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```csharp
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesExpiringDroppedApi(config);

FileParameter download = api.DbExpiredCleaned(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbExpiredCleaned.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```csharp
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesExpiringDroppedApi(config);

FileParameter download = api.DbDropped(true, date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbDropped.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```csharp
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesExpiringDroppedApi(config);

List<string> result = api.DbDroppedJson(date: new DateOnly(2026, 10, 1));
foreach (var item in result)
{
    Console.WriteLine(item);
}

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```csharp
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesExpiringDroppedApi(config);

FileParameter download = api.DbDroppedBacklinks(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbDroppedBacklinks.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```csharp
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesWHOISApi(config);

FileParameter download = api.DbWhoisDaily(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbWhoisDaily.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```csharp
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesWHOISApi(config);

FileParameter download = api.DbWhoisWeekly(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbWhoisWeekly.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```csharp
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesWHOISApi(config);

FileParameter download = api.DbWhoisMonthly(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbWhoisMonthly.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```csharp
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesDNSApi(config);

FileParameter download = api.DbDnsDaily(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbDnsDaily.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```csharp
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesDNSApi(config);

FileParameter download = api.DbDnsWeekly(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbDnsWeekly.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```csharp
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesDNSApi(config);

FileParameter download = api.DbDnsMonthly(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbDnsMonthly.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```csharp
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesSubdomainsApi(config);

FileParameter download = api.DbSubdomainsDaily(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbSubdomainsDaily.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```csharp
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesSubdomainsApi(config);

FileParameter download = api.DbSubdomainsWeekly(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbSubdomainsWeekly.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```csharp
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesSubdomainsApi(config);

FileParameter download = api.DbSubdomainsMonthly(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbSubdomainsMonthly.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```csharp
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesIPGeolocationApi(config);

SnapshotStatus result = api.DbIpCountryStatus();
Console.WriteLine(result.ToJson());

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```csharp
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesIPGeolocationApi(config);

FileParameter download = api.DbIpCountry(new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbIpCountry.zip");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```csharp
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesIPGeolocationApi(config);

SnapshotStatus result = api.DbIpCityStatus();
Console.WriteLine(result.ToJson());

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```csharp
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesIPGeolocationApi(config);

FileParameter download = api.DbIpCity(new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbIpCity.zip");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```csharp
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesASNWHOISApi(config);

FileParameter download = api.DbAsnWhois(new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbAsnWhois.json.gz");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```csharp
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesASNWHOISApi(config);

SnapshotStatus result = api.DbAsnWhoisStatus();
Console.WriteLine(result.ToJson());

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```csharp
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesIPWHOISApi(config);

FileParameter download = api.DbIpWhois(new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbIpWhois.json.gz");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```csharp
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesIPWHOISApi(config);

SnapshotStatus result = api.DbIpWhoisStatus();
Console.WriteLine(result.ToJson());

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```csharp
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required): The day whose file you want, in YYYY-MM-DD format.
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesIPSecurityApi(config);

FileParameter download = api.DbIpSecurity(new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbIpSecurity.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```csharp
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesIPSecurityApi(config);

SnapshotStatus result = api.DbIpSecurityStatus();
Console.WriteLine(result.ToJson());

```

### Databases - Threat Feed

#### Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

```csharp
// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesThreatFeedApi(config);

FileParameter download = api.DownloadThreatFeedPhishing(date: "2026-10-01");
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DownloadThreatFeedPhishing.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

```csharp
// Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesThreatFeedApi(config);

FileParameter download = api.DownloadThreatFeedPhishingSample();
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DownloadThreatFeedPhishingSample.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

```csharp
// Runnable example: Download the daily malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesThreatFeedApi(config);

FileParameter download = api.DownloadThreatFeedMalware(date: "2026-10-01");
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DownloadThreatFeedMalware.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

```csharp
// Runnable example: Download a sample of the malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware/sample)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
//   (no parameters; the API key is set on the client)
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesThreatFeedApi(config);

FileParameter download = api.DownloadThreatFeedMalwareSample();
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DownloadThreatFeedMalwareSample.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

```csharp
// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesThreatFeedApi(config);

FileParameter download = api.DownloadThreatFeedSpam(date: "2026-10-01");
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DownloadThreatFeedSpam.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

#### Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

```csharp
// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesThreatFeedApi(config);

FileParameter download = api.DownloadThreatFeedSpamSample();
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DownloadThreatFeedSpamSample.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");

```

### Databases - Streaming

#### Stream the daily phishing threat feed (CSV)

`GET /v3.4/stream/threat-feed/phishing`

```csharp
// Runnable example: Stream the daily phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamThreatFeedPhishing (GET /v3.4/stream/threat-feed/phishing):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamThreatFeedPhishing(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream a sample of the phishing threat feed (CSV)

`GET /v3.4/stream/threat-feed/phishing/sample`

```csharp
// Runnable example: Stream a sample of the phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing/sample)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamThreatFeedPhishingSample (GET /v3.4/stream/threat-feed/phishing/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamThreatFeedPhishingSample();
Console.WriteLine(result);

```

#### Stream the daily malware threat feed (CSV)

`GET /v3.4/stream/threat-feed/malware`

```csharp
// Runnable example: Stream the daily malware threat feed (CSV) (GET /v3.4/stream/threat-feed/malware)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamThreatFeedMalware (GET /v3.4/stream/threat-feed/malware):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamThreatFeedMalware(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream a sample of the malware threat feed (CSV)

`GET /v3.4/stream/threat-feed/malware/sample`

```csharp
// Runnable example: Stream a sample of the malware threat feed (CSV) (GET /v3.4/stream/threat-feed/malware/sample)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamThreatFeedMalwareSample (GET /v3.4/stream/threat-feed/malware/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamThreatFeedMalwareSample();
Console.WriteLine(result);

```

#### Stream the daily spam threat feed (CSV)

`GET /v3.4/stream/threat-feed/spam`

```csharp
// Runnable example: Stream the daily spam threat feed (CSV) (GET /v3.4/stream/threat-feed/spam)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamThreatFeedSpam (GET /v3.4/stream/threat-feed/spam):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamThreatFeedSpam(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream a sample of the spam threat feed (CSV)

`GET /v3.4/stream/threat-feed/spam/sample`

```csharp
// Runnable example: Stream a sample of the spam threat feed (CSV) (GET /v3.4/stream/threat-feed/spam/sample)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamThreatFeedSpamSample (GET /v3.4/stream/threat-feed/spam/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamThreatFeedSpamSample();
Console.WriteLine(result);

```

#### Stream newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/gtld`

```csharp
// Runnable example: Stream newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/gtld)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerGtld (GET /v3.3/stream/domainer/gtld):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerGtld(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream cleaned newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/gtld/cleaned`

```csharp
// Runnable example: Stream cleaned newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/gtld/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerGtldCleaned (GET /v3.3/stream/domainer/gtld/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerGtldCleaned(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream cleaned newly registered gTLD domains with an email (CSV)

`GET /v3.3/stream/domainer/gtld/cleaned/email`

```csharp
// Runnable example: Stream cleaned newly registered gTLD domains with an email (CSV) (GET /v3.3/stream/domainer/gtld/cleaned/email)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerGtldCleanedEmail (GET /v3.3/stream/domainer/gtld/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerGtldCleanedEmail(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream cleaned newly registered gTLD domains with a phone (CSV)

`GET /v3.3/stream/domainer/gtld/cleaned/phone`

```csharp
// Runnable example: Stream cleaned newly registered gTLD domains with a phone (CSV) (GET /v3.3/stream/domainer/gtld/cleaned/phone)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerGtldCleanedPhone (GET /v3.3/stream/domainer/gtld/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerGtldCleanedPhone(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/cctld`

```csharp
// Runnable example: Stream newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/cctld)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerCctld (GET /v3.3/stream/domainer/cctld):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerCctld(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream cleaned newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/cctld/cleaned`

```csharp
// Runnable example: Stream cleaned newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/cctld/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerCctldCleaned (GET /v3.3/stream/domainer/cctld/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerCctldCleaned(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream cleaned newly registered ccTLD domains with an email (CSV)

`GET /v3.3/stream/domainer/cctld/cleaned/email`

```csharp
// Runnable example: Stream cleaned newly registered ccTLD domains with an email (CSV) (GET /v3.3/stream/domainer/cctld/cleaned/email)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerCctldCleanedEmail (GET /v3.3/stream/domainer/cctld/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerCctldCleanedEmail(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream cleaned newly registered ccTLD domains with a phone (CSV)

`GET /v3.3/stream/domainer/cctld/cleaned/phone`

```csharp
// Runnable example: Stream cleaned newly registered ccTLD domains with a phone (CSV) (GET /v3.3/stream/domainer/cctld/cleaned/phone)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerCctldCleanedPhone (GET /v3.3/stream/domainer/cctld/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerCctldCleanedPhone(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream expiring domains (CSV)

`GET /v3.3/stream/domainer/expired`

```csharp
// Runnable example: Stream expiring domains (CSV) (GET /v3.3/stream/domainer/expired)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerExpired (GET /v3.3/stream/domainer/expired):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerExpired(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream cleaned expiring domains (CSV)

`GET /v3.3/stream/domainer/expired/cleaned`

```csharp
// Runnable example: Stream cleaned expiring domains (CSV) (GET /v3.3/stream/domainer/expired/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerExpiredCleaned (GET /v3.3/stream/domainer/expired/cleaned):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerExpiredCleaned(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream cleaned expiring domains with an email (CSV)

`GET /v3.3/stream/domainer/expired/cleaned/email`

```csharp
// Runnable example: Stream cleaned expiring domains with an email (CSV) (GET /v3.3/stream/domainer/expired/cleaned/email)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerExpiredCleanedEmail (GET /v3.3/stream/domainer/expired/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerExpiredCleanedEmail(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream cleaned expiring domains with a phone (CSV)

`GET /v3.3/stream/domainer/expired/cleaned/phone`

```csharp
// Runnable example: Stream cleaned expiring domains with a phone (CSV) (GET /v3.3/stream/domainer/expired/cleaned/phone)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerExpiredCleanedPhone (GET /v3.3/stream/domainer/expired/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerExpiredCleanedPhone(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream dropped domains (CSV)

`GET /v3.3/stream/domainer/dropped`

```csharp
// Runnable example: Stream dropped domains (CSV) (GET /v3.3/stream/domainer/dropped)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerDropped (GET /v3.3/stream/domainer/dropped):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerDropped(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream dropped domains with backlinks (CSV)

`GET /v3.3/stream/domainer/dropped/backlinks`

```csharp
// Runnable example: Stream dropped domains with backlinks (CSV) (GET /v3.3/stream/domainer/dropped/backlinks)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerDroppedBacklinks (GET /v3.3/stream/domainer/dropped/backlinks):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerDroppedBacklinks(new DateOnly(2026, 10, 1));
Console.WriteLine(result);

```

#### Stream a sample of newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/gtld`

```csharp
// Runnable example: Stream a sample of newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/sample/gtld)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerGtldSample (GET /v3.3/stream/domainer/sample/gtld):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerGtldSample();
Console.WriteLine(result);

```

#### Stream a sample of cleaned newly registered gTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/gtld/cleaned`

```csharp
// Runnable example: Stream a sample of cleaned newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/sample/gtld/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerGtldCleanedSample (GET /v3.3/stream/domainer/sample/gtld/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerGtldCleanedSample();
Console.WriteLine(result);

```

#### Stream a sample of newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/cctld`

```csharp
// Runnable example: Stream a sample of newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/sample/cctld)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerCctldSample (GET /v3.3/stream/domainer/sample/cctld):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerCctldSample();
Console.WriteLine(result);

```

#### Stream a sample of cleaned newly registered ccTLD domains (CSV)

`GET /v3.3/stream/domainer/sample/cctld/cleaned`

```csharp
// Runnable example: Stream a sample of cleaned newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/sample/cctld/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerCctldCleanedSample (GET /v3.3/stream/domainer/sample/cctld/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerCctldCleanedSample();
Console.WriteLine(result);

```

#### Stream a sample of expiring domains (CSV)

`GET /v3.3/stream/domainer/sample/expired`

```csharp
// Runnable example: Stream a sample of expiring domains (CSV) (GET /v3.3/stream/domainer/sample/expired)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerExpiredSample (GET /v3.3/stream/domainer/sample/expired):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerExpiredSample();
Console.WriteLine(result);

```

#### Stream a sample of cleaned expiring domains (CSV)

`GET /v3.3/stream/domainer/sample/expired/cleaned`

```csharp
// Runnable example: Stream a sample of cleaned expiring domains (CSV) (GET /v3.3/stream/domainer/sample/expired/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerExpiredCleanedSample (GET /v3.3/stream/domainer/sample/expired/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerExpiredCleanedSample();
Console.WriteLine(result);

```

#### Stream a sample of dropped domains (CSV)

`GET /v3.3/stream/domainer/sample/dropped`

```csharp
// Runnable example: Stream a sample of dropped domains (CSV) (GET /v3.3/stream/domainer/sample/dropped)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerDroppedSample (GET /v3.3/stream/domainer/sample/dropped):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerDroppedSample();
Console.WriteLine(result);

```

#### Stream a sample of dropped domains with backlinks (CSV)

`GET /v3.3/stream/domainer/sample/dropped/backlinks`

```csharp
// Runnable example: Stream a sample of dropped domains with backlinks (CSV) (GET /v3.3/stream/domainer/sample/dropped/backlinks)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamDomainerDroppedBacklinksSample (GET /v3.3/stream/domainer/sample/dropped/backlinks):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamDomainerDroppedBacklinksSample();
Console.WriteLine(result);

```
