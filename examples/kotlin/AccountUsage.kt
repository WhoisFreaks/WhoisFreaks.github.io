// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Run it from the Getting Started project: gradle run -PmainClass=AccountUsageKt
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.AccountApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = AccountApi()

    val result = api.accountUsage()
    println(result)
}
