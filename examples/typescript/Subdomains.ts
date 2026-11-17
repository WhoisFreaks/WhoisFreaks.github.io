// Subdomains Lookup: GET https://api.whoisfreaks.com/v1.0/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx Subdomains.ts
import { Configuration, SubdomainsApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new SubdomainsApi(config);

// subdomains({ domain, after?, before?, status?, page?, format? })
//   domain (string, required): Domain whose subdomains you want
//   after (Date, optional): Only return records created after this date, in YYYY-MM-DD format. Defaults t...
//   before (Date, optional): Only return records created before this date, in YYYY-MM-DD format. Defaults ...
//   status ("active" | "inactive", optional): Limit results to active or inactive subdomains. Both are returned when the pa...
//   page (number, optional): Page of results to return. Defaults to 1; default 1
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
async function main(): Promise<void> {
  const result = await api.subdomains({ domain: "whoisfreaks.com", page: 1 });
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
