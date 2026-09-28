# rack-methodoverride-with-params

**Tag**: web, serialization, networking

## 简介

Rack::MethodOverride only checks the X-Http-Method-Override header and the form encoded post body for _method. Rack::MethodOverrideWithParams checks both of those _and_ the query params. So, if you POST xml with a url like http://example.com/?_method=delete the application will see it as a delete request.

## 官网

- 主页: http://github.com/baroquebobcat/rack-methodoverride-with-params
- RubyGems: https://rubygems.org/gems/rack-methodoverride-with-params

## 历史版本号

- 1.0.0 (2010-09-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-methodoverride-with-params
- gem 安装: `gem install rack-methodoverride-with-params`
- Bundler: `gem "rack-methodoverride-with-params"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/rack-methodoverride-with-params-1.0.0.gem
- 版本锁定: `gem "rack-methodoverride-with-params", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
