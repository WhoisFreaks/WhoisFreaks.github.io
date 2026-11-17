<?php
// SSL Certificate Lookup
//
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required): Domain to look up.
//   - chain (boolean, optional): Set true to return the full certificate chain, ordered from the end-user certificate to...
//   - sslRaw (boolean, optional): Set true to include the raw OpenSSL response for the domain. Defaults to false.
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\SSLApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new SSLApi(new Client(), $config);

try {
    $result = $api->sslLookup('whoisfreaks.com');
    echo $result, PHP_EOL;  // models print as JSON
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
