// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Run it from the Getting Started project: gradle run -PmainClass=DnsBulkKt
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required): request body object
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.DnsBulkRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DNSApi()

    val body = DnsBulkRequest(domainNames = listOf("whoisfreaks.com", "example.com"))
    val result = api.dnsBulk("A,MX,TXT", body)
    println(result)
}
