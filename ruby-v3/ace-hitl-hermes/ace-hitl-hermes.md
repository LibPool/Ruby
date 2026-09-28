# ace-hitl-hermes

**Tag**: filesystem

## 简介

ace-hitl-hermes treats the shared lab <-> hermes folder as the HITL transport: a message is a file, the address is <machine>/<folder>/<id>, delivery is push, and ACK is deletion. The plugin owns the channel registry, notification texts, and the versioned message formats (ace.hitl.hermes.message/v1), with atomic same-directory tmp+rename writes, fail-closed validation, quarantine, and bounded retries.

## 官网

- 主页: https://github.com/cs3b/ace
- 源码仓库: https://github.com/cs3b/ace/tree/main/ace-hitl-hermes/
- 更新日志: https://github.com/cs3b/ace/blob/main/ace-hitl-hermes/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/ace-hitl-hermes

## 历史版本号

- 0.1.0 (2026-09-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/ace-hitl-hermes
- gem 安装: `gem install ace-hitl-hermes`
- Bundler: `gem "ace-hitl-hermes"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/ace-hitl-hermes-0.1.0.gem
- 版本锁定: `gem "ace-hitl-hermes", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
