// Historical DNS Lookup (v2.3): GET https://api.whoisfreaks.com/v2.3/dns/historical
// Run: WHOISFREAKS_API_KEY=your_api_key node DnsHistoricalV23.js
const { ApiClient, DNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DNSApi(client);

// dnsHistoricalV23(domainName, type, opts)
//   domainName (string, required): Domain to look up
//   type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
//   opts.page (number, optional): Page of results to return. Defaults to 1; default 1
//   opts.sort (string, optional): Sort direction. Omit to leave the results unsorted; one of asc, desc
//   opts.sortBy (string, optional): Field to sort on. Only applies when sort is given; one of firstSeen, lastSeen; default "lastSeen"
//   opts.format (string, optional): Response format. JSON when the parameter is left out; one of json, xml; default "json"
async function main() {
  const result = await api.dnsHistoricalV23("whoisfreaks.com", "A,MX,TXT", { page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
