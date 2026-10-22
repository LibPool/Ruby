# fast_mb_chars

**Tag**: library

## 简介

Faster String#mb_chars. limit(bytes) cuts on a character boundary without
walking the whole string and without raising on a broken byte. A 1 MB cut
is about 2,000 times faster than the ActiveSupport grapheme scan, and a
7 MB cut is about 3,000 times faster.

downcase, upcase, titleize, reverse, split, slice!, compose, decompose,
tidy_bytes, and the other string methods are forwarded through method_missing.
They still return mb_chars, so existing chains keep working.

## 官网

- 主页: https://github.com/SYNORYXEL/fast_mb_chars
- 更新日志: https://github.com/SYNORYXEL/fast_mb_chars/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/SYNORYXEL/fast_mb_chars/issues
- RubyGems: https://rubygems.org/gems/fast_mb_chars

## 历史版本号

- 0.1.0 (2026-10-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/fast_mb_chars
- gem 安装: `gem install fast_mb_chars`
- Bundler: `gem "fast_mb_chars"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/fast_mb_chars-0.1.0.gem
- 版本锁定: `gem "fast_mb_chars", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
