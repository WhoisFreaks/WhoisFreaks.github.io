// IP WHOIS Snapshot
//
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesIPWHOISAPI.dbIpWhois(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbIpWhois.json.gz")
    try? FileManager.default.removeItem(at: saveAs)
    try FileManager.default.moveItem(at: file, to: saveAs)
    print("Saved \(saveAs.path)")
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}
