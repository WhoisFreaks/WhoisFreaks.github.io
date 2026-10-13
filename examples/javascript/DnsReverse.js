// Reverse DNS Lookup: GET https://api.whoisfreaks.com/v2.1/dns/reverse
// Run: WHOISFREAKS_API_KEY=your_api_key node DnsReverse.js
const { ApiClient, DNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DNSApi(client);

// dnsReverse(value, type, opts)
//   value (string, required): IP, CIDR, or record value
//   type (string, required): one of a, mx, cname, ns, aaaa, txt, soa
//   opts.exact (boolean, optional): default true
//   opts.page (number, optional): default 1
//   opts.format (string, optional): one of json, xml; default "json"
async function main() {
  const result = await api.dnsReverse("8.8.8.8", "a", { page: 1 });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
