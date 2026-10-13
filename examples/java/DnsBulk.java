// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsBulk
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkDnsResponse;
import com.whoisfreaks.client.model.DnsBulkRequest;

import java.util.Arrays;

public class DnsBulk {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        DnsBulkRequest body = new DnsBulkRequest()
            .domainNames(Arrays.asList("whoisfreaks.com", "example.com"));
        // dnsBulk(type, dnsBulkRequest, format); null leaves an optional parameter unset
        BulkDnsResponse result = api.dnsBulk("A,MX,TXT", body, null);
        System.out.println(result);
    }
}
