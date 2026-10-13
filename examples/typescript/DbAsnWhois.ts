// ASN WHOIS Snapshot: GET https://files.whoisfreaks.com/v3.3/download/snapshot/asn/whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbAsnWhois.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesASNWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesASNWHOISApi(config);

// dbAsnWhois({ date })
//   date (Date, required)
async function main(): Promise<void> {
  const blob = await api.dbAsnWhois({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbAsnWhois.json.gz";
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
