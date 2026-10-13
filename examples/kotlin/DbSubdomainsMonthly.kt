// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Run it from the Getting Started project: gradle run -PmainClass=DbSubdomainsMonthlyKt
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesSubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesSubdomainsApi()

    val download = api.dbSubdomainsMonthly(date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbSubdomainsMonthly.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}
