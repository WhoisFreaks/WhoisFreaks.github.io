// Subdomain Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/subdomains/typos
// Run: WHOISFREAKS_API_KEY=your_api_key node SubdomainTyposquatting.js
const { ApiClient, TyposquattingApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new TyposquattingApi(client);

// subdomainTyposquatting(opts)
//   opts.keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits...
//   opts.pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one....
//   opts.pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward....
//   opts.fetch_size (number, optional): Subdomains per page. 100 when the parameter is left out, and values above 100...; default 100
async function main() {
  const result = await api.subdomainTyposquatting();
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
