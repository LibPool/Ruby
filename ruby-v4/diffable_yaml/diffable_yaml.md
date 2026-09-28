# diffable_yaml

**Tag**: testing, serialization, filesystem, data

## 简介

this is a little chunck of code i use to dump Ruby objects to YAML with Hash
keys in a some-what consistent order.

i do this because i often find myself using YAML files as data storage and
this makes it a lot easier to compare versions with text-based diff toolspec.

this lib is horribly alpha and has no tests what-so-ever. i'm sure it's
as full or bugs and bad ideas as 100 lines of code can be. i just put it
here so it's easier for me to use across projectspec. but you're welcome
to take it for a spin too if you really want.

this relies on Psych internals, so it has a dependency on pysch ~&gt; 2.0.
it might work fine with other versions; that's just all i've tested it
against at the moment.

## 官网

- 主页: https://github.com/nrser/DiffableYAML
- 文档: https://www.rubydoc.info/gems/diffable_yaml/0.0.2
- RubyGems: https://rubygems.org/gems/diffable_yaml

## 历史版本号

- 0.0.2 (2015-11-04)
- 0.0.1 (2015-10-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/diffable_yaml
- gem 安装: `gem install diffable_yaml`
- Bundler: `gem "diffable_yaml"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/diffable_yaml-0.0.2.gem
- 版本锁定: `gem "diffable_yaml", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
