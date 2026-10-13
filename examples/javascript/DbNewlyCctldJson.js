// Newly Registered ccTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/cctld
// Run: WHOISFREAKS_API_KEY=your_api_key node DbNewlyCctldJson.js
const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesNewlyRegisteredApi(client);

// dbNewlyCctldJson(opts)
//   opts.date (string, "yyyy-MM-dd", optional): yyyy-MM-dd; omit for latest
//   opts.tlds (string, optional)
async function main() {
  const domains = await api.dbNewlyCctldJson({ date: "2026-10-01" });
  console.log(`${domains.length} domains`);
  console.log(domains.slice(0, 10).join("\n"));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
