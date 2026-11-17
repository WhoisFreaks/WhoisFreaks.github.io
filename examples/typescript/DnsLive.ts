// Live DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsLive.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsLive({ type, domainName?, ipAddress?, cnameDepth?, relativeRecords?, isAuthoritative?, format? })
//   type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME; default "all"
//   domainName (string, optional): Domain to look up
//   ipAddress (string, optional): Use for PTR lookups
//   cnameDepth (number, optional): How many CNAME links to follow before returning the records they point at. 0,...; default 0
//   relativeRecords (boolean, optional): Keeps the records picked up for other names along the way, such as a CNAME ta...; default true
//   isAuthoritative (boolean, optional): Set true to read the records from the zone's own nameservers instead of a rec...; default false
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
async function main(): Promise<void> {
  const result = await api.dnsLive({ type: "A,MX,TXT", domainName: "whoisfreaks.com" });
  console.log(JSON.stringify(result, null, 2));
}

main().catch(async (err: unknown) => {
  // API errors carry the HTTP response
  if (err instanceof ResponseError) {
    console.error(`HTTP ${err.response.status}: ${await err.response.text()}`);
  } else {
    console.error(err);
  }
  process.exitCode = 1;
});
