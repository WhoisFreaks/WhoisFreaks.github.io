// Newly Registered gTLD (CSV): GET https://files.whoisfreaks.com/v3.1/download/domainer/gtld
// Run: WHOISFREAKS_API_KEY=your_api_key node DbNewlyGtld.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesNewlyRegisteredApi(client);

// dbNewlyGtld(whois, opts)
//   whois (boolean, required)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
//   opts.tlds (string, optional)
async function main() {
  const data = await api.dbNewlyGtld(true, { date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DbNewlyGtld.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
