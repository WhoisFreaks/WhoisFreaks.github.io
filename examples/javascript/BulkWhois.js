// Bulk WHOIS Lookup: POST https://api.whoisfreaks.com/v2.0/bulkwhois/live
// Run: WHOISFREAKS_API_KEY=your_api_key node BulkWhois.js
const { ApiClient, WHOISApi, BulkWhoisRequest } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new WHOISApi(client);

// bulkWhois(bulkWhoisRequest, opts)
//   bulkWhoisRequest (BulkWhoisRequest, required): request body
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const body = BulkWhoisRequest.constructFromObject({ domainNames: ["whoisfreaks.com", "jfreaks.com"] });
  const result = await api.bulkWhois(body);
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
