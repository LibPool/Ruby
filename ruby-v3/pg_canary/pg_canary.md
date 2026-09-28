# pg_canary

**Tag**: database, testing, tooling, data

## 简介

pg_canary watches queries executed in development/test, parses them with PostgreSQL's own parser (pg_query), and combines the AST with schema metadata (indexes, column types) to warn about anti-patterns that can become slow queries in production: leading-wildcard LIKEs, function-wrapped columns in WHERE, ORDER BY RANDOM(), NOT IN (SELECT ...), and more.

## 官网

- 主页: https://github.com/kyuuri1791/pg_canary
- 更新日志: https://github.com/kyuuri1791/pg_canary/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/pg_canary

## 历史版本号

- 0.3.0 (2026-07-19)
- 0.2.0 (2026-07-18)
- 0.1.0 (2026-07-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/pg_canary
- gem 安装: `gem install pg_canary`
- Bundler: `gem "pg_canary"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/pg_canary-0.3.0.gem
- 版本锁定: `gem "pg_canary", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
