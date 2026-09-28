# sinatra-rroute

**Tag**: web, template, filesystem

## 简介

Sinatra-rraoute provides `gget'/`ppost'/`ddelete'/... methods which work
just like Sinatra's built-in `get'/`post'/`delete'/... methods, but which
map named routes to functions so that they can be referenced in redirects
etc.

The `path' helper will return a route for a certain route name and the
given values for this route and comes in handy in both, the
controller/model component of the application, and the view where you can
use it to render links, assets URLs, AJAX calls...

The nestable `nnamespace' method is useful for API versioning and does not
interfere with other namespace extensions for Sinatra.

## 官网

- 文档: https://www.rubydoc.info/gems/sinatra-rroute/0.1.0
- RubyGems: https://rubygems.org/gems/sinatra-rroute

## 历史版本号

- 0.1.0 (2014-06-13)
- 0.0.1 (2014-05-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/sinatra-rroute
- gem 安装: `gem install sinatra-rroute`
- Bundler: `gem "sinatra-rroute"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/sinatra-rroute-0.1.0.gem
- 版本锁定: `gem "sinatra-rroute", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
