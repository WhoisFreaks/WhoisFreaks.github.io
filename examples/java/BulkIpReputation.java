// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=BulkIpReputation
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkGeolocationRequest;
import com.whoisfreaks.client.model.IpReputationResponse;

import java.util.Arrays;
import java.util.List;

public class BulkIpReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        IpReputationApi api = new IpReputationApi(client);

        BulkGeolocationRequest body = new BulkGeolocationRequest()
            .ips(Arrays.asList("8.8.8.8", "1.1.1.1"));
        List<IpReputationResponse> result = api.bulkIpReputation(body);
        System.out.println(result);
    }
}
