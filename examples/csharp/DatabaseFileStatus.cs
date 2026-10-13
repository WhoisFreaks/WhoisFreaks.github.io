// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Run it from the Getting Started project: replace Program.cs with this file, then `dotnet run`
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; no API key required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

var config = new Configuration();
// Public endpoint: no API key needed.
var api = new AccountApi(config);

DatabaseFileStatus result = api.DatabaseFileStatus();
Console.WriteLine(result.ToJson());
