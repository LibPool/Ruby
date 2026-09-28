# sashite-pan

**Tag**: web, testing

## 简介

Parse and generate Portable Action Notation (PAN) strings for representing atomic actions in abstract strategy board games including chess, shogi, xiangqi, and others. PAN provides an intuitive operator-based syntax with six core operators: "-" (move to empty square), "+" (capture), "~" (special moves with side effects), "*" (drop to board), "." (drop with capture), and "=" (in-place transformation), plus "..." (pass turn).
Supports coordinates via CELL specification and piece identifiers via EPIN specification. Handles transformations ("e7-e8=Q"), enhanced/diminished states ("+R", "-P"), and style derivation markers ("K'"). Provides comprehensive validation, immutable action objects, and functional API design.
Examples: "e2-e4" (move), "d1+f3" (capture), "e1~g1" (castling), "P*e5" (drop), "e7-e8=Q" (promotion), "..." (pass), "+d4" (static capture), "e4=+P" (modify).

## 官网

- 主页: https://github.com/sashite/pan.rb
- 文档: https://rubydoc.info/github/sashite/pan.rb/main
- 问题追踪: https://github.com/sashite/pan.rb/issues
- RubyGems: https://rubygems.org/gems/sashite-pan

## 历史版本号

- 4.0.0 (2025-10-25)
- 3.0.0 (2025-06-05)
- 2.0.0 (2025-05-23)
- 1.3.0 (2021-08-17)
- 1.2.0 (2020-07-05)
- 1.1.0 (2020-06-19)
- 1.0.0 (2020-06-16)
- 0.2.0 (2014-07-15)
- 0.1.0 (2014-07-15)
- 0.0.2 (2014-05-29)
- 0.0.1 (2014-05-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/sashite-pan
- gem 安装: `gem install sashite-pan`
- Bundler: `gem "sashite-pan"`
- 最新版本: 4.0.0
- 最新版归档: https://rubygems.org/downloads/sashite-pan-4.0.0.gem
- 版本锁定: `gem "sashite-pan", "~> 4.0.0"`
- 中央仓库: https://rubygems.org/
