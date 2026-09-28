# opt_ar

**Tag**: serialization

## 简介

Generates memory-optimal immutable ActiveRecord dupes that are easily serializable and behaves much like ARs. Define required attributes before-hand and use them just as you would on an AR, for better memory optimization. Ideally, suitable in place of caching AR objects with cache stores like Memcached, where serialization and de-serialization are memory-hungry. Optars can save upto 90% of your memory(object allocations), while being upto 20x faster, when fetching huge AR results.

## 官网

- 主页: https://github.com/ragav0102/opt_ar
- 文档: https://www.rubydoc.info/gems/opt_ar/1.1.0
- RubyGems: https://rubygems.org/gems/opt_ar

## 历史版本号

- 1.1.0 (2019-05-20)
- 1.0.1 (2019-05-04)
- 1.0.0 (2019-05-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/opt_ar
- gem 安装: `gem install opt_ar`
- Bundler: `gem "opt_ar"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/opt_ar-1.1.0.gem
- 版本锁定: `gem "opt_ar", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
