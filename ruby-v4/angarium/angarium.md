# angarium

**Tag**: web, testing, networking, tooling

## 简介

The moment "just POST from a background job" ships to production, the gaps start showing: your customers need signatures they can verify, failed deliveries need to back off and retry for hours, secrets need to rotate without downtime, an endpoint URL shouldn't be able to reach your internal network, and sooner or later someone asks "did we actually send it?". Angarium is a Rails engine that handles all of it, and signs to the Standard Webhooks spec, so your receivers verify with off-the-shelf libraries in any language and you never write verification docs of your own. That conformance is enforced in CI: any drift from the spec fails the build.

## 官网

- 主页: https://github.com/radioactive-labs/angarium
- 文档: https://github.com/radioactive-labs/angarium#readme
- 更新日志: https://github.com/radioactive-labs/angarium/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/radioactive-labs/angarium/issues
- RubyGems: https://rubygems.org/gems/angarium

## 历史版本号

- 0.3.0 (2026-07-08)
- 0.2.0 (2026-07-07)
- 0.1.0 (2026-07-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/angarium
- gem 安装: `gem install angarium`
- Bundler: `gem "angarium"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/angarium-0.3.0.gem
- 版本锁定: `gem "angarium", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
