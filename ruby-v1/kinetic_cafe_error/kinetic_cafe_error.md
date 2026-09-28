# kinetic_cafe_error

**Tag**: web, cli, serialization

## 简介

kinetic_cafe_error provides an API-smart error base class and a DSL for
defining errors. Under Rails, it also provides a controller concern
(KineticCafe::ErrorHandler) that has a useful implementation of +rescue_from+
to handle KineticCafe::Error types.

Exceptions in a hierarchy can be handled in a uniform manner, including getting
an I18n translation message with parameters, standard status values, and
meaningful JSON representations that can be used to establish a standard error
representations across both clients and servers.

## 官网

- 主页: https://github.com/KineticCafe/kinetic_cafe_error/
- 文档: https://www.rubydoc.info/gems/kinetic_cafe_error/1.12
- RubyGems: https://rubygems.org/gems/kinetic_cafe_error

## 历史版本号

- 1.12 (2016-05-27)
- 1.11 (2016-05-24)
- 1.10 (2016-03-25)
- 1.9 (2015-11-30)
- 1.8.1 (2015-10-26)
- 1.7 (2015-08-05)
- 1.6 (2015-07-30)
- 1.5 (2015-07-28)
- 1.4.1 (2015-07-08)
- 1.4 (2015-07-07)
- 1.3 (2015-06-18)
- 1.2 (2015-06-08)
- 1.1 (2015-06-05)
- 1.0.1 (2015-05-27)
- 1.0 (2015-05-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/kinetic_cafe_error
- gem 安装: `gem install kinetic_cafe_error`
- Bundler: `gem "kinetic_cafe_error"`
- 最新版本: 1.12
- 最新版归档: https://rubygems.org/downloads/kinetic_cafe_error-1.12.gem
- 版本锁定: `gem "kinetic_cafe_error", "~> 1.12"`
- 中央仓库: https://rubygems.org/
