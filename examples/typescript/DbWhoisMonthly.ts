// WHOIS Database Monthly: GET https://files.whoisfreaks.com/v3.3/download/dbupdate/monthly/domains/whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbWhoisMonthly.ts
import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { Configuration, DatabasesWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesWHOISApi(config);

// dbWhoisMonthly({ date? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
async function main(): Promise<void> {
  const blob = await api.dbWhoisMonthly({ date: new Date("2026-10-01") }); // a Blob with the file's bytes
  const file = "DbWhoisMonthly.csv";
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
