// Newly Registered gTLD (CSV)
//
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let file = try await DatabasesNewlyRegisteredAPI.dbNewlyGtld(whois: true, date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    // The SDK saves the download under the caches directory: move it somewhere permanent.
    let saveAs = URL(fileURLWithPath: "DbNewlyGtld.csv")
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
