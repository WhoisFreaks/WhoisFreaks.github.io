# Download the daily spam threat feed (CSV)
#
# Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
#   - date (string, optional): Feed date (yyyy-MM-dd); omit for the full dump of the feed

require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesThreatFeedApi.new

begin
  file = api.download_threat_feed_spam(date: "2026-10-01")
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DownloadThreatFeedSpam.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
