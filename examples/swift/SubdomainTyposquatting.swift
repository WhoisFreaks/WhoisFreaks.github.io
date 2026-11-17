// Subdomain Typosquatting Lookup
//
// Parameters for subdomainTyposquatting (GET /v3.0/subdomains/typos):
//   - keyword (string, optional): Brand or label to find typo variants for. 3 to 63 characters, letters, digits and hyphe...
//   - pattern (string, optional): Wildcard search string, where '*' matches any characters and '?' matches one. At most 2...
//   - pageToken (string, optional): Token from nextPageToken in the previous response, needed from page 2 onward. Send it w...
//   - fetch_size (integer, optional): Subdomains per page. 100 when the parameter is left out, and values above 10000 are cap...
//
// Top-level code for Sources/<YourTarget>/main.swift (see Getting Started).

import Foundation
import WhoisFreaks

// Read the API key from the environment and set it once.
WhoisFreaksAPI.apiKey = ProcessInfo.processInfo.environment["WHOISFREAKS_API_KEY"]

do {
    let result = try await TyposquattingAPI.subdomainTyposquatting(keyword: "paypal")
    print(String(decoding: try CodableHelper.jsonEncoder.encode(result), as: UTF8.self))
} catch ErrorResponse.error(let status, let data, _, let underlying) {
    let body = data.map { String(decoding: $0, as: UTF8.self) } ?? "\(underlying)"
    print("Request failed: HTTP \(status) \(body)")
    exit(1)
} catch {
    print("Request failed: \(error)")
    exit(1)
}
