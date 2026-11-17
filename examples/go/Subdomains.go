// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required): Domain whose subdomains you want.
//   - after (string, optional): Only return records created after this date, in YYYY-MM-DD format. Defaults to the olde...
//   - before (string, optional): Only return records created before this date, in YYYY-MM-DD format. Defaults to today, ...
//   - status (string (one of: active, inactive), optional): Limit results to active or inactive subdomains. Both are returned when the parameter is...
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

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

	result, _, err := client.SubdomainsAPI.Subdomains(ctx).Domain("whoisfreaks.com").Page(1).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}
