# right_gogrid

**Tag**: web, networking

## 简介

== DESCRIPTION:  The RightScale GoGrid gem has been designed to provide a robust interface to GoGrid's existing API.  == FEATURES/PROBLEMS:  - Full programmatic access to the GoGrid API. - Complete error handling: all operations check for errors and report complete error information by raising a GoGridError. - Persistent HTTP connections with robust network-level retry layer using RightHttpConnection).  This includes socket timeouts and retries. - Robust HTTP-level retry layer.  Certain (user-adjustable) HTTP errors returned by GoGrid are classified as temporary errors. These errors are automaticallly retried using exponentially increasing intervals. The number of retries is user-configurable.

## 官网

- 文档: https://www.rubydoc.info/gems/right_gogrid/0.1.0
- RubyGems: https://rubygems.org/gems/right_gogrid

## 历史版本号

- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/right_gogrid
- gem 安装: `gem install right_gogrid`
- Bundler: `gem "right_gogrid"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/right_gogrid-0.1.0.gem
- 版本锁定: `gem "right_gogrid", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
