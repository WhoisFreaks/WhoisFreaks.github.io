// Runnable example: Stream the daily spam threat feed (CSV) (GET /v3.4/stream/threat-feed/spam)
// Run it from the Getting Started project: gradle run -PmainClass=StreamThreatFeedSpamKt
// Parameters for streamThreatFeedSpam (GET /v3.4/stream/threat-feed/spam):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamThreatFeedSpam(LocalDate.of(2026, 10, 1))
    println(result)
}
