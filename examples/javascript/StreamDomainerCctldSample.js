// Stream a sample of newly registered ccTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/cctld
// Run (public endpoint, no API key needed): node StreamDomainerCctldSample.js
const { DatabasesStreamingApi } = require("whoisfreaks-js");

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerCctldSample(opts)
//   opts.whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   opts.offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   opts.limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main() {
  const csvText = await api.streamDomainerCctldSample(); // plain CSV text, already decompressed
  console.log(csvText);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
