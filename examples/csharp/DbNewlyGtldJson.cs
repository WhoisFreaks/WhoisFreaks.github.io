// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesNewlyRegisteredApi(config);

List<string> result = api.DbNewlyGtldJson(date: new DateOnly(2026, 10, 1));
foreach (var item in result)
{
    Console.WriteLine(item);
}
