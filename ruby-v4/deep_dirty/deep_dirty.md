# deep_dirty

**Tag**: web

## 简介

ActiveRecord dirty tracking that compares every attribute to it's value before type cast
    and marks all changes detected as changed attributes. This makes it possible to detect `user.name.upcase!`
    `user.roles &lt;&lt; 'some_role'` and similar implicit changes.

    To make it automatic on `save`, this module sets up a `before_validation` callback when included into a model.

## 官网

- 主页: https://github.com/borgand/deep_dirty
- 文档: https://www.rubydoc.info/gems/deep_dirty/1.0.2
- RubyGems: https://rubygems.org/gems/deep_dirty

## 历史版本号

- 1.0.2 (2014-08-25)
- 1.0.1 (2014-08-25)
- 1.0.0 (2014-08-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/deep_dirty
- gem 安装: `gem install deep_dirty`
- Bundler: `gem "deep_dirty"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/deep_dirty-1.0.2.gem
- 版本锁定: `gem "deep_dirty", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
