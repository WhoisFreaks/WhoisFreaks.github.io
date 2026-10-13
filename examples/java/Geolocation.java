// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=Geolocation
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.GeolocationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.GeolocationResponse;

public class Geolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        GeolocationApi api = new GeolocationApi(client);

        GeolocationResponse result = api.geolocation("8.8.8.8");
        System.out.println(result);
    }
}
