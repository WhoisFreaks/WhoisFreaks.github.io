// Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
// Run it from the Getting Started project: gradle run -PmainClass=DownloadThreatFeedPhishingSampleKt
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesThreatFeedApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.io.File

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesThreatFeedApi()

    val download = api.downloadThreatFeedPhishingSample()
    // The SDK saves the response to a temporary file that is deleted on exit: copy it.
    val target = download.copyTo(File("DownloadThreatFeedPhishingSample.csv"), overwrite = true)
    println("Saved ${target.length()} bytes to ${target.absolutePath}")
}
