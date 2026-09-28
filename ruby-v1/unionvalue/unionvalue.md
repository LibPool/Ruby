# unionvalue

**Tag**: web, data

## 简介

Allows easy creation of immutable union values, a.k.a. sum-types.

Example: 
APICallResult = UnionValue.new(:success, :failure, :timeout)
APICallResult.failure.is_failure? #=&gt; true
APICallResult.timeout.is_success? #=&gt; false
APICallResult.success(12345).data #=&gt; 12345

## 官网

- 主页: http://github.com/asivitz/unionvalue
- 文档: https://www.rubydoc.info/gems/unionvalue/1.1.0
- RubyGems: https://rubygems.org/gems/unionvalue

## 历史版本号

- 1.1.0 (2015-05-01)
- 1.0.0 (2015-04-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/unionvalue
- gem 安装: `gem install unionvalue`
- Bundler: `gem "unionvalue"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/unionvalue-1.1.0.gem
- 版本锁定: `gem "unionvalue", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
