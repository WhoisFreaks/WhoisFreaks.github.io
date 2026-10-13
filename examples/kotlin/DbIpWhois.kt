// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpWhoisKt
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesIPWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPWHOISApi()

    val download = api.dbIpWhois(LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbIpWhois.json.gz"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}
