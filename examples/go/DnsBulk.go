// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required): request body object

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

	body := whoisfreaks.NewDnsBulkRequest()
	body.SetDomainNames([]string{"whoisfreaks.com", "example.com"})
	result, _, err := client.DNSAPI.DnsBulk(ctx).Type_("A,MX,TXT").DnsBulkRequest(*body).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}
