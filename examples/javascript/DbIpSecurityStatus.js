// IP Security Snapshot Status: GET https://files.whoisfreaks.com/v3.3/status/snapshot/ip/security
// Run: WHOISFREAKS_API_KEY=your_api_key node DbIpSecurityStatus.js
const { ApiClient, DatabasesIPSecurityApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DatabasesIPSecurityApi(client);

// dbIpSecurityStatus() takes no parameters.
async function main() {
  const result = await api.dbIpSecurityStatus();
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
