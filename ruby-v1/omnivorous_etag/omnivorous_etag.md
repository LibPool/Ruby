# omnivorous_etag

**Tag**: template

## 简介

ETags are good, however normally they are generated based on strings. However, very often it is easier
to pass in a complete model object as your ETag, or it's parametrized represenation (record id) together
with the version. Or an array of objects (if you want to cache your object listing page and prevent it
from spending time on template rendering).

This module will take care of transforming any object into a stringified representation that is usable as an etag
with minimum fuss.

## 官网

- 主页: http://github.com/julik/omnivorous_etag
- RubyGems: https://rubygems.org/gems/omnivorous_etag

## 历史版本号

- 1.0.0 (2011-11-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/omnivorous_etag
- gem 安装: `gem install omnivorous_etag`
- Bundler: `gem "omnivorous_etag"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/omnivorous_etag-1.0.0.gem
- 版本锁定: `gem "omnivorous_etag", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
