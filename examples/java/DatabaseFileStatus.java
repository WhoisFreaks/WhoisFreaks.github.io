// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DatabaseFileStatus
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; no API key required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AccountApi;

public class DatabaseFileStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        AccountApi api = new AccountApi(client);

        com.whoisfreaks.client.model.DatabaseFileStatus result = api.databaseFileStatus();
        System.out.println(result);
    }
}
