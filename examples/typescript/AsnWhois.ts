// ASN WHOIS Lookup: GET https://api.whoisfreaks.com/v2.0/asn-whois
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx AsnWhois.ts
import { Configuration, ASNWHOISApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new ASNWHOISApi(config);

// asnWhois({ asn, format? })
//   asn (string, required)
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.asnWhois({ asn: "as15169" });
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
