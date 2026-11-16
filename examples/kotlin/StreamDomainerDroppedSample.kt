// Runnable example: Stream a sample of dropped domains (CSV) (GET /v3.3/stream/domainer/sample/dropped)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerDroppedSampleKt
// Parameters for streamDomainerDroppedSample (GET /v3.3/stream/domainer/sample/dropped):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerDroppedSample()
    println(result)
}
