// Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/domain/typos
// Run: WHOISFREAKS_API_KEY=your_api_key node Typosquatting.js
const { ApiClient, TyposquattingApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new TyposquattingApi(client);

// typosquatting(opts)
//   opts.keyword (string, optional)
//   opts.pattern (string, optional)
//   opts.pageToken (string, optional)
async function main() {
  const result = await api.typosquatting({ keyword: "whoisfreaks" });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
