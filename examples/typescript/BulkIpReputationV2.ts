// Bulk IP Reputation (v2.0): POST https://api.whoisfreaks.com/v2.0/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx BulkIpReputationV2.ts
import { Configuration, IPReputationApi, ResponseError, type BulkGeolocationRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new IPReputationApi(config);

// bulkIpReputationV2({ bulkGeolocationRequest })
//   bulkGeolocationRequest (BulkGeolocationRequest, required): request body
async function main(): Promise<void> {
  const body: BulkGeolocationRequest = { ips: ["1.1.1.1", "2.2.2.2", "8.8.8.8"] };
  const results = await api.bulkIpReputationV2({ bulkGeolocationRequest: body });
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
