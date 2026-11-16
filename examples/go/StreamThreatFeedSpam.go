// Runnable example: Stream the daily spam threat feed (CSV) (GET /v3.4/stream/threat-feed/spam)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for streamThreatFeedSpam (GET /v3.4/stream/threat-feed/spam):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"

	whoisfreaks "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
	// Set the API key once on the context; every call made with ctx sends it.
	ctx := context.WithValue(context.Background(), whoisfreaks.ContextAPIKeys,
		map[string]whoisfreaks.APIKey{"ApiKeyAuth": {Key: os.Getenv("WHOISFREAKS_API_KEY")}})
	client := whoisfreaks.NewAPIClient(whoisfreaks.NewConfiguration())

	result, _, err := client.DatabasesStreamingAPI.StreamThreatFeedSpam(ctx).
		Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}
