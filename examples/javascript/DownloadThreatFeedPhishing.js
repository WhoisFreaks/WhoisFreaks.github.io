// Download the daily phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing
// Run: WHOISFREAKS_API_KEY=your_api_key node DownloadThreatFeedPhishing.js
const fs = require("node:fs");
const path = require("node:path");
const { ApiClient, DatabasesThreatFeedApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesThreatFeedApi(client);

// downloadThreatFeedPhishing(opts)
//   opts.date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
async function main() {
  const data = await api.downloadThreatFeedPhishing({ date: "2026-10-01" }); // a Buffer with the file's bytes
  const file = "DownloadThreatFeedPhishing.csv";
  fs.writeFileSync(file, data);
  console.log(`Saved ${data.length} bytes to ${path.resolve(file)}`);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
