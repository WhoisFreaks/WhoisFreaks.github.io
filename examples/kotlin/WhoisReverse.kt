// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Run it from the Getting Started project: gradle run -PmainClass=WhoisReverseKt
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = WHOISApi()

    val result = api.whoisReverse("whoisfreaks", page = 1)
    println(result)
}
