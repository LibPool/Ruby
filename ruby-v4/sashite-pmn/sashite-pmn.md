# sashite-pmn

**Tag**: testing, serialization

## 简介

PMN (Portable Move Notation) provides a rule-agnostic, JSON-based format for describing
the mechanical decomposition of moves in abstract strategy board games. This gem implements
the PMN Specification v1.0.0 with a functional Ruby interface, breaking down complex movements
into sequences of atomic actions while remaining completely independent of specific game rules.
PMN reveals the underlying mechanics of any board game move through sequential action
decomposition, supporting both explicit and inferred piece specifications. Built on CELL
(coordinate encoding), HAND (reserve notation), and QPI (piece identification) specifications,
it enables universal move representation across chess variants, shōgi, xiangqi, and any
abstract strategy game. Perfect for game engines, move validators, and board game analysis tools.

## 官网

- 主页: https://github.com/sashite/pmn.rb
- 文档: https://rubydoc.info/github/sashite/pmn.rb/main
- 问题追踪: https://github.com/sashite/pmn.rb/issues
- RubyGems: https://rubygems.org/gems/sashite-pmn

## 历史版本号

- 1.2.0 (2025-10-25)
- 1.1.0 (2025-09-09)
- 1.0.0 (2025-09-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/sashite-pmn
- gem 安装: `gem install sashite-pmn`
- Bundler: `gem "sashite-pmn"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/sashite-pmn-1.2.0.gem
- 版本锁定: `gem "sashite-pmn", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
