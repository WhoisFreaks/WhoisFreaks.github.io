// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=RotateApiKey
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AccountApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

public class RotateApiKey {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        AccountApi api = new AccountApi(client);

        String newKey = api.rotateApiKey();
        // The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.
        System.out.println("New API key: " + newKey);
    }
}
