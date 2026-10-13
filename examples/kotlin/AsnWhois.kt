// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Run it from the Getting Started project: gradle run -PmainClass=AsnWhoisKt
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.ASNWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = ASNWHOISApi()

    val result = api.asnWhois("as15169")
    println(result)
}
