// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Run it from the Getting Started project: gradle run -PmainClass=DbExpiredKt
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesExpiringDroppedApi()

    val download = api.dbExpired(true, date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbExpired.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}
