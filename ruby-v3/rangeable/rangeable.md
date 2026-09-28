# rangeable

**Tag**: filesystem

## 简介

Rangeable is a language-neutral, generic, integer-coordinate closed-interval
set container. It pairs hashable elements with their merged disjoint integer
ranges and answers three queries: by-element ranges, by-position active set,
and by-range transition events. The Ruby reference implementation follows
the Rangeable RFC normatively, including idempotent containment fast-path,
lazy boundary-event indexing, and first-insert deterministic ordering.

## 官网

- 主页: https://github.com/ZhgChgLi/RubyRangeable
- 文档: https://github.com/ZhgChgLi/RangeableRFC/blob/main/RFC.md
- 更新日志: https://github.com/ZhgChgLi/RubyRangeable/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/ZhgChgLi/RubyRangeable/issues
- RubyGems: https://rubygems.org/gems/rangeable

## 历史版本号

- 2.0.0 (2026-05-10)
- 1.0.0 (2026-05-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/rangeable
- gem 安装: `gem install rangeable`
- Bundler: `gem "rangeable"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/rangeable-2.0.0.gem
- 版本锁定: `gem "rangeable", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
