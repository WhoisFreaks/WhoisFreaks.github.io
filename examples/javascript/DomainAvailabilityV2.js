// Domain Availability Check with Suggestions: GET https://api.whoisfreaks.com/v2.0/domain/availability
// Run: WHOISFREAKS_API_KEY=your_api_key node DomainAvailabilityV2.js
const { ApiClient, DomainAvailabilityApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DomainAvailabilityApi(client);

// domainAvailabilityV2(domain, opts)
//   domain (string, required): The domain name to check
//   opts.sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain; default false
//   opts.count (number, optional): Number of TLD suggestions to return when sug=true. Maximum is 100; default 5
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.domainAvailabilityV2("google.com", { sug: true, count: 5 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
