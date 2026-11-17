// Runnable example: IP Reputation Lookup (v2.0) (GET /v2.0/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=IpReputationV2
// Parameters for ipReputationV2 (GET /v2.0/security):
//   - ip (string, required): IP address to look up.
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.IpReputationResponse;

public class IpReputationV2 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        IpReputationApi api = new IpReputationApi(client);

        IpReputationResponse result = api.ipReputationV2("8.8.8.8");
        System.out.println(result);
    }
}
