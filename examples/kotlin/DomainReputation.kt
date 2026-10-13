// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Run it from the Getting Started project: gradle run -PmainClass=DomainReputationKt
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DomainReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DomainReputationApi()

    val result = api.domainReputation("amazon.com")
    println(result)
}
