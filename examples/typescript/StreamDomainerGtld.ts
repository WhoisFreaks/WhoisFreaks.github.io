// Stream newly registered gTLD domains (CSV): GET https://files.whoisfreaks.com/v3.3/stream/domainer/gtld
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx StreamDomainerGtld.ts
import { Configuration, DatabasesStreamingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesStreamingApi(config);

// streamDomainerGtld({ date, whois?, offset?, limit? })
//   date (Date, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints
//   whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false st...; default false
//   offset (number, optional): Data rows to skip from the start of the file. The header row is never counted...
//   limit (number, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the hea...
async function main(): Promise<void> {
  const newKey = await api.streamDomainerGtld({ date: new Date("2026-10-01") }); // use this key from now on
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
