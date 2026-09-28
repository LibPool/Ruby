# consul-template-generator

**Tag**: cli, template, tooling

## 简介

When using complex consul-template templates or distributing them across many hosts, you run the risk of DoSing your consul cluster.  Using consul-template-generator you can instead delegate the watching/rendering of templates to a single host and have downstream clients instead use a simple consul-template KV watch to retrieve the template and write it to disk.

## 官网

- 主页: http://github.com/boldfield/consul-template-generator
- 源码仓库: http://github.com/socrata-platform/consul-template-generator
- 文档: https://www.rubydoc.info/gems/consul-template-generator/0.3.6
- RubyGems: https://rubygems.org/gems/consul-template-generator

## 历史版本号

- 0.3.6 (2019-04-29)
- 0.3.5 (2016-01-05)
- 0.3.4 (2015-08-14)
- 0.3.3 (2015-08-04)
- 0.3.2 (2015-08-03)
- 0.3.1 (2015-07-30)
- 0.3.0 (2015-07-28)
- 0.2.0 (2015-07-27)
- 0.1.2 (2015-07-26)
- 0.1.1 (2015-07-24)
- 0.1.0 (2015-07-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/consul-template-generator
- gem 安装: `gem install consul-template-generator`
- Bundler: `gem "consul-template-generator"`
- 最新版本: 0.3.6
- 最新版归档: https://rubygems.org/downloads/consul-template-generator-0.3.6.gem
- 版本锁定: `gem "consul-template-generator", "~> 0.3.6"`
- 中央仓库: https://rubygems.org/
