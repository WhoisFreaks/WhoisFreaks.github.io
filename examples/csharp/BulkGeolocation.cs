// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
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
var api = new GeolocationApi(config);

var body = new BulkGeolocationRequest(ips: new List<string> { "8.8.8.8", "1.1.1.1" });
List<GeolocationResponse> result = api.BulkGeolocation(body);
foreach (var item in result)
{
    Console.WriteLine(item.ToJson());
}
