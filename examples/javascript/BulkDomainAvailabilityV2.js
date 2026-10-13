// Bulk Domain Availability Check: POST https://api.whoisfreaks.com/v2.0/domain/availability
// Run: WHOISFREAKS_API_KEY=your_api_key node BulkDomainAvailabilityV2.js
const { ApiClient, DomainAvailabilityApi, BulkDomainAvailabilityRequest } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DomainAvailabilityApi(client);

// bulkDomainAvailabilityV2(bulkDomainAvailabilityRequest, opts)
//   bulkDomainAvailabilityRequest (BulkDomainAvailabilityRequest, required): request body
//   opts.domain (string, optional): Required for TLD-mode bulk check (base domain)
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const body = BulkDomainAvailabilityRequest.constructFromObject({ domainNames: ["whoisfreaks.com", "example.com"] });
  const result = await api.bulkDomainAvailabilityV2(body);
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
