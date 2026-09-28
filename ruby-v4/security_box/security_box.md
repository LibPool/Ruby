# security_box

**Tag**: security, networking, filesystem

## 简介

SecurityBox runs untrusted Ruby code inside a ruby.wasm (wasm32-unknown-wasip1) module via the wasmtime gem. The guest has no filesystem, network, processes, threads or sockets, and the host enforces CPU (fuel), wall-clock, memory and output-size limits, always receiving a structured Result back.

## 官网

- 主页: https://github.com/juneira/security_box
- 更新日志: https://github.com/juneira/security_box/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/security_box

## 历史版本号

- 0.6.0 (2026-09-22)
- 0.5.0 (2026-09-20)
- 0.3.0 (2026-09-15)
- 0.2.0 (2026-09-14)
- 0.1.0 (2026-09-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/security_box
- gem 安装: `gem install security_box`
- Bundler: `gem "security_box"`
- 最新版本: 0.6.0
- 最新版归档: https://rubygems.org/downloads/security_box-0.6.0.gem
- 版本锁定: `gem "security_box", "~> 0.6.0"`
- 中央仓库: https://rubygems.org/
