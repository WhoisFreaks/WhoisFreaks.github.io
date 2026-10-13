// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Run it from the Getting Started project: gradle run -PmainClass=DnsReverseKt
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val result = api.dnsReverse("8.8.8.8", DNSApi.TypeDnsReverse.a, page = 1)
    println(result)
}
