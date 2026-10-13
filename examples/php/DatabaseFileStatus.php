<?php
// Database File Status (Public)
//
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; no API key required)

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\AccountApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
// (This endpoint is public, so the key is not sent with this request.)
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new AccountApi(new Client(), $config);

try {
    $result = $api->databaseFileStatus();
    echo $result, PHP_EOL;  // models print as JSON
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
