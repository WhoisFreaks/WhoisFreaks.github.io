// Runnable example: Stream a sample of the phishing threat feed (CSV) (GET /v3.4/stream/threat-feed/phishing/sample)
// Run it from the Getting Started project: gradle run -PmainClass=StreamThreatFeedPhishingSampleKt
// Parameters for streamThreatFeedPhishingSample (GET /v3.4/stream/threat-feed/phishing/sample):
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamThreatFeedPhishingSample()
    println(result)
}
