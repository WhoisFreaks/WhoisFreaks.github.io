// Historical DNS Lookup (v2.2): GET https://api.whoisfreaks.com/v2.2/dns/historical
// Run: WHOISFREAKS_API_KEY=your_api_key node DnsHistoricalV22.js
const { ApiClient, DNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DNSApi(client);

// dnsHistoricalV22(domainName, type, opts)
//   domainName (string, required)
//   type (string, required): default "all"
//   opts.page (number, optional): default 1
//   opts.sort (string, optional): Sort direction. Omit to leave the results unsorted; one of asc, desc
//   opts.sortBy (string, optional): Field to sort on. Only applies when sort is given; one of firstSeen, lastSeen; default "lastSeen"
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.dnsHistoricalV22("whoisfreaks.com", "A,MX,TXT", { page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
