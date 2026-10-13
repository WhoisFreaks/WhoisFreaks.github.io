// Bulk IP Reputation: POST https://api.whoisfreaks.com/v1.0/security
// Run: WHOISFREAKS_API_KEY=your_api_key node BulkIpReputation.js
const { ApiClient, IPReputationApi, BulkGeolocationRequest } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new IPReputationApi(client);

// bulkIpReputation(bulkGeolocationRequest)
//   bulkGeolocationRequest (BulkGeolocationRequest, required): request body
async function main() {
  const body = BulkGeolocationRequest.constructFromObject({ ips: ["8.8.8.8", "1.1.1.1"] });
  const results = await api.bulkIpReputation(body);
  console.log(JSON.stringify(results, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
