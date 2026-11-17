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
