// Runnable example: Bulk IP Reputation (v2.0) (POST /v2.0/security)
// Run it from the Getting Started project: gradle run -PmainClass=BulkIpReputationV2Kt
// Parameters for bulkIpReputationV2 (POST /v2.0/security):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkGeolocationRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = IPReputationApi()

    val body = BulkGeolocationRequest(ips = listOf("1.1.1.1", "2.2.2.2", "8.8.8.8"))
    val result = api.bulkIpReputationV2(body)
    println(result)
}
