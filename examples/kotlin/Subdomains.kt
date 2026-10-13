// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Run it from the Getting Started project: gradle run -PmainClass=SubdomainsKt
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.SubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = SubdomainsApi()

    val result = api.subdomains("whoisfreaks.com", page = 1)
    println(result)
}
