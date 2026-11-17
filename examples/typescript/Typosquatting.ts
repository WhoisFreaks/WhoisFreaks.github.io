// Typosquatting Lookup: GET https://api.whoisfreaks.com/v3.0/domain/typos
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx Typosquatting.ts
import { Configuration, TyposquattingApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new TyposquattingApi(config);

// typosquatting({ keyword?, pattern?, pageToken? })
//   keyword (string, optional): Brand or label to find typo variants for. Pass either keyword or pattern, not...
//   pattern (string, optional): Wildcard search string, where '*' matches any characters. Pass either keyword...
//   pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward....
async function main(): Promise<void> {
  const result = await api.typosquatting({ keyword: "whoisfreaks" });
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
