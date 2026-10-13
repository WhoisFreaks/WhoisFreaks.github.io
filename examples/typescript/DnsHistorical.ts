// Historical DNS Lookup: GET https://api.whoisfreaks.com/v2.0/dns/historical
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsHistorical.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsHistorical({ domainName, type, page?, format? })
//   domainName (string, required)
//   type (string, required): default "all"
//   page (number, optional): default 1
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.dnsHistorical({ domainName: "whoisfreaks.com", type: "A,MX,TXT", page: 1 });
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
