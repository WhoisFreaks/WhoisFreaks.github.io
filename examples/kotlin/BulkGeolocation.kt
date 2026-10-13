// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Run it from the Getting Started project: gradle run -PmainClass=BulkGeolocationKt
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required): request body object
import com.whoisfreaks.client.apis.GeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkGeolocationRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = GeolocationApi()

    val body = BulkGeolocationRequest(ips = listOf("8.8.8.8", "1.1.1.1"))
    val result = api.bulkGeolocation(body)
    println(result)
}
