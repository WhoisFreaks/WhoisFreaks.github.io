// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; no API key required)

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

	whoisfreaks "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
	// Public endpoint: no API key needed.
	ctx := context.Background()
	client := whoisfreaks.NewAPIClient(whoisfreaks.NewConfiguration())

	result, _, err := client.AccountAPI.DatabaseFileStatus(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	out, _ := json.MarshalIndent(result, "", "  ")
	fmt.Println(string(out))
}
