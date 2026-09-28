# schema_reaper

**Tag**: web, cli, database, serialization, data

## 简介

schema_reaper scans a Rails + PostgreSQL app for schema debt that's easy to accumulate and hard to find by hand.

It checks your live database against your codebase and flags three kinds of problems: things nothing references anymore (dead columns and dead tables), index trouble (indexes nobody queries, indexes made redundant by a wider index that already covers them, and foreign-key columns with no index at all), and degenerate data (columns that are always NULL, or hold the exact same value in every row).

Every finding comes with a confidence score, an estimate of the disk space removing it would reclaim, and a concrete fix. For a column, that's a two-step migration: stop reading it first, then drop it once you've confirmed nothing broke. An optional runtime tracker can sample real production traffic to raise confidence further, for cases a static code scan alone can't settle.

Reports come as a colored terminal summary, JSON, Markdown for a PR comment, or SARIF for GitHub code scanning -- plus a CI baseline gate and a trend log to track progress release over release.

PostgreSQL only for now. Requires Ruby 2.7 or later. Full usage is in the README.

## 官网

- 主页: https://github.com/aksshatt/schema_reaper
- 文档: https://github.com/aksshatt/schema_reaper#readme
- 更新日志: https://github.com/aksshatt/schema_reaper/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/aksshatt/schema_reaper/issues
- RubyGems: https://rubygems.org/gems/schema_reaper

## 历史版本号

- 2.0.1 (2026-09-23)
- 2.0.0 (2026-09-23)
- 1.0.16 (2026-09-22)
- 1.0.15 (2026-09-18)
- 1.0.14 (2026-09-18)
- 1.0.13 (2026-09-18)
- 1.0.12 (2026-09-15)
- 1.0.11 (2026-09-15)
- 1.0.10 (2026-09-15)
- 1.0.9 (2026-09-09)
- 1.0.8 (2026-09-08)
- 1.0.7 (2026-09-04)
- 1.0.6 (2026-09-04)
- 1.0.5 (2026-09-04)
- 1.0.4 (2026-09-04)
- 1.0.3 (2026-09-04)
- 1.0.2 (2026-09-04)
- 1.0.0 (2026-09-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/schema_reaper
- gem 安装: `gem install schema_reaper`
- Bundler: `gem "schema_reaper"`
- 最新版本: 2.0.1
- 最新版归档: https://rubygems.org/downloads/schema_reaper-2.0.1.gem
- 版本锁定: `gem "schema_reaper", "~> 2.0.1"`
- 中央仓库: https://rubygems.org/
