// Runnable example: Stream a sample of cleaned newly registered gTLD domains (CSV) (GET /v3.3/stream/domainer/sample/gtld/cleaned)
// Run it from the Getting Started project: gradle run -PmainClass=StreamDomainerGtldCleanedSampleKt
// Parameters for streamDomainerGtldCleanedSample (GET /v3.3/stream/domainer/sample/gtld/cleaned):
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...
import com.whoisfreaks.client.apis.DatabasesStreamingApi

fun main() {
    // Public endpoint: no API key needed.
    val api = DatabasesStreamingApi()

    val result = api.streamDomainerGtldCleanedSample()
    println(result)
}
