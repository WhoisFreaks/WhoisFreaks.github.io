# Download a sample of the phishing threat feed (CSV)
#
# Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
#   (no parameters; the API key is set on the client)

require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesThreatFeedApi.new

begin
  file = api.download_threat_feed_phishing_sample
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DownloadThreatFeedPhishingSample.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
