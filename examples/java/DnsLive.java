// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsLive
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, optional)
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.DnsResponse;

public class DnsLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsLive(type, domainName, ipAddress, format); null leaves an optional parameter unset
        DnsResponse result = api.dnsLive("A,MX,TXT", "whoisfreaks.com", null, null);
        System.out.println(result);
    }
}
