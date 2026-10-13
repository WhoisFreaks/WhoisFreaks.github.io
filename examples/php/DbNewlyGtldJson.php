<?php
// Newly Registered gTLD (JSON)
//
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)

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
    $domains = $api->dbNewlyGtldJson('2026-10-01');
    echo implode(PHP_EOL, $domains), PHP_EOL;
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
