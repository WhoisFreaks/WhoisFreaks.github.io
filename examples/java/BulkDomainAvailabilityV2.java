// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=BulkDomainAvailabilityV2
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required): request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DomainAvailabilityApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.BulkDomainAvailabilityRequest;
import com.whoisfreaks.client.model.BulkDomainAvailabilityResponse;

import java.util.Arrays;

public class BulkDomainAvailabilityV2 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DomainAvailabilityApi api = new DomainAvailabilityApi(client);

        BulkDomainAvailabilityRequest body = new BulkDomainAvailabilityRequest()
            .domainNames(Arrays.asList("whoisfreaks.com", "example.com"));
        // bulkDomainAvailabilityV2(bulkDomainAvailabilityRequest, domain, format); null leaves an optional parameter unset
        BulkDomainAvailabilityResponse result = api.bulkDomainAvailabilityV2(body, null, null);
        System.out.println(result);
    }
}
