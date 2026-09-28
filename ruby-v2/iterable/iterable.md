# iterable

**Tag**: testing

## 简介

Provides the class IterableArray, which implements all of the methods of Array
(as of Ruby 1.9.3) in an iterable-aware fashion. I.e., behavior is defined to
the greatest extent possible for operations that modify an IterableArray from
within an iteration block (e.g. each, map, delete_if, reverse_each). To use,
call #to_iter on a pre-existing Array or use IterableArray.new; the
IterableArray should act identically to a regular Array except that it
responds logically to modifications during iteration.

## 官网

- 主页: https://github.com/scooter-dangle/iterable
- 文档: https://www.rubydoc.info/gems/iterable/0.0.11.pre
- RubyGems: https://rubygems.org/gems/iterable

## 历史版本号

- 0.0.11.pre (2013-07-21)
- 0.0.10.pre (2013-06-25)
- 0.0.6.pre (2013-02-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/iterable
- gem 安装: `gem install iterable`
- Bundler: `gem "iterable"`
- 最新版本: 0.0.11.pre
- 最新版归档: https://rubygems.org/downloads/iterable-0.0.11.pre.gem
- 版本锁定: `gem "iterable", "~> 0.0.11.pre"`
- 中央仓库: https://rubygems.org/
