# rack-nackmode

**Tag**: web

## 简介

Middleware that communicates impending shutdown to a load balancer via NACKing
(negative acking) health checks.  Provided you have at least two load-balanced
instances, this allows you to shut down or restart an instance without dropping
any requests.

Your app needs to inform the middleware when it wants to shut down, and the
middleware will call back when it's safe to do so.

## 官网

- 主页: http://github.com/rapportive-oss/rack-nackmode
- 文档: https://www.rubydoc.info/gems/rack-nackmode/0.1.1
- RubyGems: https://rubygems.org/gems/rack-nackmode

## 历史版本号

- 0.1.1 (2013-06-04)
- 0.1.0 (2013-05-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-nackmode
- gem 安装: `gem install rack-nackmode`
- Bundler: `gem "rack-nackmode"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/rack-nackmode-0.1.1.gem
- 版本锁定: `gem "rack-nackmode", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
