// Bulk DNS Lookup: POST https://api.whoisfreaks.com/v2.0/dns/bulk/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DnsBulk.ts
import { Configuration, DNSApi, ResponseError, type DnsBulkRequest } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DNSApi(config);

// dnsBulk({ type, dnsBulkRequest, cname_depth?, isAuthoritative?, format? })
//   type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to...; default "all"
//   dnsBulkRequest (DnsBulkRequest, required): request body
//   cname_depth (number, optional): How many CNAME links to follow before returning the records they point at. 0,...; default 0
//   isAuthoritative (boolean, optional): Set true to read the records from each zone's own nameservers instead of a re...; default false
//   format ("json" | "xml", optional): Response format. JSON when the parameter is left out; default "json"
async function main(): Promise<void> {
  const body: DnsBulkRequest = { domainNames: ["whoisfreaks.com", "example.com"] };
  const result = await api.dnsBulk({ type: "A,MX,TXT", dnsBulkRequest: body });
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
