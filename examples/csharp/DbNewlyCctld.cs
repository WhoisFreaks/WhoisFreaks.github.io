// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
using System;
using System.IO;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DatabasesNewlyRegisteredApi(config);

FileParameter download = api.DbNewlyCctld(true, date: new DateOnly(2026, 10, 1));
// The SDK returns the response body as a stream: copy it to a file.
var path = Path.GetFullPath("DbNewlyCctld.csv");
using (Stream input = download.Content)
using (FileStream output = File.Create(path))
{
    input.CopyTo(output);
}
Console.WriteLine($"Saved {new FileInfo(path).Length} bytes to {path}");
