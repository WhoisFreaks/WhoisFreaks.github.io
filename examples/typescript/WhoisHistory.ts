// Historical WHOIS records for a domain: GET https://api.whoisfreaks.com/v2.0/whois/history
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx WhoisHistory.ts
import { Configuration, WHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new WHOISApi(config);

// whoisHistory({ domainName, format? })
//   domainName (string, required): Domain to fetch historical WHOIS records for
//   format ("json" | "xml", optional)
async function main(): Promise<void> {
  const result = await api.whoisHistory({ domainName: "whoisfreaks.com" });
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
