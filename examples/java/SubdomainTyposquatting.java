// Runnable example: Subdomain Typosquatting Lookup (GET /v3.0/subdomains/typos)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=SubdomainTyposquatting
// Parameters for subdomainTyposquatting (GET /v3.0/subdomains/typos):
//   - keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits and hyphe...
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one. At most 2...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
//   - fetch_size (integer, optional): Subdomains per page. 100 when the parameter is left out, and values above 10000 are cap...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.TyposquattingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.TyposquatSubdomainsResponse;

public class SubdomainTyposquatting {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        TyposquattingApi api = new TyposquattingApi(client);

        // subdomainTyposquatting(keyword, pattern, pageToken, fetch_size); null leaves an optional parameter unset
        TyposquatSubdomainsResponse result = api.subdomainTyposquatting("paypal", null, null, null);
        System.out.println(result);
    }
}
