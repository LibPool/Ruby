# tokenize_attr

**Tag**: web

## 简介

tokenize_attr adds a `tokenize` class macro to ActiveRecord models. When no
prefix is needed it transparently delegates to Rails' built-in
has_secure_token (Rails 5+). When a prefix is required it installs a
before_create callback backed by SecureRandom.base58 with configurable
size, prefix, and retry logic.

## 官网

- 主页: https://github.com/pniemczyk/tokenize_attr
- RubyGems: https://rubygems.org/gems/tokenize_attr

## 历史版本号

- 0.2.0 (2026-03-08)
- 0.1.0 (2026-03-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/tokenize_attr
- gem 安装: `gem install tokenize_attr`
- Bundler: `gem "tokenize_attr"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/tokenize_attr-0.2.0.gem
- 版本锁定: `gem "tokenize_attr", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
