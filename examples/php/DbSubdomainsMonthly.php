<?php
// Subdomains Monthly
//
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\DatabasesSubdomainsApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new DatabasesSubdomainsApi(new Client(), $config);

try {
    $file = $api->dbSubdomainsMonthly('2026-10-01');
    // The SDK streams the download into a temporary file: copy it somewhere permanent.
    $saveAs = 'DbSubdomainsMonthly.csv';
    copy($file->getPathname(), $saveAs);
    echo 'Saved ', realpath($saveAs), ' (', filesize($saveAs), ' bytes)', PHP_EOL;
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
