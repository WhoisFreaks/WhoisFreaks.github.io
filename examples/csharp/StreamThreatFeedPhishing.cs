// Runnable example: Stream the daily phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamThreatFeedPhishing (GET /v3.4/stream/threat-feed/phishing):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesStreamingApi(config);

string result = api.StreamThreatFeedPhishing(new DateOnly(2026, 10, 1));
Console.WriteLine(result);
