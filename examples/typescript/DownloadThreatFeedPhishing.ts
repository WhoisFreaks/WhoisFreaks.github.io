// Download the daily phishing threat feed (CSV): GET https://files.whoisfreaks.com/v3.4/download/threat-feed/phishing
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DownloadThreatFeedPhishing.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesThreatFeedApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesThreatFeedApi(config);

// downloadThreatFeedPhishing({ date? })
//   date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
async function main(): Promise<void> {
  const blob = await api.downloadThreatFeedPhishing({ date: "2026-10-01" }); // a Blob with the file's bytes
  const file = "DownloadThreatFeedPhishing.csv";
  await writeFile(file, new Uint8Array(await blob.arrayBuffer()));
  console.log(`Saved ${blob.size} bytes to ${resolve(file)}`);
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
