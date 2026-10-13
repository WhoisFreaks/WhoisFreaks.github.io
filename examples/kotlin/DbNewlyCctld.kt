// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Run it from the Getting Started project: gradle run -PmainClass=DbNewlyCctldKt
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesNewlyRegisteredApi()

    val download = api.dbNewlyCctld(true, date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbNewlyCctld.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}
