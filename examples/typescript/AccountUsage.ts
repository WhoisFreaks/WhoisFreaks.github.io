// Account Usage: GET https://api.whoisfreaks.com/v1.0/whoisapi/usage
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx AccountUsage.ts
import { Configuration, AccountApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new AccountApi(config);

// accountUsage() takes no parameters.
async function main(): Promise<void> {
  const result = await api.accountUsage();
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
