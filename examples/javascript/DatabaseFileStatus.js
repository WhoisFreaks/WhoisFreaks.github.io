// Database File Status (Public): GET https://files.whoisfreaks.com/v3.4/status
// Run (public endpoint, no API key needed): node DatabaseFileStatus.js
const { AccountApi } = require("whoisfreaks-js");

// Public endpoint: no API key needed.
const api = new AccountApi();

// databaseFileStatus() takes no parameters.
async function main() {
  const result = await api.databaseFileStatus();
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
