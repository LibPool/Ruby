# erlnixify

**Tag**: template

## 简介

Erlnixify's purpose is to rectify a problem in Erlang. At the moment
 the Erlang VM has the problem that it can not react to unix
signals. This renders it impossible to integrate Erlang into a basic
unix environment like init.d or daemontools. This ruby project is
designed to fill that void. It provides a small unix executable whose
responsibility it is to capture normal unix signals and translate them
into something that the erlang vm can understand.

## 官网

- 文档: https://www.rubydoc.info/gems/erlnixify/0.0.8
- RubyGems: https://rubygems.org/gems/erlnixify

## 历史版本号

- 0.0.8 (2013-08-08)
- 0.0.7 (2013-08-02)
- 0.0.6 (2013-07-31)
- 0.0.5 (2013-07-30)
- 0.0.4 (2013-07-30)
- 0.0.3 (2013-06-12)
- 0.0.2 (2013-05-24)
- 0.0.1 (2013-05-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/erlnixify
- gem 安装: `gem install erlnixify`
- Bundler: `gem "erlnixify"`
- 最新版本: 0.0.8
- 最新版归档: https://rubygems.org/downloads/erlnixify-0.0.8.gem
- 版本锁定: `gem "erlnixify", "~> 0.0.8"`
- 中央仓库: https://rubygems.org/
