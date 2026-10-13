// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Run it from the Getting Started module: save it as main.go, then `go run .`
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)

package main

import (
	"context"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"

	whoisfreaks "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
	// Set the API key once on the context; every call made with ctx sends it.
	ctx := context.WithValue(context.Background(), whoisfreaks.ContextAPIKeys,
		map[string]whoisfreaks.APIKey{"ApiKeyAuth": {Key: os.Getenv("WHOISFREAKS_API_KEY")}})
	client := whoisfreaks.NewAPIClient(whoisfreaks.NewConfiguration())

	file, _, err := client.DatabasesIPGeolocationAPI.DbIpCity(ctx).Date("2026-10-01").Execute()
	if err != nil {
		log.Fatal(err)
	}
	// The SDK saves the response to a temporary file: copy it to its destination.
	defer os.Remove(file.Name())
	defer file.Close()

	out, err := os.Create("DbIpCity.zip")
	if err != nil {
		log.Fatal(err)
	}
	defer out.Close()
	n, err := io.Copy(out, file)
	if err != nil {
		log.Fatal(err)
	}
	path, _ := filepath.Abs(out.Name())
	fmt.Printf("Saved %d bytes to %s\n", n, path)
}
