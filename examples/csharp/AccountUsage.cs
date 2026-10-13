// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new AccountApi(config);

AccountUsageResponse result = api.AccountUsage();
Console.WriteLine(result.ToJson());
