// Bulk IP Reputation: POST https://api.whoisfreaks.com/v1.0/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkIpReputation.ts
import { Configuration, IPReputationApi, ResponseError, type BulkGeolocationRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new IPReputationApi(config);

// bulkIpReputation({ bulkGeolocationRequest })
//   bulkGeolocationRequest (BulkGeolocationRequest, required): request body
async function main(): Promise<void> {
  const body: BulkGeolocationRequest = { ips: ["8.8.8.8", "1.1.1.1"] };
  const results = await api.bulkIpReputation({ bulkGeolocationRequest: body });
  console.log(JSON.stringify(results, null, 2));
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
