// Expiring Domains: GET https://files.whoisfreaks.com/v3.1/download/domainer/expired
// Run: WHOISFREAKS_API_KEY=your_api_key node DbExpired.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesExpiringDroppedApi(client);

// dbExpired(whois, opts)
//   whois (boolean, required)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
async function main() {
  const data = await api.dbExpired(true, { date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbExpired.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
