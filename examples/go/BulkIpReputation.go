// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkGeolocationRequest (required): request body object

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

	body := whoisfreaks.NewBulkGeolocationRequest([]string{"8.8.8.8", "1.1.1.1"})
	result, _, err := client.IPReputationAPI.BulkIpReputation(ctx).
		BulkGeolocationRequest(*body).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}
