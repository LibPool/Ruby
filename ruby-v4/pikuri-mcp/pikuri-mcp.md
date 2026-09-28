# pikuri-mcp

**Tag**: web, networking

## 简介

pikuri-mcp adds Model Context Protocol support to pikuri-core
agents: a +Pikuri::Mcp::Registry+ for declaring stdio + HTTP MCP
servers, the +Pikuri::Mcp::Servers+ runtime that spawns them, a
+Pikuri::Mcp::Synthesizer+ that LLM-fills missing server
descriptions, a +Pikuri::Mcp::Verifier+ that screens server
surfaces for prompt-injection patterns before any tool is
advertised to the LLM, and a +Pikuri::Mcp::Extension+ that wires
everything into a +Pikuri::Agent+ via +c.add_extension(...)+ in
the +Agent.new+ block.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-mcp

## 历史版本号

- 0.1.0 (2026-08-30)
- 0.0.7 (2026-06-11)
- 0.0.6 (2026-06-04)
- 0.0.5 (2026-06-04)
- 0.0.4 (2026-05-29)
- 0.0.3 (2026-05-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-mcp
- gem 安装: `gem install pikuri-mcp`
- Bundler: `gem "pikuri-mcp"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-mcp-0.1.0.gem
- 版本锁定: `gem "pikuri-mcp", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
