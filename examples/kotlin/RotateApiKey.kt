// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Run it from the Getting Started project: gradle run -PmainClass=RotateApiKeyKt
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.AccountApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = AccountApi()

    val newKey = api.rotateApiKey()
    // The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.
    println("New API key: $newKey")
}
