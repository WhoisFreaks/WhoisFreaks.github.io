// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
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
