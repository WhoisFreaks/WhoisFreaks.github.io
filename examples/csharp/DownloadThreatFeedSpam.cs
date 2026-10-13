// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesThreatFeedApi(config);

FileParameter download = api.DownloadThreatFeedSpam(date: "2026-10-01");
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DownloadThreatFeedSpam.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");
