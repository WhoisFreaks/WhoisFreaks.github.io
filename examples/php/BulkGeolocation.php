<?php
// Bulk IP Geolocation
//
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required): request body object

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\GeolocationApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;
use WhoisFreaks\Model\BulkGeolocationRequest;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new GeolocationApi(new Client(), $config);

$request = new BulkGeolocationRequest([
    'ips' => ['8.8.8.8', '1.1.1.1'],
]);

try {
    $results = $api->bulkGeolocation($request);
    foreach ($results as $result) {
        echo $result, PHP_EOL;  // models print as JSON
    }
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
