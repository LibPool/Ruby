# winipc

**Tag**: web, cli, security, filesystem

## 简介

winipc is a native extension that exposes Windows local inter-process
communication through an ergonomic, safe-by-default Ruby API: duplex named
pipes (byte and message mode, with a server and a connect-with-retry client),
pagefile-backed shared memory via named file mappings, and named
synchronization objects (mutex, event, semaphore). Pipe handles are opened
for overlapped I/O so they cooperate with a fiber scheduler, and objects are
created with a restrictive security descriptor by default. Windows MSVC
(mswin) Ruby only.

## 官网

- 主页: https://github.com/main-path/winipc
- 更新日志: https://github.com/main-path/winipc/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/winipc/issues
- RubyGems: https://rubygems.org/gems/winipc

## 历史版本号

- 0.1.0 (2026-06-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/winipc
- gem 安装: `gem install winipc`
- Bundler: `gem "winipc"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/winipc-0.1.0.gem
- 版本锁定: `gem "winipc", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
