# portage-ucp-webmcp

**Tag**: web, cli

## 简介

WebMCP as a transport, not a commerce backend. Inbound: registers a Portage-powered store's catalog/cart/checkout tools on the page via document.modelContext, each one calling back into the same Portage::Ucp::Mcp::Server every other transport uses. Outbound: a portage-ucp-client transport that discovers and calls the WebMCP tools any page registers, through whatever browser driver the caller already has (Ferrum, Playwright, Selenium, or a plain JS-evaluating callable). No adapter gem is a dependency.

## 官网

- 主页: https://github.com/tomtom87/Portage/tree/main/portage-ucp-webmcp
- 更新日志: https://github.com/tomtom87/Portage/blob/main/portage-ucp-webmcp/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/portage-ucp-webmcp

## 历史版本号

- 0.1.1 (2026-09-25)
- 0.1.0 (2026-09-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/portage-ucp-webmcp
- gem 安装: `gem install portage-ucp-webmcp`
- Bundler: `gem "portage-ucp-webmcp"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/portage-ucp-webmcp-0.1.1.gem
- 版本锁定: `gem "portage-ucp-webmcp", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
