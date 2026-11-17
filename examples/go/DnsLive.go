// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, optional): Domain to look up.
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - cnameDepth (integer, optional): How many CNAME links to follow before returning the records they point at. 0, the defau...
//   - relativeRecords (boolean, optional): Keeps the records picked up for other names along the way, such as a CNAME target's own...
//   - isAuthoritative (boolean, optional): Set true to read the records from the zone's own nameservers instead of a recursive res...
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

	result, _, err := client.DNSAPI.DnsLive(ctx).
		DomainName("whoisfreaks.com").Type_("A,MX,TXT").Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}
