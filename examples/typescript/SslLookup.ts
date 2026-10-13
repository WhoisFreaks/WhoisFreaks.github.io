// SSL Certificate Lookup: GET https://api.whoisfreaks.com/v1.0/ssl/live
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx SslLookup.ts
import { Configuration, SSLApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new SSLApi(config);

// sslLookup({ domainName, chain?, sslRaw?, format? })
//   domainName (string, required)
//   chain (boolean, optional): default false
//   sslRaw (boolean, optional): default false
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.sslLookup({ domainName: "whoisfreaks.com" });
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
