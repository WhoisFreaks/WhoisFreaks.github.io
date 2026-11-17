// Subdomains Lookup: GET https://api.whoisfreaks.com/v1.0/subdomains
// Run: WHOISFREAKS_API_KEY=your_api_key node Subdomains.js
const { ApiClient, SubdomainsApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new SubdomainsApi(client);

// subdomains(domain, opts)
//   domain (string, required): Domain whose subdomains you want
//   opts.after (string, "yyyy-MM-dd", optional): Only return records created after this date, in YYYY-MM-DD format. Defaults t...
//   opts.before (string, "yyyy-MM-dd", optional): Only return records created before this date, in YYYY-MM-DD format. Defaults ...
//   opts.status (string, optional): Limit results to active or inactive subdomains. Both are returned when the pa...; one of active, inactive
//   opts.page (number, optional): Page of results to return. Defaults to 1; default 1
//   opts.format (string, optional): Response format. JSON when the parameter is left out; one of json, xml; default "json"
async function main() {
  const result = await api.subdomains("whoisfreaks.com", { page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
