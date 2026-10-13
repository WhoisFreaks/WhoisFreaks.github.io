// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Run it from the Getting Started project: gradle run -PmainClass=DnsHistoricalKt
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val result = api.dnsHistorical("whoisfreaks.com", "A,MX,TXT", page = 1)
    println(result)
}
