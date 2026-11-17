// Runnable example: IP Reputation Lookup (v2.0) (GET /v2.0/security)
// Run it from the Getting Started project: gradle run -PmainClass=IpReputationV2Kt
// Parameters for ipReputationV2 (GET /v2.0/security):
//   - ip (string, required): IP address to look up.
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = IPReputationApi()

    val result = api.ipReputationV2("8.8.8.8")
    println(result)
}
