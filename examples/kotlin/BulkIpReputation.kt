// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Run it from the Getting Started project: gradle run -PmainClass=BulkIpReputationKt
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkGeolocationRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = IPReputationApi()

    val body = BulkGeolocationRequest(ips = listOf("8.8.8.8", "1.1.1.1"))
    val result = api.bulkIpReputation(body)
    println(result)
}
