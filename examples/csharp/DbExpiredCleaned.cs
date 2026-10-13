// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesExpiringDroppedApi(config);

FileParameter download = api.DbExpiredCleaned(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbExpiredCleaned.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");
