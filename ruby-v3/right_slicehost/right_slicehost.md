# right_slicehost

**Tag**: web, networking

## 简介

== DESCRIPTION:  The RightScale Slicehost gem has been designed to provide a robust interface to Slicehost's existing API.  == FEATURES/PROBLEMS:  - Full programmatic access to the Slicehost API. - Complete error handling: all operations check for errors and report complete error information by raising a SlicehostError. - Persistent HTTP connections with robust network-level retry layer using Rightscale::HttpConnection. This includes socket timeouts and retries. - Robust HTTP-level retry layer. Certain (user-adjustable) HTTP errors returned by Slicehost are classified as temporary errors. These errors are automaticallly retried using exponentially increasing intervals. The number of retries is user-configurable.  == INSTALL:

## 官网

- 文档: https://www.rubydoc.info/gems/right_slicehost/0.1.0
- RubyGems: https://rubygems.org/gems/right_slicehost

## 历史版本号

- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/right_slicehost
- gem 安装: `gem install right_slicehost`
- Bundler: `gem "right_slicehost"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/right_slicehost-0.1.0.gem
- 版本锁定: `gem "right_slicehost", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
