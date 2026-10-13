// Historical DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/historical
// Run: WHOISFREAKS_API_KEY=your_api_key node DnsHistorical.js
const { ApiClient, DNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DNSApi(client);

// dnsHistorical(domainName, type, opts)
//   domainName (string, required)
//   type (string, required): default "all"
//   opts.page (number, optional): default 1
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.dnsHistorical("whoisfreaks.com", "A,MX,TXT", { page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
