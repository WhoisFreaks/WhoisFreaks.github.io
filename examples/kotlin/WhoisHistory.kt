// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Run it from the Getting Started project: gradle run -PmainClass=WhoisHistoryKt
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = WHOISApi()

    val result = api.whoisHistory("whoisfreaks.com")
    println(result)
}
