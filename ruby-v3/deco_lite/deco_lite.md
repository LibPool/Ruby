# deco_lite

**Tag**: web, networking, template

## 简介

DecoLite is a little gem that allows you to use the provided DecoLite::Model
    class to dynamically create Decorator class objects. Use the DecoLite::Model
    class directly, or inherit from the DecoLite::Model class to create your own
    unique subclasses with custom functionality. DecoLite::Model
    includes ActiveModel::Model, so validation can be applied using ActiveModel
    validation helpers (https://api.rubyonrails.org/v6.1.3/classes/ActiveModel/Validations/HelperMethods.html)
    you're familiar with; or, you can roll your own - just like any other ActiveModel.

    DecoLite::Model allows you to consume a Ruby Hash that you supply via the
    initializer (DecoLite::Model#new) or via the DecoLite::Model#load! method. Any
    number of Ruby Hashes can be consumed. Your supplied Ruby Hashes are used to
    create attr_accessor attributes (or "fields") on the model. Each attribute
    created is then assigned the value from the Hash that was loaded. Again, any
    number of hashes can be consumed using the DecoLite::Model#load! method.

## 官网

- 主页: https://github.com/gangelo/deco_lite
- 文档: https://www.rubydoc.info/gems/deco_lite/1.5.14
- RubyGems: https://rubygems.org/gems/deco_lite

## 历史版本号

- 1.5.14 (2024-08-10)
- 1.5.13 (2024-02-19)
- 1.5.12 (2024-02-08)
- 1.5.11 (2024-01-22)
- 1.5.10 (2024-01-07)
- 1.5.9 (2023-12-28)
- 1.5.8 (2023-12-02)
- 1.5.7 (2023-10-30)
- 1.5.5 (2023-08-29)
- 1.5.4 (2023-08-17)
- 1.5.3 (2023-05-05)
- 1.5.2 (2023-03-22)
- 1.5.1 (2023-02-16)
- 1.5.0 (2022-11-04)
- 1.4.0 (2022-10-21)
- 1.3.0 (2022-10-04)
- 1.2.1 (2022-10-04)
- 1.2.0 (2022-10-01)
- 1.1.0 (2022-09-30)
- 1.0.0 (2022-09-29)
- 0.3.3 (2022-08-30)
- 0.3.2 (2022-08-29)
- 0.3.1 (2022-08-27)
- 0.3.0 (2022-08-26)
- 0.2.5 (2022-08-22)
- 0.2.4 (2022-08-21)
- 0.2.3 (2022-08-18)
- 0.2.2 (2022-08-17)
- 0.1.1 (2022-08-14)
- 0.1.0 (2022-08-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/deco_lite
- gem 安装: `gem install deco_lite`
- Bundler: `gem "deco_lite"`
- 最新版本: 1.5.14
- 最新版归档: https://rubygems.org/downloads/deco_lite-1.5.14.gem
- 版本锁定: `gem "deco_lite", "~> 1.5.14"`
- 中央仓库: https://rubygems.org/
