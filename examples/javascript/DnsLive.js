// Live DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/live
// Run: WHOISFREAKS_API_KEY=your_api_key node DnsLive.js
const { ApiClient, DNSApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new DNSApi(client);

// dnsLive(type, opts)
//   type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME; default "all"
//   opts.domainName (string, optional): Domain to look up
//   opts.ipAddress (string, optional): Use for PTR lookups
//   opts.cnameDepth (number, optional): How many CNAME links to follow before returning the records they point at. 0,...; default 0
//   opts.relativeRecords (boolean, optional): Keeps the records picked up for other names along the way, such as a CNAME ta...; default true
//   opts.isAuthoritative (boolean, optional): Set true to read the records from the zone's own nameservers instead of a rec...; default false
//   opts.format (string, optional): Response format. JSON when the parameter is left out; one of json, xml; default "json"
async function main() {
  const result = await api.dnsLive("A,MX,TXT", { domainName: "whoisfreaks.com" });
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
