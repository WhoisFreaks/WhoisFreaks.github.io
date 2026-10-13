// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
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
