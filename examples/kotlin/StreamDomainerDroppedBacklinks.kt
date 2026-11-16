// Runnable example: Stream dropped domains with backlinks (CSV) (GET /v3.3/stream/domainer/dropped/backlinks)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerDroppedBacklinksKt
// Parameters for streamDomainerDroppedBacklinks (GET /v3.3/stream/domainer/dropped/backlinks):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi
import com.whoisfreaks.client.infrastructure.ApiClient
import java.time.LocalDate

fun main() {
    ApiClient.apiKey["apiKey"] = System.getenv("WHOISFREAKS_API_KEY")  // set once, sent with every call
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerDroppedBacklinks(LocalDate.of(2026, 10, 1))
    println(result)
}
