# mailodds

**Tag**: web, security

## 简介

MailOdds provides email validation services to help maintain clean email lists  and improve deliverability. The API performs multiple validation checks including  format verification, domain validation, MX record checking, and disposable email detection.  ## Authentication  All API requests require authentication using a Bearer token. Include your API key  in the Authorization header:  ``` Authorization: Bearer YOUR_API_KEY ```  API keys can be created in the MailOdds dashboard.  ## Rate Limits  Rate limits vary by plan: - Free: 10 requests/minute - Starter: 60 requests/minute   - Pro: 300 requests/minute - Business: 1000 requests/minute - Enterprise: Custom limits  ## Response Format  All responses include: - `schema_version`: API schema version (currently "1.0") - `request_id`: Unique request identifier for debugging  Error responses include: - `error`: Machine-readable error code - `message`: Human-readable error description

## 官网

- 主页: https://openapi-generator.tech
- 文档: https://www.rubydoc.info/gems/mailodds/1.1.0
- RubyGems: https://rubygems.org/gems/mailodds

## 历史版本号

- 1.1.0 (2026-02-08)
- 1.0.0 (2026-02-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/mailodds
- gem 安装: `gem install mailodds`
- Bundler: `gem "mailodds"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/mailodds-1.1.0.gem
- 版本锁定: `gem "mailodds", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
