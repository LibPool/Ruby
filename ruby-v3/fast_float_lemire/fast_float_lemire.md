# fast_float_lemire

**Tag**: testing, data

## 简介

An educational Ruby C extension implementing the Eisel-Lemire algorithm
for string-to-float conversion. This gem demonstrates why this optimization,
despite being ~2.6x faster for complex numbers, was NOT submitted to Ruby core:
it regresses performance by ~9% on simple numbers (the common case).

Use this gem to learn about float parsing algorithms and their tradeoffs,
or if you specifically work with high-precision scientific data.

## 官网

- 主页: https://github.com/mensfeld/fast_float_lemire
- 更新日志: https://github.com/mensfeld/fast_float_lemire/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/fast_float_lemire

## 历史版本号

- 0.2.0 (2025-12-19)
- 0.1.1 (2025-12-18)
- 0.1.0 (2025-12-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/fast_float_lemire
- gem 安装: `gem install fast_float_lemire`
- Bundler: `gem "fast_float_lemire"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/fast_float_lemire-0.2.0.gem
- 版本锁定: `gem "fast_float_lemire", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
