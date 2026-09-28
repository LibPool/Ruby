# viewing_as

**Tag**: web, cli, database, security, template, tooling, data

## 简介

Let an administrator view an account as its owner. Read-only by default (two
layers: no non-GET requests, and ActiveRecord writes refused), re-validated
from the database on every request so revoked consent bites on the next click,
time-boxed server-side, and logged in words the account owner can read.
Stores its state in a signed cookie rather than the Rails session, so an
edge-cached site stays cached. Built for the Rails 8 authentication
generator; works with anything that can answer "who is signed in".

## 官网

- 主页: https://github.com/delistmydata/viewing_as
- 更新日志: https://github.com/delistmydata/viewing_as/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/delistmydata/viewing_as/issues
- RubyGems: https://rubygems.org/gems/viewing_as

## 历史版本号

- 0.1.0 (2026-09-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/viewing_as
- gem 安装: `gem install viewing_as`
- Bundler: `gem "viewing_as"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/viewing_as-0.1.0.gem
- 版本锁定: `gem "viewing_as", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
