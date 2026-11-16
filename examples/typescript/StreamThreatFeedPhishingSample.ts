// Stream a sample of the phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/stream/threat-feed/phishing/sample
// Run (public endpoint, no API key needed): npx tsx StreamThreatFeedPhishingSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamThreatFeedPhishingSample({ offset?, limit? })
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const newKey = await api.streamThreatFeedPhishingSample(); // use this key from now on
  console.log("New API key:", newKey);
}

main().catch(async (err: unknown) => {
  // API errors carry the HTTP response
  if (err instanceof ResponseError) {
    console.error(`HTTP ${err.response.status}: ${await err.response.text()}`);
  } else {
    console.error(err);
  }
  process.exitCode = 1;
});
