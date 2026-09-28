# detagger

**Tag**: cli, filesystem

## 简介

This is intended to be used as a mixin, usualy with some kind of library that parses
  optional command line arguments. The feature here is that the options may contain tags ('example_tag:') that
  are not resolved until they are used. This means that one option may refer to another. An example might be:
  --stage /tmp/fred --logfile stage:/my.log 
  which would later provide a method 'logfile' that would return '/tmp/fred/my.log'

## 官网

- 主页: http://github.com/christfo/detagger
- RubyGems: https://rubygems.org/gems/detagger

## 历史版本号

- 0.2.3 (2012-04-13)
- 0.2.2 (2012-04-10)
- 0.2.1 (2012-03-21)
- 0.2.0 (2012-03-14)
- 0.1.0 (2012-03-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/detagger
- gem 安装: `gem install detagger`
- Bundler: `gem "detagger"`
- 最新版本: 0.2.3
- 最新版归档: https://rubygems.org/downloads/detagger-0.2.3.gem
- 版本锁定: `gem "detagger", "~> 0.2.3"`
- 中央仓库: https://rubygems.org/
