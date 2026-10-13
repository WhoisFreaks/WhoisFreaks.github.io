// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsHistorical
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.HistoricalDnsResponse;

public class DnsHistorical {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsHistorical(domainName, type, page, format); null leaves an optional parameter unset
        HistoricalDnsResponse result = api.dnsHistorical("whoisfreaks.com", "A,MX,TXT", 1, null);
        System.out.println(result);
    }
}
