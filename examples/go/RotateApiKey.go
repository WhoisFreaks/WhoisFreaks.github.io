// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)

package main

import (
	"context"
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

	newKey, _, err := client.AccountAPI.RotateApiKey(ctx).Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The old key stops working: store the new one, e.g. in WHOISFREAKS_API_KEY.
	fmt.Println("New API key:", newKey)
}
