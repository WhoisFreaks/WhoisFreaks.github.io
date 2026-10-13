// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesNewlyRegisteredApi(config);

FileParameter download = api.DbNewlyGtldCleaned(date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbNewlyGtldCleaned.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");
