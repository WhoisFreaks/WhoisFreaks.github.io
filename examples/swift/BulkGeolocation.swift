// Bulk IP Geolocation
//
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required): request body object
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

let request = BulkGeolocationRequest(ips: ["8.8.8.8", "1.1.1.1"])

do {
    let result = try await GeolocationAPI.bulkGeolocation(bulkGeolocationRequest: request)
    print(String(decoding: try CodableHelper.jsonEncoder.encode(result), as: UTF8.self))
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}
