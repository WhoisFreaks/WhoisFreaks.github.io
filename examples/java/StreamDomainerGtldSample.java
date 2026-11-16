// Runnable example: Stream a sample of newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/sample/gtld)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=StreamDomainerGtldSample
// Parameters for streamDomainerGtldSample (GET /v3.3/stream/domainer/sample/gtld):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesStreamingApi;

public class StreamDomainerGtldSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        // Public endpoint: no API key needed.
        DatabasesStreamingApi api = new DatabasesStreamingApi(client);

        // streamDomainerGtldSample(whois, offset, limit); null leaves an optional parameter unset
        String result = api.streamDomainerGtldSample(null, null, null);
        System.out.println(result);
    }
}
