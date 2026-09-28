# parlo-sdk

**Tag**: web, security, serialization, networking, template

## 简介

The Parlo API sends transactional email and manages the sending domains it authenticates from. Marketing campaigns (audiences, templates, broadcasts) are designed and sent from the Parlo dashboard, not this API — the API is transactional-only at launch.  All requests authenticate with a company API key as an HTTP bearer token: `Authorization: Bearer parlo_live_xxx`. Errors return a JSON body of the shape `{ "message": string, "code": string }`.

## 官网

- 主页: https://getparlo.io
- 文档: https://getparlo.io/docs
- RubyGems: https://rubygems.org/gems/parlo-sdk

## 历史版本号

- 1.1.0 (2026-08-25)
- 1.0.0 (2026-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/parlo-sdk
- gem 安装: `gem install parlo-sdk`
- Bundler: `gem "parlo-sdk"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/parlo-sdk-1.1.0.gem
- 版本锁定: `gem "parlo-sdk", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
