// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Run it from the Getting Started project: gradle run -PmainClass=DomainAvailabilityV2Kt
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DomainAvailabilityApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DomainAvailabilityApi()

    val result = api.domainAvailabilityV2("google.com", sug = true, count = 5)
    println(result)
}
