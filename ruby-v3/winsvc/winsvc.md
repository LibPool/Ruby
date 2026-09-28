# winsvc

**Tag**: cli, tooling

## 简介

winsvc runs a Ruby process as a Windows service (SERVICE_WIN32_OWN_PROCESS)
with correct service-control-manager integration: the control handler is
pure C (no Ruby ever runs on an SCM thread), controls arrive on a
Thread::Queue (fiber-scheduler cooperative), SERVICE_STOPPED is reported
exactly once, and checkpoints are only ever honest. The same block runs
unchanged as a console program for development. Includes a minimal
installer (CreateServiceW, delayed auto-start, restart-on-failure recovery)
and a correctly quoted sc.exe command generator. Windows MSVC (mswin) Ruby
only.

## 官网

- 主页: https://github.com/main-path/winsvc
- 更新日志: https://github.com/main-path/winsvc/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/winsvc/issues
- RubyGems: https://rubygems.org/gems/winsvc

## 历史版本号

- 0.1.0 (2026-06-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/winsvc
- gem 安装: `gem install winsvc`
- Bundler: `gem "winsvc"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/winsvc-0.1.0.gem
- 版本锁定: `gem "winsvc", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
