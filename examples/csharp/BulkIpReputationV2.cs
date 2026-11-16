// Runnable example: Bulk IP Reputation (v2.0) (POST /v2.0/security)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for bulkIpReputationV2 (POST /v2.0/security):
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

var body = new BulkGeolocationRequest(ips: new List<string> { "1.1.1.1", "2.2.2.2", "8.8.8.8" });
List<IpReputationResponse> result = api.BulkIpReputationV2(body);
foreach (var item in result)
{
    Console.WriteLine(item.ToJson());
}
