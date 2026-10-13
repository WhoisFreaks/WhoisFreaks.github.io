<?php
// ASN WHOIS Snapshot Status
//
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\DatabasesASNWHOISApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new DatabasesASNWHOISApi(new Client(), $config);

try {
    $result = $api->dbAsnWhoisStatus();
    echo $result, PHP_EOL;  // models print as JSON
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
