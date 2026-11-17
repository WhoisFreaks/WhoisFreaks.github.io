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
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DNSAPI.dnsLive(type: "A,MX,TXT", domainName: "whoisfreaks.com")
    print(String(decoding: try CodableHelper.jsonEncoder.encode(result), as: UTF8.self))
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}
