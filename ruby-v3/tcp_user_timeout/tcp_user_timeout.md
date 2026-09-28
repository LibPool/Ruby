# tcp_user_timeout

**Tag**: web, networking

## 简介

Wraps the Linux TCP_USER_TIMEOUT (and optional SO_KEEPALIVE) socket
options behind a fiber-safe block API. Sockets opened inside the block
inherit a deadline the kernel itself enforces — Ruby threads parked in
blocking syscalls that Thread#kill and Timeout.timeout cannot interrupt
are released when the kernel drops the connection. No-op on macOS and
other non-Linux platforms.

## 官网

- 主页: https://github.com/rubymonolith/tcp_user_timeout
- 更新日志: https://github.com/rubymonolith/tcp_user_timeout/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/tcp_user_timeout

## 历史版本号

- 0.1.0 (2026-04-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/tcp_user_timeout
- gem 安装: `gem install tcp_user_timeout`
- Bundler: `gem "tcp_user_timeout"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/tcp_user_timeout-0.1.0.gem
- 版本锁定: `gem "tcp_user_timeout", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
