// SSL Certificate Lookup: GET https://api.whoisfreaks.com/v1.0/ssl/live
// Run: WHOISFREAKS_API_KEY=your_api_key node SslLookup.js
const { ApiClient, SSLApi } = require("whoisfreaks-js");

// Set the API key once; the client adds it to every request.
const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = process.env.WHOISFREAKS_API_KEY;
const api = new SSLApi(client);

// sslLookup(domainName, opts)
//   domainName (string, required): Domain to look up
//   opts.chain (boolean, optional): Set true to return the full certificate chain, ordered from the end-user cert...; default false
//   opts.sslRaw (boolean, optional): Set true to include the raw OpenSSL response for the domain. Defaults to false; default false
//   opts.format (string, optional): Response format. JSON when the parameter is left out; one of json, xml; default "json"
async function main() {
  const result = await api.sslLookup("whoisfreaks.com");
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  // API errors carry the HTTP status and the parsed error body
  console.error(err.status ? `HTTP ${err.status}: ${JSON.stringify(err.body)}` : err);
  process.exitCode = 1;
});
