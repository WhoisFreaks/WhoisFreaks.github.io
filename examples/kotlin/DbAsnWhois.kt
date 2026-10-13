// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Run it from the Getting Started project: gradle run -PmainClass=DbAsnWhoisKt
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesASNWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesASNWHOISApi()

    val download = api.dbAsnWhois(LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbAsnWhois.json.gz"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}
