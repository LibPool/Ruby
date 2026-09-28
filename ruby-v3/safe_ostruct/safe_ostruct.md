# safe_ostruct

**Tag**: library

## 简介

SafeOstruct is a fast, dependency-free struct-like class with an OpenStruct-style interface. Instances are built on cached per-key-set shape classes with real attr_accessor methods, so attribute reads and writes run at Struct speed (within ~10% of raw Hash access) instead of going through method_missing. It supports dynamic attributes, method-style and hash-style (symbol or string) access, and returns nil instead of raising NoMethodError for undefined attributes.

## 官网

- 主页: https://github.com/wqsaali/safe-ostruct
- 更新日志: https://github.com/wqsaali/safe-ostruct/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/safe_ostruct

## 历史版本号

- 2.0.0 (2026-07-27)
- 1.0.0 (2026-07-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/safe_ostruct
- gem 安装: `gem install safe_ostruct`
- Bundler: `gem "safe_ostruct"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/safe_ostruct-2.0.0.gem
- 版本锁定: `gem "safe_ostruct", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
