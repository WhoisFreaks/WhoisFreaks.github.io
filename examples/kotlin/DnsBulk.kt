// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Run it from the Getting Started project: gradle run -PmainClass=DnsBulkKt
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - cname_depth (integer, optional): How many CNAME links to follow before returning the records they point at. 0, the defau...
//   - isAuthoritative (boolean, optional): Set true to read the records from each zone's own nameservers instead of a recursive re...
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
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
