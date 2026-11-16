// Runnable example: Historical DNS Lookup (v2.2) (GET /v2.2/dns/historical)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsHistoricalV22
// Parameters for dnsHistoricalV22 (GET /v2.2/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.HistoricalDnsResponseV2_2;

public class DnsHistoricalV22 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsHistoricalV22(domainName, type, page, sort, sortBy, format); null leaves an optional parameter unset
        HistoricalDnsResponseV2_2 result = api.dnsHistoricalV22("whoisfreaks.com", "A,MX,TXT", 1, null, null, null);
        System.out.println(result);
    }
}
