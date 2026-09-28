# rack-indifferent

**Tag**: web

## 简介

rack-indifferent monkey patches Rack::Utils::KeySpaceConstrainedParams
to make the hash it stores params in support indifferent access.  So web
frameworks that use rack-indifferent don't have to make a deep copy
of the params to allow indifferent access to the params.

## 官网

- 主页: http://github.com/jeremyevans/rack-indifferent
- 文档: https://www.rubydoc.info/gems/rack-indifferent/1.2.0
- RubyGems: https://rubygems.org/gems/rack-indifferent

## 历史版本号

- 1.2.0 (2016-09-20)
- 1.1.0 (2015-03-09)
- 1.0.0 (2015-03-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-indifferent
- gem 安装: `gem install rack-indifferent`
- Bundler: `gem "rack-indifferent"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/rack-indifferent-1.2.0.gem
- 版本锁定: `gem "rack-indifferent", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
