# nested_has_many_through

**Tag**: database

## 简介

This plugin makes it possible to define has_many :through relationships that
  go through other has_many :through relationships, possibly through an arbitrarily deep hierarchy.
  This allows associations across any number of tables to be constructed, without having to resort to
  find_by_sql (which isn't a suitable solution if you need to do eager loading through :include as well).

## 官网

- 主页: http://twitter.com/i2w
- 源码仓库: https://github.com/romanvbabenko/nested_has_many_through
- 问题追踪: https://github.com/romanvbabenko/nested_has_many_through/issues
- RubyGems: https://rubygems.org/gems/nested_has_many_through

## 历史版本号

- 0.0.2 (2011-04-16)
- 0.0.1 (2011-04-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/nested_has_many_through
- gem 安装: `gem install nested_has_many_through`
- Bundler: `gem "nested_has_many_through"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/nested_has_many_through-0.0.2.gem
- 版本锁定: `gem "nested_has_many_through", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
