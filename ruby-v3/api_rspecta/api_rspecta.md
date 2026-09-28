# api_rspecta

**Tag**: web, testing, security, serialization

## 简介

`api_rspecta` adds following helper methods to test your JSON APIs with RSpec:

    **JSON:**
    - `#json` returns parsed `last_response.body`
    - `#refresh_json` reparses `last_response.body`
    - `#print_json` to `JSON.pretty_generate` last response JSON
    - `#json_has_key` tells you if passed json object has a `key`
    - `#json_has_keys` same as above but for a list of keys
    - `#json_has_no_key` is opposite to `#json_has_key`

    **Response:**
      - `should_respond_ok` checks if `last_response.status` was 200
    - `should_respond_created` checks if `last_response.status` was 201
    - `should_respond_with_no_content` checks if `last_response.status` was 204
    - `should_respond_not_authenticated` checks if `last_response.status` was 401
    - `should_respond_not_authorized` checks if `last_response.status` was 403
    - `should_respond_not_found` checks if `last_response.status` was 404
    - `should_respond_with_error_for` checks if `last_response.status` was 422 and that `json` has `errors` for passed `field`
    - `should_respond_with_errors_for` same as above but for a list of errors

## 官网

- 主页: https://github.com/SmartCloud/api_rspecta
- 文档: https://www.rubydoc.info/gems/api_rspecta/0.0.3
- RubyGems: https://rubygems.org/gems/api_rspecta

## 历史版本号

- 0.0.3 (2016-03-04)
- 0.0.2 (2014-12-20)
- 0.0.1 (2014-12-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/api_rspecta
- gem 安装: `gem install api_rspecta`
- Bundler: `gem "api_rspecta"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/api_rspecta-0.0.3.gem
- 版本锁定: `gem "api_rspecta", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
