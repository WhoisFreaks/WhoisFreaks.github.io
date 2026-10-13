// Bulk DNS Lookup: POST https://api.whoisfreaks.com/v2.0/dns/bulk/live
// Run: WHOISFREAKS_API_KEY=your_api_key node DnsBulk.js
const { ApiClient, DNSApi, DnsBulkRequest } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DNSApi(client);

// dnsBulk(type, dnsBulkRequest, opts)
//   type (string, required): default "all"
//   dnsBulkRequest (DnsBulkRequest, required): request body
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const body = DnsBulkRequest.constructFromObject({ domainNames: ["whoisfreaks.com", "example.com"] });
  const result = await api.dnsBulk("A,MX,TXT", body);
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
