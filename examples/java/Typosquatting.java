// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=Typosquatting
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional): Brand or label to find typo variants for. Pass either keyword or pattern, not both.
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters. Pass either keyword or patter...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.TyposquattingApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.TyposquattingResponse;

public class Typosquatting {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        TyposquattingApi api = new TyposquattingApi(client);

        // typosquatting(keyword, pattern, pageToken); null leaves an optional parameter unset
        TyposquattingResponse result = api.typosquatting("whoisfreaks", null, null);
        System.out.println(result);
    }
}
