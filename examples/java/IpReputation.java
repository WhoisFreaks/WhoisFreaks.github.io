// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=IpReputation
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.IpReputationResponse;

public class IpReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        IpReputationApi api = new IpReputationApi(client);

        IpReputationResponse result = api.ipReputation("8.8.8.8");
        System.out.println(result);
    }
}
