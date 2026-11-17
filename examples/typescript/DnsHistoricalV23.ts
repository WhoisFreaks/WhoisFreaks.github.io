// Historical DNS Lookup (v2.3): GET https://api.whoisfreaks.com/v2.3/dns/historical
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsHistoricalV23.ts
import { Configuration, DNSApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsHistoricalV23({ domainName, type, page?, sort?, sortBy?, format? })
//   domainName (string, required): Domain to look up
//   type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
//   page (number, optional): Page of results to return. Defaults to 1; default 1
//   sort ("asc" | "desc", optional): Sort direction. Omit to leave the results unsorted
//   sortBy ("firstSeen" | "lastSeen", optional): Field to sort on. Only applies when sort is given; default "lastSeen"
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
async function main(): Promise<void> {
  const result = await api.dnsHistoricalV23({ domainName: "whoisfreaks.com", type: "A,MX,TXT", page: 1 });
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
