// Runnable example: Reverse DNS Lookup (v2.3) (GET /v2.3/dns/reverse)
// Run it from the Getting Started project: mvn -q compile exec:java -Dexec.mainClass=DnsReverseV23
// Parameters for dnsReverseV23 (GET /v2.3/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional): When false the value is matched as a substring, which is far slower than an exact match...
//   - page (integer, optional)
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.model.ReverseDnsResponseV2_3;

public class DnsReverseV23 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        ApiKeyAuth auth = (ApiKeyAuth) client.getAuthentication("ApiKeyAuth");
        auth.setApiKey(System.getenv("WHOISFREAKS_API_KEY"));  // set once, sent with every call
        DnsApi api = new DnsApi(client);

        // dnsReverseV23(value, type, exact, page, sort, sortBy, format); null leaves an optional parameter unset
        ReverseDnsResponseV2_3 result = api.dnsReverseV23("8.8.8.8", "a", null, 1, null, null, null);
        System.out.println(result);
    }
}
