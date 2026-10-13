// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=Subdomains
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.SubdomainsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SubdomainsResponse;

public class Subdomains {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        SubdomainsApi api = new SubdomainsApi(client);

        // subdomains(domain, after, before, status, page, format); null leaves an optional parameter unset
        SubdomainsResponse result = api.subdomains("whoisfreaks.com", null, null, null, 1, null);
        System.out.println(result);
    }
}
