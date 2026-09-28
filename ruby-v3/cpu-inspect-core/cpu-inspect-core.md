# cpu-inspect-core

**Tag**: web, cli, database, testing, serialization, template, devops, filesystem

## 简介

Background per-core CPU monitoring for Ruby/Rails applications.
Reads /proc/stat on Linux (Heroku) or top on macOS. Writes a rotating
1 MB JSON-lines log per dyno. On single dynos the file backend is used;
on multi-dyno Heroku deployments the Redis backend aggregates all dynos
into a single CpuInspectCore.status view. Ships with a Rails Railtie for
zero-config boot and a CLI executable for bash usage.

## 官网

- 主页: https://github.com/mykbren/cpu-inspect-core
- 更新日志: https://github.com/mykbren/cpu-inspect-core/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/mykbren/cpu-inspect-core/issues
- RubyGems: https://rubygems.org/gems/cpu-inspect-core

## 历史版本号

- 0.1.3 (2026-04-15)
- 0.1.2 (2026-04-15)
- 0.1.1 (2026-04-15)
- 0.1.0 (2026-04-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/cpu-inspect-core
- gem 安装: `gem install cpu-inspect-core`
- Bundler: `gem "cpu-inspect-core"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/cpu-inspect-core-0.1.3.gem
- 版本锁定: `gem "cpu-inspect-core", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
