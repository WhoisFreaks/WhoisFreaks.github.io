// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Run it from the Getting Started project: gradle run -PmainClass=DownloadThreatFeedSpamKt
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed
import com.whoisfreaks.client.apis.DatabasesThreatFeedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesThreatFeedApi()

    val download = api.downloadThreatFeedSpam(date = "2026-10-01")
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DownloadThreatFeedSpam.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}
