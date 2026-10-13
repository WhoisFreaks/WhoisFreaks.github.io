// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Run it from the Getting Started project: gradle run -PmainClass=DatabaseFileStatusKt
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; no API key required)
import com.whoisfreaks.client.apis.AccountApi

fun main() {
    // Public endpoint: no API key needed.
    val api = AccountApi()

    val result = api.databaseFileStatus()
    println(result)
}
