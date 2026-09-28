# reqless

**Tag**: cli, database, testing, data

## 简介

`reqless` is meant to be a performant alternative to other queueing
systems, with statistics collection, a browser interface, and
strong guarantees about job losses.

It's written as a collection of Lua scipts that are loaded into the
Redis instance to be used, and then executed by the client library.
As such, it's intended to be extremely easy to port to other languages,
without sacrificing performance and not requiring a lot of logic
replication between clients. Keep the Lua scripts updated, and your
language-specific extension will also remain up to date.

## 官网

- 文档: https://www.rubydoc.info/gems/reqless/0.0.5
- RubyGems: https://rubygems.org/gems/reqless

## 历史版本号

- 0.0.5 (2024-08-29)
- 0.0.4 (2024-08-28)
- 0.0.3 (2024-08-27)
- 0.0.2 (2024-08-26)
- 0.0.1 (2024-08-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/reqless
- gem 安装: `gem install reqless`
- Bundler: `gem "reqless"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/reqless-0.0.5.gem
- 版本锁定: `gem "reqless", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
