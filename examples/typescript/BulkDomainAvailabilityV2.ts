// Bulk Domain Availability Check: POST https://api.whoisfreaks.com/v2.0/domain/availability
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkDomainAvailabilityV2.ts
import { Configuration, DomainAvailabilityApi, ResponseError, type BulkDomainAvailabilityRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DomainAvailabilityApi(config);

// bulkDomainAvailabilityV2({ bulkDomainAvailabilityRequest, domain?, format? })
//   bulkDomainAvailabilityRequest (BulkDomainAvailabilityRequest, required): request body
//   domain (string, optional): Required for TLD-mode bulk check (base domain)
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const body: BulkDomainAvailabilityRequest = { domainNames: ["whoisfreaks.com", "example.com"] };
  const result = await api.bulkDomainAvailabilityV2({ bulkDomainAvailabilityRequest: body });
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
