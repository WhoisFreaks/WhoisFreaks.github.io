// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=SslLookup
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.SslApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SslResponse;

public class SslLookup {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        SslApi api = new SslApi(client);

        // sslLookup(domainName, chain, sslRaw, format); null leaves an optional parameter unset
        SslResponse result = api.sslLookup("whoisfreaks.com", null, null, null);
        System.out.println(result);
    }
}
