<?php
// Download the daily phishing threat feed (CSV)
//
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\DatabasesThreatFeedApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new DatabasesThreatFeedApi(new Client(), $config);

try {
    $file = $api->downloadThreatFeedPhishing('2026-10-01');
    // The SDK streams the download into a temporary file: copy it somewhere permanent.
    $saveAs = 'DownloadThreatFeedPhishing.csv';
    copy($file->getPathname(), $saveAs);
    echo 'Saved ', realpath($saveAs), ' (', filesize($saveAs), ' bytes)', PHP_EOL;
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
