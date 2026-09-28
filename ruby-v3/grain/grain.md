# grain

**Tag**: database, template, tooling, data

## 简介

Grain keeps dashboard aggregates pre-computed and up to date inside your own
Postgres database. You declare the grain of an aggregate once — tenant, time
bucket and dimensions — and database triggers record what changed so a worker
can rebuild just the affected cells, instead of recomputing everything on a
schedule. No new infrastructure, no materialized view refresh storms, and a
verify command that proves the aggregate still matches its source.

## 官网

- 主页: https://github.com/grainrb/grain
- 更新日志: https://github.com/grainrb/grain/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/grain

## 历史版本号

- 0.0.3 (2026-08-21)
- 0.0.2 (2026-08-21)
- 0.0.1 (2026-08-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/grain
- gem 安装: `gem install grain`
- Bundler: `gem "grain"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/grain-0.0.3.gem
- 版本锁定: `gem "grain", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
