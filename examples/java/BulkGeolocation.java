// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=BulkGeolocation
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.GeolocationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkGeolocationRequest;
import com.whoisfreaks.client.model.GeolocationResponse;

import java.util.Arrays;
import java.util.List;

public class BulkGeolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        GeolocationApi api = new GeolocationApi(client);

        BulkGeolocationRequest body = new BulkGeolocationRequest()
            .ips(Arrays.asList("8.8.8.8", "1.1.1.1"));
        List<GeolocationResponse> result = api.bulkGeolocation(body);
        System.out.println(result);
    }
}
