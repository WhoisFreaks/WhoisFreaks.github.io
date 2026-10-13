// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbNewlyGtldJson
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;
import java.util.List;

public class DbNewlyGtldJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);

        // dbNewlyGtldJson(date, tlds); null leaves an optional parameter unset
        List<String> result = api.dbNewlyGtldJson(LocalDate.of(2026, 10, 1), null);
        System.out.println(result);
    }
}
