// Runnable example: Stream the daily phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamThreatFeedPhishing
// Parameters for streamThreatFeedPhishing (GET /v3.4/stream/threat-feed/phishing):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;

import java.time.LocalDate;

public class StreamThreatFeedPhishing {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamThreatFeedPhishing(date, offset, limit); null leaves an optional parameter unset
        String result = api.streamThreatFeedPhishing(LocalDate.of(2026, 10, 1), null, null);
        System.out.println(result);
    }
}
