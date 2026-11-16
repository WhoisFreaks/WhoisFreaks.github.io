// Stream a sample of the spam threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/spam/sample
// Run (public endpoint, no API key needed): node StreamThreatFeedSpamSample.js
const { DatabasesStreamingApi } = require("whoisfreaks-js");

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamThreatFeedSpamSample(opts)
//   opts.offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   opts.limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main() {
  const csvText = await api.streamThreatFeedSpamSample(); // plain CSV text, already decompressed
  console.log(csvText);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
