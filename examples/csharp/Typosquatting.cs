// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new TyposquattingApi(config);

TyposquattingResponse result = api.Typosquatting(keyword: "whoisfreaks");
Console.WriteLine(result.ToJson());
