// Bulk DNS Lookup
//
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required): request body object
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

let request = DnsBulkRequest(domainNames: ["whoisfreaks.com", "example.com"])

do {
    let result = try await DNSAPI.dnsBulk(type: "A,MX,TXT", dnsBulkRequest: request)
    print(String(decoding: try CodableHelper.jsonEncoder.encode(result), as: UTF8.self))
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}
