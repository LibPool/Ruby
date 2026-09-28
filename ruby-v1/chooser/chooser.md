# chooser

**Tag**: library

## 简介

Provides short interface for choosing elements from array of structs.
Filtering by equality, matching and inclusion, e.g.:
  target.choose(:street => "Main", :age => (24..30), :address => /Main/)
Filtering by instance evaluated string, e.g.:
  target.choose("age >= 24 && address =~ /^Main/")
Rejecting elements with #choose_not method, e.g.:
  target.choose_not(:street => "Main")

## 官网

- 文档: https://www.rubydoc.info/gems/chooser/0.0.3
- RubyGems: https://rubygems.org/gems/chooser

## 历史版本号

- 0.0.3 (2014-03-16)
- 0.0.2 (2014-03-16)
- 0.0.1 (2014-03-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/chooser
- gem 安装: `gem install chooser`
- Bundler: `gem "chooser"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/chooser-0.0.3.gem
- 版本锁定: `gem "chooser", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
