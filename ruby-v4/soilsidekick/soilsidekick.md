# soilsidekick

**Tag**: web, security, data

## 简介

Agricultural intelligence and soil analysis API with tier-based access control.  ## What's New in 1.2.0 - **Consumer Plant Care APIs**: Three new endpoints addressing top pain points in plant ID apps:   - `/safe-identification`: Toxic lookalike warnings and environmental context   - `/dynamic-care`: Hyper-localized, real-time care recommendations   - `/beginner-guidance`: Judgment-free, jargon-free plant guidance  ## Authentication All endpoints require an API key passed via the `x-api-key` header: ``` x-api-key: ak_your_api_key_here ```  API keys are generated through the dashboard and use the `ak_*` format.  ## Rate Limiting Rate limits are enforced based on your subscription tier: - **Free**: 10 req/min, 100 req/hour, 1,000 req/day - **Starter**: 30 req/min, 500 req/hour, 5,000 req/day - **Pro**: 100 req/min, 2,000 req/hour, 25,000 req/day - **Enterprise**: 500 req/min, 10,000 req/hour, 100,000 req/day  Rate limit information is returned in response headers: - `X-RateLimit-Limit`: Maximum requests in window - `X-RateLimit-Remaining`: Remaining requests in window - `X-RateLimit-Reset`: Unix timestamp when limit resets  ## Response Time SLAs All endpoints return response time headers for performance monitoring: - `X-Response-Time`: Human-readable response time (e.g., "245ms") - `X-Response-Time-Ms`: Response time in milliseconds - `X-Response-Time-Target`: Target response time for this endpoint - `X-Response-Time-Max`: Maximum acceptable response time - `X-Response-Time-Status`: Performance status (`optimal`, `acceptable`, `exceeded`)  ### Response Time Targets by Category  | Category | Target | Maximum | Endpoints | |----------|--------|---------|-----------| | **Fast** | 200ms | 500ms | county-lookup, check-subscription | | **Standard** | 500ms | 1,500ms | get-soil-data, territorial-water-quality | | **Complex** | 2,000ms | 5,000ms | agricultural-intelligence, gpt5-chat, visual-crop-analysis | | **Heavy** | 5,000ms | 15,000ms | live-agricultural-data, generate-vrt-prescription |

## 官网

- 主页: https://openapi-generator.tech
- 文档: https://www.rubydoc.info/gems/soilsidekick/3.0.0
- RubyGems: https://rubygems.org/gems/soilsidekick

## 历史版本号

- 3.0.0 (2026-06-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/soilsidekick
- gem 安装: `gem install soilsidekick`
- Bundler: `gem "soilsidekick"`
- 最新版本: 3.0.0
- 最新版归档: https://rubygems.org/downloads/soilsidekick-3.0.0.gem
- 版本锁定: `gem "soilsidekick", "~> 3.0.0"`
- 中央仓库: https://rubygems.org/
