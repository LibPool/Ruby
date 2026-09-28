# lazy_as_json

**Tag**: web, cli, serialization, filesystem, data

## 简介

Lazy As Json

A simple and concise way to use as_json with “only”, “except” and other options without using them literally.

Instead of using this -

`User.as_json(only: [:id, :first_name, profiles: [:company, :location]])`

You can perhaps use this -

`User.as_json(only_keys: ‘_,first_name,profiles(p),p.company,p.location’)`

As simple as this.

You can control what your API response should include through a flexible parameter string.

i.e. - “/api/v1/users/me?_keys=_,last_name,profiles(p),p.company,p.location”

This parameter string could dig through the nested objects and their nesting too.
Just to reduce the API response size significantly, you can use this parameter control over wherever it is used.
However it might seems quite trivial but frankly speaking it saves lot in response data hence faster loading time at client side.

Moreover as it uses Hash.new and constructs attribute on runtime, you can throttle calling from the expensive method by using this parameter string.

## 官网

- 主页: http://hasan.wordpress.com
- 源码仓库: https://github.com/we4tech/lazy-as-json
- 文档: https://www.rubydoc.info/gems/lazy_as_json/0.1.0
- RubyGems: https://rubygems.org/gems/lazy_as_json

## 历史版本号

- 0.1.0 (2016-03-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/lazy_as_json
- gem 安装: `gem install lazy_as_json`
- Bundler: `gem "lazy_as_json"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/lazy_as_json-0.1.0.gem
- 版本锁定: `gem "lazy_as_json", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
