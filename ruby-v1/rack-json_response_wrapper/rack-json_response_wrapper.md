# rack-json_response_wrapper

**Tag**: web, serialization

## 简介

Rack Middleware for JSON APIs accessed cross-domain from legacy browsers

Firefox version 4 does not support response headers for cross-domain requests.
This middleware intercepts all requests and if the X-WRAP-RESPONSE is set, 
the response will be wrappped in JSON like {header: ..., body: ...}

## 官网

- 主页: http://github.com/gnidan/rack-json_response_wrapper
- 文档: https://www.rubydoc.info/gems/rack-json_response_wrapper/0.1.3
- RubyGems: https://rubygems.org/gems/rack-json_response_wrapper

## 历史版本号

- 0.1.3 (2014-09-15)
- 0.1.2 (2014-09-10)
- 0.1.1 (2014-08-27)
- 0.1.0 (2014-08-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-json_response_wrapper
- gem 安装: `gem install rack-json_response_wrapper`
- Bundler: `gem "rack-json_response_wrapper"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/rack-json_response_wrapper-0.1.3.gem
- 版本锁定: `gem "rack-json_response_wrapper", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
