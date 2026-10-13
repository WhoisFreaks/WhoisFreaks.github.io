// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=AccountUsage
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AccountApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.AccountUsageResponse;

public class AccountUsage {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        AccountApi api = new AccountApi(client);

        AccountUsageResponse result = api.accountUsage();
        System.out.println(result);
    }
}
