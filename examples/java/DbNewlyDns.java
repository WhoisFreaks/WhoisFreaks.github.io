// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DbNewlyDns
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDate;

public class DbNewlyDns {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);

        File download = api.dbNewlyDns(LocalDate.of(2026, 10, 1));
        // The SDK saves the response to a temporary file: move it where you want it.
        Path target = Paths.get("DbNewlyDns.json");
        Files.move(download.toPath(), target, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved " + Files.size(target) + " bytes to " + target.toAbsolutePath());
    }
}
