<?php
// IP to City Snapshot
//
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\DatabasesIPGeolocationApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new DatabasesIPGeolocationApi(new Client(), $config);

try {
    $file = $api->dbIpCity('2026-10-01');
    // The SDK streams the download into a temporary file: copy it somewhere permanent.
    $saveAs = 'DbIpCity.zip';
    copy($file->getPathname(), $saveAs);
    echo 'Saved ', realpath($saveAs), ' (', filesize($saveAs), ' bytes)', PHP_EOL;
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
