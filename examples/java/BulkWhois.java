// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=BulkWhois
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkWhoisRequest;
import com.whoisfreaks.client.model.BulkWhoisResponse;

import java.util.Arrays;

public class BulkWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        WhoisApi api = new WhoisApi(client);

        BulkWhoisRequest body = new BulkWhoisRequest()
            .domainNames(Arrays.asList("whoisfreaks.com", "jfreaks.com"));
        // bulkWhois(bulkWhoisRequest, format); null leaves an optional parameter unset
        BulkWhoisResponse result = api.bulkWhois(body, null);
        System.out.println(result);
    }
}
