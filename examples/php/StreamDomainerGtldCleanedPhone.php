<?php
// Stream cleaned newly registered gTLD domains with a phone (CSV)
//
// Parameters for streamDomainerGtldCleanedPhone (GET /v3.3/stream/domainer/gtld/cleaned/phone):
//   - date (string, required): yyyy-MM-dd. Streaming always requires a date, unlike the download endpoints.
//   - whois (boolean, optional): true streams the full WHOIS record per domain with a CSV header row; false streams only...
//   - offset (integer, optional): Data rows to skip from the start of the file. The header row is never counted. Rows are...
//   - limit (integer, optional): Maximum data rows to return. Omit for the whole file. limit=0 returns the header row on...

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\DatabasesStreamingApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new DatabasesStreamingApi(new Client(), $config);

try {
    $result = $api->streamDomainerGtldCleanedPhone('2026-10-01');
    echo $result, PHP_EOL;
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
