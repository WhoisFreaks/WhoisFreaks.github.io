// IP Reputation Lookup (v2.0): GET https://api.whoisfreaks.com/v2.0/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx IpReputationV2.ts
import { Configuration, IPReputationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new IPReputationApi(config);

// ipReputationV2({ ip })
//   ip (string, required)
async function main(): Promise<void> {
  const result = await api.ipReputationV2({ ip: "8.8.8.8" });
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
