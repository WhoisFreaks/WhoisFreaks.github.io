// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required): request body object
using System;
using System.Collections.Generic;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
var apiKey = Environment.GetEnvironmentVariable("WHOISFREAKS_API_KEY")
    ?? throw new InvalidOperationException("Set the WHOISFREAKS_API_KEY environment variable");
config.AddApiKey("apiKey", apiKey);  // set once, sent with every call
var api = new DomainAvailabilityApi(config);

var body = new BulkDomainAvailabilityRequest(domainNames: new List<string> { "whoisfreaks.com", "example.com" });
BulkDomainAvailabilityResponse result = api.BulkDomainAvailabilityV2(body);
Console.WriteLine(result.ToJson());
