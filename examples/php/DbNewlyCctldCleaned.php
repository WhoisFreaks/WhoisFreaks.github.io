<?php
// Newly Registered ccTLD Cleaned WHOIS (CSV)
//
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\DatabasesNewlyRegisteredApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new DatabasesNewlyRegisteredApi(new Client(), $config);

try {
    $file = $api->dbNewlyCctldCleaned('2026-10-01');
    // The SDK streams the download into a temporary file: copy it somewhere permanent.
    $saveAs = 'DbNewlyCctldCleaned.csv';
    copy($file->getPathname(), $saveAs);
    echo 'Saved ', realpath($saveAs), ' (', filesize($saveAs), ' bytes)', PHP_EOL;
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
