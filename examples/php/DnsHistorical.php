<?php
// Historical DNS Lookup
//
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required): Domain to look up.
//   - type (string, required): Comma separated DNS record types to return, for example A,MX,TXT. Defaults to all.
//   - page (integer, optional): Page of results to return. Defaults to 1.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\DNSApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new DNSApi(new Client(), $config);

try {
    $result = $api->dnsHistorical('whoisfreaks.com', 'A,MX,TXT', 1);  // domainName, type, page
    echo $result, PHP_EOL;  // models print as JSON
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
