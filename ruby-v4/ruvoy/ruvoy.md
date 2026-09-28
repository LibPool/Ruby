# ruvoy

**Tag**: web, cli, networking, data

## 简介

Ruvoy is a Ruby application runtime inside Envoy. It loads an ordinary
rackup into a CRuby VM embedded in a dynamic module and answers requests as
a terminal HTTP filter, so a request reaches Rack as owned data rather than
over a second HTTP connection to a separate application server. HTTP/1.1,
HTTP/2, TLS, timeouts and the downstream connection lifecycle stay with
Envoy. Scheduler-aware Ruby I/O overlaps on fibers; CPU-bound Ruby does not
run in parallel, since the process holds one VM.

## 官网

- 主页: https://github.com/CodePrometheus/ruvoy
- 问题追踪: https://github.com/CodePrometheus/ruvoy/issues
- RubyGems: https://rubygems.org/gems/ruvoy

## 历史版本号

- 0.1.0-x86_64-linux (2026-09-08)
- 0.1.0-aarch64-linux (2026-09-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruvoy
- gem 安装: `gem install ruvoy`
- Bundler: `gem "ruvoy"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/ruvoy-0.1.0.gem
- 版本锁定: `gem "ruvoy", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
