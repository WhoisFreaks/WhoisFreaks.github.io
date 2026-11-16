// Stream a sample of cleaned newly registered ccTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/cctld/cleaned
// Run (public endpoint, no API key needed): npx tsx StreamDomainerCctldCleanedSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerCctldCleanedSample({ whois?, offset?, limit? })
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const newKey = await api.streamDomainerCctldCleanedSample(); // use this key from now on
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
