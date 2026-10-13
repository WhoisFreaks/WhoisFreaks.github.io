// Newly Registered gTLD (JSON): GET https://files.whoisfreaks.com/v3.1/domains/newly/gtld
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbNewlyGtldJson.ts
import { Configuration, DatabasesNewlyRegisteredApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesNewlyRegisteredApi(config);

// dbNewlyGtldJson({ date?, tlds? })
//   date (Date, optional): yyyy-MM-dd; omit for latest
//   tlds (string, optional)
async function main(): Promise<void> {
  const domains = await api.dbNewlyGtldJson({ date: new Date("2026-10-01") });
  console.log(`${domains.length} domains`);
  console.log(domains.slice(0, 10).join("\n"));
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
