// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Run it from the Getting Started project: gradle run -PmainClass=DbIpCountryKt
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesIPGeolocationApi()

    val download = api.dbIpCountry(LocalDate.of(2026, 10, 1))
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DbIpCountry.zip"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}
