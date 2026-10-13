# DNS Database Monthly
#
# Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest

require "date"
require "fileutils"
require "whoisfreaks"

# Read the API key from the environment and set it once.
WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = ENV.fetch("WHOISFREAKS_API_KEY")
end

api = WhoisFreaks::DatabasesDNSApi.new

begin
  file = api.db_dns_monthly(date: Date.parse("2026-10-01"))
  # The SDK returns a Tempfile that is deleted when the program exits: copy it.
  save_as = "DbDnsMonthly.csv"
  FileUtils.cp(file.path, save_as)
  puts "Saved #{File.expand_path(save_as)} (#{File.size(save_as)} bytes)"
rescue WhoisFreaks::ApiError => e
  warn "Request failed: HTTP #{e.code} #{e.response_body}"
  exit 1
end
