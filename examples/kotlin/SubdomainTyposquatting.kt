// Runnable example: Subdomain Typosquatting Lookup (GET /v3.0/subdomains/typos)
// Run it from the Getting Started project: gradle run -PmainClass=SubdomainTyposquattingKt
// Parameters for subdomainTyposquatting (GET /v3.0/subdomains/typos):
//   - keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits and hyphe...
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one. At most 2...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
//   - fetch_size (integer, optional): Subdomains per page. 100 when the parameter is left out, and values above 10000 are cap...
import com.whoisfreaks.client.apis.TyposquattingApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = TyposquattingApi()

    val result = api.subdomainTyposquatting(keyword = "paypal")
    println(result)
}
