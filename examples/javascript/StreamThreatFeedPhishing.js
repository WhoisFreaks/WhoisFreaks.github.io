// Stream the daily phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/phishing
// Run: WHOISFREAKS_API_KEY=your_api_key node StreamThreatFeedPhishing.js
const { ApiClient, DatabasesStreamingApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesStreamingApi(client);

// streamThreatFeedPhishing(date, opts)
//   date (string, "yyyy-MM-dd", required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   opts.offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   opts.limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main() {
  const newKey = await api.streamThreatFeedPhishing("2026-10-01"); // use this key from now on
  console.log("New API key:", newKey);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
