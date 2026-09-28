# terret-acp

**Tag**: web, serialization, networking

## 简介

The second interface (plan §9.1): an ACP v1 server so an editor can drive a Terret agent over JSON-RPC 2.0 on stdio. Newline-delimited framing, session/new spawns a durable agent, session/prompt pends the whole turn, session/update notifications projected from the session log. Consumes the same two seams the socket does with no change to core, which is the standing proof that the interface is not privileged. Zero runtime dependencies beyond stdlib json.

## 官网

- 主页: https://terret.org
- 源码仓库: https://github.com/terret-org/terret
- 问题追踪: https://github.com/terret-org/terret/issues
- RubyGems: https://rubygems.org/gems/terret-acp

## 历史版本号

- 0.1.0 (2026-08-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/terret-acp
- gem 安装: `gem install terret-acp`
- Bundler: `gem "terret-acp"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/terret-acp-0.1.0.gem
- 版本锁定: `gem "terret-acp", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
