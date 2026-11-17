// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, optional): Domain to look up.
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
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
