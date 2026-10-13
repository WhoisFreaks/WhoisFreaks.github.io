// Reverse DNS Lookup: GET https://api.whoisfreaks.com/v2.1/dns/reverse
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsReverse.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsReverse({ value, type, exact?, page?, format? })
//   value (string, required): IP, CIDR, or record value
//   type ("a" | "mx" | "cname" | "ns" | "aaaa" | "txt" | "soa", required)
//   exact (boolean, optional): default true
//   page (number, optional): default 1
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.dnsReverse({ value: "8.8.8.8", type: "a", page: 1 });
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
