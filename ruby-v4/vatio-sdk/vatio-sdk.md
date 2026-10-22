# vatio-sdk

**Tag**: web, cli, networking

## 简介

Vatio holds only the public half of your signing key, so it can verify a
token and never mint one. Everything dangerous about that arrangement is
therefore on your side: this gem signs the token for the widget and
verifies the same token back on your own API.

`require "vatio/server"` adds the opt-in client for the server API --
having the agent write to a contact first on WhatsApp -- and the
receiver for its signed webhooks, on Net::HTTP and nothing else.

## 官网

- 主页: https://github.com/vatio-ai/ruby
- 文档: https://vatio.ai/docs/sdk/ruby
- 问题追踪: https://github.com/vatio-ai/ruby/issues
- RubyGems: https://rubygems.org/gems/vatio-sdk

## 历史版本号

- 0.6.0 (2026-10-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/vatio-sdk
- gem 安装: `gem install vatio-sdk`
- Bundler: `gem "vatio-sdk"`
- 最新版本: 0.6.0
- 最新版归档: https://rubygems.org/downloads/vatio-sdk-0.6.0.gem
- 版本锁定: `gem "vatio-sdk", "~> 0.6.0"`
- 中央仓库: https://rubygems.org/
