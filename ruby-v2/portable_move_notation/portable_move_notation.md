# portable_move_notation

**Tag**: testing, serialization

## 简介

Portable Move Notation (PMN) v1.0.0 is a rule-agnostic, JSON-based format using arrays to represent deterministic state-changing actions in abstract strategy board games. This gem provides a consistent Ruby interface for serializing, deserializing, and validating moves across Chess, Shogi, Xiangqi, and other traditional or non-traditional variants. The v1.0.0 format uses simple 4-element arrays: [source_square, destination_square, piece_name, captured_piece], making it compact and language-agnostic while focusing on deterministic state transformations independent of game-specific rules.

## 官网

- 主页: https://github.com/sashite/pmn.rb
- 文档: https://rubydoc.info/github/sashite/pmn.rb/main
- 问题追踪: https://github.com/sashite/pmn.rb/issues
- RubyGems: https://rubygems.org/gems/portable_move_notation

## 历史版本号

- 3.0.0 (2025-06-11)
- 2.2.0 (2025-05-16)
- 2.1.1 (2025-05-14)
- 2.1.0 (2025-05-13)
- 2.0.0 (2025-05-12)
- 1.2.0 (2020-07-06)
- 1.1.1 (2020-06-19)
- 1.1.0 (2020-06-17)
- 1.0.0 (2020-06-14)
- 0.2.0 (2020-05-14)
- 0.1.0 (2019-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/portable_move_notation
- gem 安装: `gem install portable_move_notation`
- Bundler: `gem "portable_move_notation"`
- 最新版本: 3.0.0
- 最新版归档: https://rubygems.org/downloads/portable_move_notation-3.0.0.gem
- 版本锁定: `gem "portable_move_notation", "~> 3.0.0"`
- 中央仓库: https://rubygems.org/
