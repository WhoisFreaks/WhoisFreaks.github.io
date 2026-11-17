// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Run it from the Getting Started project: gradle run -PmainClass=IpWhoisKt
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required): IP address to look up.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.
import com.whoisfreaks.client.apis.IPWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = IPWHOISApi()

    val result = api.ipWhois("8.8.8.8")
    println(result)
}
