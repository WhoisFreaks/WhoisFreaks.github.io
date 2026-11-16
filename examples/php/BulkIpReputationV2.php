<?php
// Bulk IP Reputation (v2.0)
//
// Parameters for bulkIpReputationV2 (POST /v2.0/security):
//   - body: BulkGeolocationRequest (required): request body object

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\IPReputationApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;
use WhoisFreaks\Model\BulkGeolocationRequest;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new IPReputationApi(new Client(), $config);

$request = new BulkGeolocationRequest([
    'ips' => ['1.1.1.1', '2.2.2.2', '8.8.8.8'],
]);

try {
    $results = $api->bulkIpReputationV2($request);
    foreach ($results as $result) {
        echo $result, PHP_EOL;  // models print as JSON
    }
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
