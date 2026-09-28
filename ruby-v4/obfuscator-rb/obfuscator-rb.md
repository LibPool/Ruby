# obfuscator-rb

**Tag**: data

## 简介

A Ruby library for data obfuscation that:
- Preserves original data format and structure as much as possible
- Supports numbers (including IP-like sequences), dates, and text
- Maintains text structure while replacing content with meaningless but natural-looking words in English and Russian
- Maintains data type consistency and decimal precision
- Offers seeded randomization for reproducible results
- Handles various number formats (leading zeros, separators)
- Provides configurable options (unsigned mode, format preservation)

Note: Individual obfuscator instances are not thread-safe.
For concurrent operations, create separate instances per thread.

## 官网

- 主页: https://hub.mos.ru/ad/obfuscator
- 更新日志: https://hub.mos.ru/ad/obfuscator/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/obfuscator-rb

## 历史版本号

- 0.8.1 (2025-02-23)
- 0.3.2 (2025-02-19)
- 0.3.1 (2025-02-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/obfuscator-rb
- gem 安装: `gem install obfuscator-rb`
- Bundler: `gem "obfuscator-rb"`
- 最新版本: 0.8.1
- 最新版归档: https://rubygems.org/downloads/obfuscator-rb-0.8.1.gem
- 版本锁定: `gem "obfuscator-rb", "~> 0.8.1"`
- 中央仓库: https://rubygems.org/
