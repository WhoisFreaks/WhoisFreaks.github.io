// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
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
