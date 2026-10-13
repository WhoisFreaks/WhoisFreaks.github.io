// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Run it from the Getting Started project: gradle run -PmainClass=TyposquattingKt
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import com.whoisfreaks.client.apis.TyposquattingApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = TyposquattingApi()

    val result = api.typosquatting(keyword = "whoisfreaks")
    println(result)
}
