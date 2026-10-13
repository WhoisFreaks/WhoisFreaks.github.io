// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DomainReputation
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DomainReputationApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.DomainReputationResponse;

public class DomainReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DomainReputationApi api = new DomainReputationApi(client);

        // domainReputation(domainName, format); null leaves an optional parameter unset
        DomainReputationResponse result = api.domainReputation("amazon.com", null);
        System.out.println(result);
    }
}
