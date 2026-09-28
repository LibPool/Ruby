# dials

**Tag**: serialization, template

## 简介

Dials turns hardcoded constants into operator-adjustable values without
giving up code review as the source of truth. Each dial is declared in
code with a default, a type, JSON-Schema-style constraints, and optional
dimensions (per market, per platform, ...); runtime overrides live in
one small append-only table (state and attributed history are the same
rows), resolve scoped override → global override → code default, are
served from a per-process cache, and every write supports optional
stale-write protection.

## 官网

- 主页: https://github.com/zarpay/dials
- 源码仓库: https://github.com/zarpay/dials/tree/main/gem
- 文档: https://zarpay.github.io/dials/
- 更新日志: https://github.com/zarpay/dials/blob/main/gem/CHANGELOG.md
- 问题追踪: https://github.com/zarpay/dials/issues
- RubyGems: https://rubygems.org/gems/dials

## 历史版本号

- 0.4.0 (2026-09-09)
- 0.3.0 (2026-09-07)
- 0.2.0 (2026-09-04)
- 0.1.0 (2026-09-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/dials
- gem 安装: `gem install dials`
- Bundler: `gem "dials"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/dials-0.4.0.gem
- 版本锁定: `gem "dials", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
