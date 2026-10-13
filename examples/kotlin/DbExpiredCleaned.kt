// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=DbExpiredCleanedKt
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesExpiringDroppedApi()

    val download = api.dbExpiredCleaned(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbExpiredCleaned.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}
