// Runnable example: Stream a sample of the phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing/sample)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamThreatFeedPhishingSample
// Parameters for streamThreatFeedPhishingSample (GET /v3.4/stream/threat-feed/phishing/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamThreatFeedPhishingSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamThreatFeedPhishingSample(offset, limit); null leaves an optional parameter unset
        String result = api.streamThreatFeedPhishingSample(null, null);
        System.out.println(result);
    }
}
