# mcp_toolkit

**Tag**: web, testing, security, serialization, networking

## 简介

mcp_toolkit extracts the shared MCP-server framework that Smily's apps grew
independently: a Streamable-HTTP transport, cache-backed sessions, central-app
token introspection (satellite + authority roles), a registry-driven
"generic tools over N resources" dispatcher, and an injectable serializer DSL.
It wraps the official `mcp` gem as the JSON-RPC core so each app ships only its
serializers, resource registrations, and scope blocks.

## 官网

- 主页: https://github.com/BookingSync/mcp_toolkit
- 更新日志: https://github.com/BookingSync/mcp_toolkit/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/mcp_toolkit

## 历史版本号

- 0.6.2 (2026-08-28)
- 0.6.1 (2026-07-20)
- 0.6.0 (2026-07-17)
- 0.5.0 (2026-07-14)
- 0.4.0 (2026-07-08)
- 0.3.0 (2026-07-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/mcp_toolkit
- gem 安装: `gem install mcp_toolkit`
- Bundler: `gem "mcp_toolkit"`
- 最新版本: 0.6.2
- 最新版归档: https://rubygems.org/downloads/mcp_toolkit-0.6.2.gem
- 版本锁定: `gem "mcp_toolkit", "~> 0.6.2"`
- 中央仓库: https://rubygems.org/
