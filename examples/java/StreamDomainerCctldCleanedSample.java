// Runnable example: Stream a sample of cleaned newly registered ccTLD domains (CSV) (GET /v3.3/stream/domainer/sample/cctld/cleaned)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerCctldCleanedSample
// Parameters for streamDomainerCctldCleanedSample (GET /v3.3/stream/domainer/sample/cctld/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamDomainerCctldCleanedSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerCctldCleanedSample(whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerCctldCleanedSample(null, null, null);
        System.out.println(result);
    }
}
