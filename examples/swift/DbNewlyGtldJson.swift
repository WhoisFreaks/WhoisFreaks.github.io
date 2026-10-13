// Newly Registered gTLD (JSON)
//
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let domains = try await DatabasesNewlyRegisteredAPI.dbNewlyGtldJson(date: OpenAPIDateWithoutTime(rawValue: "2026-10-01")!)
    print(domains.joined(separator: "\n"))
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}
