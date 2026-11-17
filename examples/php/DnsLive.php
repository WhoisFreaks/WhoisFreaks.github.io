<?php
// Live DNS Lookup
//
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, optional): Domain to look up.
//   - ipAddress (string, optional): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - cnameDepth (integer, optional): How many CNAME links to follow before returning the records they point at. 0, the defau...
//   - relativeRecords (boolean, optional): Keeps the records picked up for other names along the way, such as a CNAME target's own...
//   - isAuthoritative (boolean, optional): Set true to read the records from the zone's own nameservers instead of a recursive res...
//   - format (string (one of: json, xml), optional): Response format. JSON when the parameter is left out.

require __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;
use WhoisFreaks\Api\DNSApi;
use WhoisFreaks\ApiException;
use WhoisFreaks\Configuration;

// Read the API key from the environment and set it once.
$config = Configuration::getDefaultConfiguration()
    ->setApiKey('apiKey', getenv('WHOISFREAKS_API_KEY'));

$api = new DNSApi(new Client(), $config);

try {
    $result = $api->dnsLive('A,MX,TXT', 'whoisfreaks.com');  // type, domainName
    echo $result, PHP_EOL;  // models print as JSON
} catch (ApiException $e) {
    fwrite(STDERR, 'Request failed: HTTP ' . $e->getCode() . ' ' . $e->getResponseBody() . PHP_EOL);
    exit(1);
}
