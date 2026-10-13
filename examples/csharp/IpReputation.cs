// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
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
