// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbDroppedJson
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;
import java.util.List;

public class DbDroppedJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);

        // dbDroppedJson(date, tlds); null leaves an optional parameter unset
        List<String> result = api.dbDroppedJson(LocalDate.of(2026, 10, 1), null);
        System.out.println(result);
    }
}
