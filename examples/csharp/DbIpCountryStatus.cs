// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesIPGeolocationApi(config);

SnapshotStatus result = api.DbIpCountryStatus();
Console.WriteLine(result.ToJson());
