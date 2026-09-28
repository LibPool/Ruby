# extended_has_enumeration

**Tag**: database, testing, data

## 简介

Extends ActiveRecord with the has_enumeration method allowing a symbolic
enumeration to be stored in an ActiveRecord attribute.  The enumeration is
specified as a mapping between symbols and their underlying representation
in the database.  Predicates are provided for each symbol in the enumeration
and the symbols may be used in finder methods.  When using ActiveRecord 3,
the symbols may also be used when interacting with the underlying Arel attribute
for the enumeration.  has_enumeration has been tested with Ruby 1.8.7,
Ruby 1.9.2, JRuby 1.5.5, Rubinius 1.1.0, ActiveRecord 2.3.10, and ActiveRecord
3.0.3.

## 官网

- 主页: http://github.com/maxtsap/has_enumeration
- 文档: https://www.rubydoc.info/gems/extended_has_enumeration/0.0.4
- RubyGems: https://rubygems.org/gems/extended_has_enumeration

## 历史版本号

- 0.0.4 (2013-07-03)
- 0.0.2 (2013-07-02)
- 0.0.1 (2013-06-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/extended_has_enumeration
- gem 安装: `gem install extended_has_enumeration`
- Bundler: `gem "extended_has_enumeration"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/extended_has_enumeration-0.0.4.gem
- 版本锁定: `gem "extended_has_enumeration", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
