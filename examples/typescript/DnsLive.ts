// Live DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsLive.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsLive({ type, domainName?, ipAddress?, format? })
//   type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME; default "all"
//   domainName (string, optional)
//   ipAddress (string, optional): Use for PTR lookups
//   format ("json" | "xml", optional): default "json"
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
