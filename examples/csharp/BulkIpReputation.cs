// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkGeolocationRequest (required): request body object
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new IPReputationApi(config);

var body = new BulkGeolocationRequest(ips: new List<string> { "8.8.8.8", "1.1.1.1" });
List<IpReputationResponse> result = api.BulkIpReputation(body);
foreach (var item in result)
{
    Console.WriteLine(item.ToJson());
}
