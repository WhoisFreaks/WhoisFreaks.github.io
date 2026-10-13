// Domain Availability Check with Suggestions: GET https://api.whoisfreaks.com/v2.0/domain/availability
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DomainAvailabilityV2.ts
import { Configuration, DomainAvailabilityApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DomainAvailabilityApi(config);

// domainAvailabilityV2({ domain, sug?, count?, format? })
//   domain (string, required): The domain name to check
//   sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain; default false
//   count (number, optional): Number of TLD suggestions to return when sug=true. Maximum is 100; default 5
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.domainAvailabilityV2({ domain: "google.com", sug: true, count: 5 });
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
