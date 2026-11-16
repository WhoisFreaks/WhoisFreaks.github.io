// Runnable example: Historical DNS Lookup (v2.2) (GET /v2.2/dns/historical)
// Run it from the Getting Started project: gradle run -PmainClass=DnsHistoricalV22Kt
// Parameters for dnsHistoricalV22 (GET /v2.2/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - sort (string (one of: asc, desc), optional): Sort direction. Omit to leave the results unsorted.
//   - sortBy (string (one of: firstSeen, lastSeen), optional): Field to sort on. Only applies when sort is given.
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val result = api.dnsHistoricalV22("whoisfreaks.com", "A,MX,TXT", page = 1)
    println(result)
}
