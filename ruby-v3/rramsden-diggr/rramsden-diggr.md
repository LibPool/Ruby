# rramsden-diggr

**Tag**: web, networking

## 简介

Diggr is a ruby wrapper for the Digg API.  Diggr strives to remain consistent with the Digg API endpoints listed here:  http://apidoc.digg.com/CompleteList. Endpoints are created in Diggr with method calls.  Each node in an endpoint becomes a method call and each node which is an argument becomes  an argument to the previous method. As an example, the following endpoint  /user/{user name}  in which the user name is "johndoe" would be created with this Diggr call:  diggr.user("johndoe")  To send the request to the Digg API and retrieve the results of the call, Diggr requests are terminated in one of two ways.  1. Using the fetch method. By ending your request with the fetch method, your result will be returned to you. If the request is singular, you will receive a single object as a response. If the request is plural, you will receive a collection of objects stored in an array.  2. Using any Enumerable method. In this case, it is unnecessary to use the fetch method.  See the synopsis for examples of each of these types of calls.  Options such as count or offset can be set using the options method and providing a hash of  arguments. See synopsis for more information.  Note: In an effort to remain consistent with the Digg API, some method names do not follow the ruby idiom of underscores. Although somewhat ugly, this allows a user to read the Digg API and understand the exact methods to call in Diggr to achieve their desired results.

## 官网

- 主页: http://github.com/drewolson/diggr
- 文档: https://www.rubydoc.info/gems/rramsden-diggr/0.2.0
- RubyGems: https://rubygems.org/gems/rramsden-diggr

## 历史版本号

- 0.1.8 (2014-08-10)
- 0.1.9 (2014-08-10)
- 0.2.0 (2014-08-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/rramsden-diggr
- gem 安装: `gem install rramsden-diggr`
- Bundler: `gem "rramsden-diggr"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/rramsden-diggr-0.2.0.gem
- 版本锁定: `gem "rramsden-diggr", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
