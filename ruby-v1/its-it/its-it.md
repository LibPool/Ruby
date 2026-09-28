# its-it

**Tag**: web, testing

## 简介

This gem defines the Kernel method "it" that queue and defer method calls.
This extends the Symbol#to_proc idiom to support chaining multiple methods.
For example, items.collect(&it.to_s.capitalize).  This also allows
conditionals in case statements, such as: case ... when it > 3 then [etc.].
The method is also aliased as "its", for methods that describe possessives
rather than actions, such as items.collect(&its.name.capitalize)

[This gem is an extension of Jay Philips' "methodphitamine" gem, updated
for ruby 1.9 and gemspec compatibility and adding the case statement functionality.]

## 官网

- 主页: http://github.com/ronen/its-it
- 文档: https://www.rubydoc.info/gems/its-it/2.0.0
- RubyGems: https://rubygems.org/gems/its-it

## 历史版本号

- 2.0.0 (2020-06-07)
- 1.3.0 (2016-07-06)
- 1.2.1 (2016-02-22)
- 1.2.0 (2015-12-09)
- 1.1.1 (2012-04-04)
- 1.1.0 (2011-04-26)
- 1.0.1 (2011-04-24)
- 1.0.0 (2011-04-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/its-it
- gem 安装: `gem install its-it`
- Bundler: `gem "its-it"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/its-it-2.0.0.gem
- 版本锁定: `gem "its-it", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
