// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbNewlyCctldJson
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;
import java.util.List;

public class DbNewlyCctldJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);

        // dbNewlyCctldJson(date, tlds); null leaves an optional parameter unset
        List<String> result = api.dbNewlyCctldJson(LocalDate.of(2026, 10, 1), null);
        System.out.println(result);
    }
}
