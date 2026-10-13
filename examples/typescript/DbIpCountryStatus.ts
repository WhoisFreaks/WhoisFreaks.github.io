// IP to Country Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/country
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DbIpCountryStatus.ts
import { Configuration, DatabasesIPGeolocationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DatabasesIPGeolocationApi(config);

// dbIpCountryStatus() takes no parameters.
async function main(): Promise<void> {
  const result = await api.dbIpCountryStatus();
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
