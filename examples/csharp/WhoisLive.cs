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
