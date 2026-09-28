# qless

**Tag**: cli, database, testing, data

## 简介

`qless` is meant to be a performant alternative to other queueing
systems, with statistics collection, a browser interface, and
strong guarantees about job losses.

It's written as a collection of Lua scipts that are loaded into the
Redis instance to be used, and then executed by the client library.
As such, it's intended to be extremely easy to port to other languages,
without sacrificing performance and not requiring a lot of logic
replication between clients. Keep the Lua scripts updated, and your
language-specific extension will also remain up to date.

## 官网

- 主页: http://github.com/seomoz/qless
- 文档: https://www.rubydoc.info/gems/qless/0.12.0
- RubyGems: https://rubygems.org/gems/qless

## 历史版本号

- 0.12.0 (2018-01-17)
- 0.11.0 (2017-12-08)
- 0.10.5 (2016-11-29)
- 0.10.4 (2016-11-28)
- 0.10.3 (2016-04-15)
- 0.10.2 (2016-03-31)
- 0.10.1 (2016-03-31)
- 0.10.0 (2016-02-02)
- 0.9.3 (2013-05-20)
- 0.9.2 (2012-11-30)
- 0.9.1 (2012-07-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/qless
- gem 安装: `gem install qless`
- Bundler: `gem "qless"`
- 最新版本: 0.12.0
- 最新版归档: https://rubygems.org/downloads/qless-0.12.0.gem
- 版本锁定: `gem "qless", "~> 0.12.0"`
- 中央仓库: https://rubygems.org/
