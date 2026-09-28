# TextualRegexp

**Tag**: library

## 简介

== FEATURES/PROBLEMS:  Incompatible with 1.9, as far as we know. Technically, it supports everything current RegExp does.  == SYNOPSIS:  Password = TextualRegexp.new do anchor :beginning  group :capture do any :letter repeat(4..13) do any :char end any :digit end end

## 官网

- 文档: https://www.rubydoc.info/gems/TextualRegexp/1.8.6
- RubyGems: https://rubygems.org/gems/TextualRegexp

## 历史版本号

- 1.8.6 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/TextualRegexp
- gem 安装: `gem install TextualRegexp`
- Bundler: `gem "TextualRegexp"`
- 最新版本: 1.8.6
- 最新版归档: https://rubygems.org/downloads/TextualRegexp-1.8.6.gem
- 版本锁定: `gem "TextualRegexp", "~> 1.8.6"`
- 中央仓库: https://rubygems.org/
