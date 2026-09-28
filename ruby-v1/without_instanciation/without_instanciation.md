# without_instanciation

**Tag**: data

## 简介

On large results of ActiveRecord queries, instanciation + GC of objects has a real cost of
    allocating memory, setting values, and after all GC garbage ...
    Inside a without_instanciation block, data is returned as hash of values.
    Objects instanciation process id skipped and though GC of theses objects too.
    Performance up to 80% for large query result.
    Of course, you no longer work with Ruby AR objects in this block.

## 官网

- RubyGems: https://rubygems.org/gems/without_instanciation

## 历史版本号

- 1.0.0 (2012-02-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/without_instanciation
- gem 安装: `gem install without_instanciation`
- Bundler: `gem "without_instanciation"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/without_instanciation-1.0.0.gem
- 版本锁定: `gem "without_instanciation", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
