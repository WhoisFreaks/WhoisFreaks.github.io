// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Run it from the Getting Started project: gradle run -PmainClass=DbNewlyGtldKt
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required): Set true for the file with full WHOIS records, false for domain names only.
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional): Comma separated TLDs to limit the file to, for example com,net. Every TLD is included w...
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesNewlyRegisteredApi()

    val download = api.dbNewlyGtld(true, date = LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbNewlyGtld.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}
