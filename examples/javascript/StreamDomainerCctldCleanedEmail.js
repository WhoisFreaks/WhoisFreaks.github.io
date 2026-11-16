// Stream cleaned newly registered ccTLD domains with an email (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/cctld/cleaned/email
// Run: WHOISFREAKS_API_KEY=your_api_key node StreamDomainerCctldCleanedEmail.js
const { ApiClient, DatabasesStreamingApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesStreamingApi(client);

// streamDomainerCctldCleanedEmail(date, opts)
//   date (string, "yyyy-MM-dd", required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   opts.whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   opts.offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   opts.limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main() {
  const csvText = await api.streamDomainerCctldCleanedEmail("2026-10-01"); // plain CSV text, already decompressed
  console.log(csvText);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
