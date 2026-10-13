// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpWhoisStatusKt
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPWHOISApi()

    val result = api.dbIpWhoisStatus()
    println(result)
}
