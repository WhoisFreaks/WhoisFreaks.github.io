// Runnable example: Stream cleaned newly registered gTLD domains with an email (CSV) (GET /v3.3/stream/domainer/gtld/cleaned/email)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerGtldCleanedEmail
// Parameters for streamDomainerGtldCleanedEmail (GET /v3.3/stream/domainer/gtld/cleaned/email):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamDomainerGtldCleanedEmail {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerGtldCleanedEmail(date, whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerGtldCleanedEmail(LocalDate.of(2026, 10, 1), null, null, null);
        System.out.println(result);
    }
}
