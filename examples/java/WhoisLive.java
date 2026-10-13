// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=WhoisLive
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.WhoisResponse;

public class WhoisLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        WhoisApi api = new WhoisApi(client);

        // whoisLive(domainName, format); null leaves an optional parameter unset
        WhoisResponse result = api.whoisLive("whoisfreaks.com", null);
        System.out.println(result);
    }
}
