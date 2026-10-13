// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Run it from the Getting Started project: gradle run -PmainClass=BulkDomainAvailabilityV2Kt
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required): request body object
import com.whoisfreaks.client.apis.DomainAvailabilityApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkDomainAvailabilityRequest

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DomainAvailabilityApi()

    val body = BulkDomainAvailabilityRequest(domainNames = listOf("whoisfreaks.com", "example.com"))
    val result = api.bulkDomainAvailabilityV2(body)
    println(result)
}
