// Historical WHOIS records for a domain: GET https://api.whoisfreaks.com/v2.0/whois/history
// Run: WHOISFREAKS_API_KEY=your_api_key node WhoisHistory.js
const { ApiClient, WHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new WHOISApi(client);

// whoisHistory(domainName, opts)
//   domainName (string, required): Domain to fetch historical WHOIS records for
//   opts.format (string, optional): one of json, xml
async function main() {
  const result = await api.whoisHistory("whoisfreaks.com");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
