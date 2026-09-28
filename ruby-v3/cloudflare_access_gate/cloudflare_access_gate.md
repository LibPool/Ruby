# cloudflare_access_gate

**Tag**: web, testing, security, devops

## 简介

Rack middleware that gates a Sidekiq (or any Rack) dashboard behind
Cloudflare Access: it validates the Cf-Access-Jwt-Assertion JWT against your
team's JWKS, issuer, and audience (fail-closed) and audit-logs every request
that gets through. No Rails or logging-library dependency at runtime.

## 官网

- 主页: https://github.com/homebotapp/cloudflare_access_gate
- 更新日志: https://github.com/homebotapp/cloudflare_access_gate/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/homebotapp/cloudflare_access_gate/issues
- RubyGems: https://rubygems.org/gems/cloudflare_access_gate

## 历史版本号

- 0.2.1 (2026-08-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/cloudflare_access_gate
- gem 安装: `gem install cloudflare_access_gate`
- Bundler: `gem "cloudflare_access_gate"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/cloudflare_access_gate-0.2.1.gem
- 版本锁定: `gem "cloudflare_access_gate", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
