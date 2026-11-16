// Stream a sample of the phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/phishing/sample
// Run (public endpoint, no API key needed): node StreamThreatFeedPhishingSample.js
const { DatabasesStreamingApi } = require("whoisfreaks-js");

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamThreatFeedPhishingSample(opts)
//   opts.offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   opts.limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main() {
  const newKey = await api.streamThreatFeedPhishingSample(); // use this key from now on
  console.log("New API key:", newKey);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
