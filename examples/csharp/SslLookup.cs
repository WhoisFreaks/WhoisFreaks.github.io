// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new SSLApi(config);

SslResponse result = api.SslLookup("whoisfreaks.com");
Console.WriteLine(result.ToJson());
