// Runnable example: Stream a sample of the phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing/sample)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for streamThreatFeedPhishingSample (GET /v3.4/stream/threat-feed/phishing/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new DatabasesStreamingApi(config);

string result = api.StreamThreatFeedPhishingSample();
Console.WriteLine(result);
