// ASN WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/asn-whois
// Run: WHOISFREAKS_API_KEY=your_api_key node AsnWhois.js
const { ApiClient, ASNWHOISApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new ASNWHOISApi(client);

// asnWhois(asn, opts)
//   asn (string, required): Autonomous system number to look up, with or without the AS prefix
//   opts.format (string, optional): Response format. JSON when the parameter is left out; one of json, xml; default "json"
async function main() {
  const result = await api.asnWhois("as15169");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
