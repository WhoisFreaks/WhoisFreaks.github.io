// ASN WHOIS Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/asn/whois
// Run: WHOISFREAKS_API_KEY=your_api_key node DbAsnWhois.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesASNWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesASNWHOISApi(client);

// dbAsnWhois(date)
//   date (string, "yyyy-MM-dd", required)
async function main() {
  const data = await api.dbAsnWhois("2026-10-01"); // a Buffer with the file's bytes
  const file = "DbAsnWhois.json.gz";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
