// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
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
var api = new SubdomainsApi(config);

SubdomainsResponse result = api.Subdomains("whoisfreaks.com", page: 1);
Console.WriteLine(result.ToJson());
