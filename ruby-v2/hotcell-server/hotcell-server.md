# hotcell-server

**Tag**: web, networking

## 简介

Runs a HotCell container. A supervisor listens on two Unix sockets, forks a worker for each request,
and enforces a wall clock deadline and resource limits on it. Write the work as a subclass of
HotCell::Operation.

## 官网

- 主页: https://github.com/basecamp/hotcell
- 源码仓库: https://github.com/basecamp/hotcell/tree/v0.5.0/hotcell-server
- 更新日志: https://github.com/basecamp/hotcell/blob/v0.5.0/CHANGELOG.md
- 问题追踪: https://github.com/basecamp/hotcell/issues
- RubyGems: https://rubygems.org/gems/hotcell-server

## 历史版本号

- 0.5.0 (2026-09-09)
- 0.4.1 (2026-09-08)
- 0.4.0 (2026-09-08)
- 0.3.1 (2026-09-02)
- 0.3.0 (2026-09-01)
- 0.2.0 (2026-08-25)
- 0.1.0 (2026-08-19)
- 0.0.0 (2026-08-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/hotcell-server
- gem 安装: `gem install hotcell-server`
- Bundler: `gem "hotcell-server"`
- 最新版本: 0.5.0
- 最新版归档: https://rubygems.org/downloads/hotcell-server-0.5.0.gem
- 版本锁定: `gem "hotcell-server", "~> 0.5.0"`
- 中央仓库: https://rubygems.org/
