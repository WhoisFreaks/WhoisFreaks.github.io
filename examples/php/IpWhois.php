<?php
// IP WHOIS Lookup
//
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\IPWHOISApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new IPWHOISApi(new Client(), $config);

try {
    $result = $api->ipWhois('8.8.8.8');
    echo $result, PHP_EOL;  // models print as JSON
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
