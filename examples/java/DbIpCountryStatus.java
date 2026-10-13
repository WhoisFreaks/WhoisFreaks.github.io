// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbIpCountryStatus
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SnapshotStatus;

public class DbIpCountryStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);

        SnapshotStatus result = api.dbIpCountryStatus();
        System.out.println(result);
    }
}
