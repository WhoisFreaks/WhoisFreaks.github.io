// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpCountryStatusKt
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPGeolocationApi()

    val result = api.dbIpCountryStatus()
    println(result)
}
