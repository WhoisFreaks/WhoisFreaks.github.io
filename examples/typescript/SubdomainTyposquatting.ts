// Subdomain Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/subdomains/typos
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx SubdomainTyposquatting.ts
import { Configuration, TyposquattingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new TyposquattingApi(config);

// subdomainTyposquatting({ keyword?, pattern?, pageToken?, fetch_size? })
//   keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits...
//   pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one....
//   pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward....
//   fetch_size (number, optional): Subdomains per page. 100 when the parameter is left out, and values above 100...; default 100
async function main(): Promise<void> {
  const result = await api.subdomainTyposquatting();
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
