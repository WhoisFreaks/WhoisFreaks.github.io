// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsReverse
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.ReverseDnsResponse;

public class DnsReverse {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsReverse(value, type, exact, page, format); null leaves an optional parameter unset
        ReverseDnsResponse result = api.dnsReverse("8.8.8.8", "a", null, 1, null);
        System.out.println(result);
    }
}
