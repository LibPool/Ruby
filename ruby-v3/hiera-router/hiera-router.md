# hiera-router

**Tag**: serialization, filesystem

## 简介

This hiera backend replaces the default yaml backend, but will resend queries to other hiera backends based on the value returned by the yaml files.

When hiera-router gets a string matching "backend[otherbackendname]", it will resend the same query to "otherbackendname".

## 官网

- 主页: https://github.com/jovandeginste/hiera-router
- 问题追踪: https://github.com/jovandeginste/hiera-router/issues
- RubyGems: https://rubygems.org/gems/hiera-router

## 历史版本号

- 0.5.11 (2017-06-30)
- 0.5.10 (2017-06-29)
- 0.5.9 (2017-06-29)
- 0.5.8 (2017-06-29)
- 0.5.7 (2017-06-29)
- 0.5.6 (2017-06-29)
- 0.5.5 (2017-06-29)
- 0.5.4 (2017-06-29)
- 0.5.3 (2017-06-29)
- 0.5.2 (2017-06-29)
- 0.5.1 (2017-06-29)
- 0.5.0 (2017-06-29)
- 0.4.2 (2017-06-22)
- 0.4.1 (2017-06-22)
- 0.4.0 (2017-06-22)
- 0.3.8 (2017-04-21)
- 0.3.7 (2017-04-21)
- 0.3.6 (2017-04-21)
- 0.3.5 (2017-04-21)
- 0.3.4 (2017-04-21)
- 0.3.3 (2017-04-21)
- 0.3.2 (2017-04-21)
- 0.3.1 (2017-04-21)
- 0.3.0 (2017-04-21)
- 0.2.6.1 (2016-12-15)
- 0.2.6b (2016-12-15)
- 0.2.6 (2016-12-14)
- 0.2.5 (2016-07-04)
- 0.2.3 (2016-07-04)
- 0.2.2 (2016-06-24)
- 0.2.1 (2016-06-24)
- 0.2.0 (2016-06-24)
- 0.1.9 (2016-06-23)
- 0.1.8 (2016-06-23)
- 0.1.7 (2016-06-23)
- 0.1.6 (2016-06-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/hiera-router
- gem 安装: `gem install hiera-router`
- Bundler: `gem "hiera-router"`
- 最新版本: 0.5.11
- 最新版归档: https://rubygems.org/downloads/hiera-router-0.5.11.gem
- 版本锁定: `gem "hiera-router", "~> 0.5.11"`
- 中央仓库: https://rubygems.org/
