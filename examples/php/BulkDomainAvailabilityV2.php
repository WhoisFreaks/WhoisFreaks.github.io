<?php
// Bulk Domain Availability Check
//
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required): request body object

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\DomainAvailabilityApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;
use WhoisFreaks\Model\BulkDomainAvailabilityRequest;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new DomainAvailabilityApi(new Client(), $config);

$request = new BulkDomainAvailabilityRequest([
    'domainNames' => ['whoisfreaks.com', 'example.com'],
]);

try {
    $result = $api->bulkDomainAvailabilityV2($request);
    echo $result, PHP_EOL;  // models print as JSON
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
