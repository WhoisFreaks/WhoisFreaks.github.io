// ASN WHOIS Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/asn/whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbAsnWhoisStatus.ts
import { Configuration, DatabasesASNWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesASNWHOISApi(config);

// dbAsnWhoisStatus() takes no parameters.
async function main(): Promise<void> {
  const result = await api.dbAsnWhoisStatus();
  console.log(JSON.stringify(result, null, 2));
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
