// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbIpSecurityStatus
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpSecurityApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.SnapshotStatus;

public class DbIpSecurityStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesIpSecurityApi api = new DatabasesIpSecurityApi(client);

        SnapshotStatus result = api.dbIpSecurityStatus();
        System.out.println(result);
    }
}
