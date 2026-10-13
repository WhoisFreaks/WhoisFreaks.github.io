// Historical DNS Lookup
//
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await DNSAPI.dnsHistorical(domainName: "whoisfreaks.com", type: "A,MX,TXT", page: 1)
    print(String(decoding: try CodableHelper.jsonEncoder.encode(result), as: UTF8.self))
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}
