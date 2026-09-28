# pikuri-lsp

**Tag**: web, serialization

## 简介

pikuri-lsp lets a pikuri agent ask a real language server the
questions grep cannot answer: where is this defined, who calls it,
what does it inherit from. It speaks LSP over a long-lived stdio
child (+Pikuri::Lsp::Connection+ owns the JSON-RPC framing, the
id demux and the reply to server-initiated requests) and models
coordinates once, at the wire boundary, in
+Pikuri::Lsp::Position+ / +Range+ / +Location+.

Read-only by construction: no formatting, no code actions, no
rename, no workspace edits. It reads what the server says and
reports it.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-lsp

## 历史版本号

- 0.1.0 (2026-08-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-lsp
- gem 安装: `gem install pikuri-lsp`
- Bundler: `gem "pikuri-lsp"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-lsp-0.1.0.gem
- 版本锁定: `gem "pikuri-lsp", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
