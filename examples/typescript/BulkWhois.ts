// Bulk WHOIS Lookup: POST https://api.whoisfreaks.com/v2.0/bulkwhois/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkWhois.ts
import { Configuration, WHOISApi, ResponseError, type BulkWhoisRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new WHOISApi(config);

// bulkWhois({ bulkWhoisRequest, format? })
//   bulkWhoisRequest (BulkWhoisRequest, required): request body
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const body: BulkWhoisRequest = { domainNames: ["whoisfreaks.com", "jfreaks.com"] };
  const result = await api.bulkWhois({ bulkWhoisRequest: body });
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
