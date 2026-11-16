// Stream a sample of expiring domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/sample/expired
// Run (public endpoint, no API key needed): npx tsx StreamDomainerExpiredSample.ts
import { DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new DatabasesStreamingApi();

// streamDomainerExpiredSample({ whois?, offset?, limit? })
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const csvText = await api.streamDomainerExpiredSample(); // plain CSV text, already decompressed
  console.log(csvText);
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
