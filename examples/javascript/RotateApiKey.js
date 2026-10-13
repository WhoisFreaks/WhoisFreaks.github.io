// Rotate API Key: GET https://api.whoisfreaks.com/v1.0/api-key/rotate
// Run: WHOISFREAKS_API_KEY=your_api_key node RotateApiKey.js
const { ApiClient, AccountApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new AccountApi(client);

// rotateApiKey() takes no parameters.
async function main() {
  const newKey = await api.rotateApiKey(); // use this key from now on
  console.log("New API key:", newKey);
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
