// Runnable example: Historical DNS Lookup (v2.2) (GET /v2.2/dns/historical)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsHistoricalV22 (GET /v2.2/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional)
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
