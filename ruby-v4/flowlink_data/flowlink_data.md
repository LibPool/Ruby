# flowlink_data

**Tag**: data

## 简介

A framework for getting Flowlink objects from other sources. For example:
  class Distributor::Product &lt; Flowlink::Product
    def sku(hashable)
      # code that picks sku data out of a hashable object.
    end
  end
  Distributor::Product.new(CSV::Row).to_message #=&gt; A bunch of NotImplementedError because just a sku is an invalid product

## 官网

- 主页: https://github.com/aokpower/flowlink_data
- 文档: https://www.rubydoc.info/gems/flowlink_data/0.4.0
- RubyGems: https://rubygems.org/gems/flowlink_data

## 历史版本号

- 0.4.0 (2016-07-07)
- 0.3.0 (2016-06-22)
- 0.2.1 (2016-06-20)
- 0.2.0 (2016-06-17)
- 0.1.0 (2016-04-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/flowlink_data
- gem 安装: `gem install flowlink_data`
- Bundler: `gem "flowlink_data"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/flowlink_data-0.4.0.gem
- 版本锁定: `gem "flowlink_data", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
