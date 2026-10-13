// Database File Status (Public): GET https://files.whoisfreaks.com/v3.4/status
// Run (public endpoint, no API key needed): npx tsx DatabaseFileStatus.ts
import { AccountApi, ResponseError } from "whoisfreaks";

// Public endpoint: no API key needed.
const api = new AccountApi();

// databaseFileStatus() takes no parameters.
async function main(): Promise<void> {
  const result = await api.databaseFileStatus();
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
