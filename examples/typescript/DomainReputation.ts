// Domain Reputation Lookup: GET https://api.whoisfreaks.com/v1/domain/security
// Run: WHOISFREAKS_API_KEY=your_api_key npx tsx DomainReputation.ts
import { Configuration, DomainReputationApi, ResponseError } from "whoisfreaks";

// Set the API key once; the client adds it to every request.
const config = new Configuration({ apiKey: process.env.WHOISFREAKS_API_KEY });
const api = new DomainReputationApi(config);

// domainReputation({ domainName, format? })
//   domainName (string, required): The domain name to assess
//   format ("json" | "xml", optional): default "json"
async function main(): Promise<void> {
  const result = await api.domainReputation({ domainName: "amazon.com" });
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
