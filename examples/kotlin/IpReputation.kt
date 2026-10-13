// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Run it from the Getting Started project: gradle run -PmainClass=IpReputationKt
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = IPReputationApi()

    val result = api.ipReputation("8.8.8.8")
    println(result)
}
