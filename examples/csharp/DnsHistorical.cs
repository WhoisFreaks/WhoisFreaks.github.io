// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
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

HistoricalDnsResponse result = api.DnsHistorical("whoisfreaks.com", "A,MX,TXT", page: 1);
Console.WriteLine(result.ToJson());
