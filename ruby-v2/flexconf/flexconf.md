# flexconf

**Tag**: serialization, filesystem

## 简介

FlexConf is a simple configuration utility that does its job and gets
out of your way. It reads settings from a hash or YAML file ('config.yml' by default)
but allows overrides from a '*_local.yml' file and from environment variables. 
Settings can be read as indifferent hash values (config['foo'] or config[:foo]) 
or method calls (config.foo) with recursive nesting (config.foo.bar). The code
is lightweight and fast with no additional dependencies.

## 官网

- RubyGems: https://rubygems.org/gems/flexconf

## 历史版本号

- 0.2.1 (2011-11-06)
- 0.2.0 (2011-11-04)
- 0.1.0 (2011-10-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/flexconf
- gem 安装: `gem install flexconf`
- Bundler: `gem "flexconf"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/flexconf-0.2.1.gem
- 版本锁定: `gem "flexconf", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
