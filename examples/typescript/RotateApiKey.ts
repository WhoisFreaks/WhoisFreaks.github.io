// Rotate API Key: GET https://api.whoisfreaks.com/v1.0/api-key/rotate
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx RotateApiKey.ts
import { Configuration, AccountApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new AccountApi(config);

// rotateApiKey() takes no parameters.
async function main(): Promise<void> {
  const newKey = await api.rotateApiKey(); // use this key from now on
  console.log("New API key:", newKey);
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
