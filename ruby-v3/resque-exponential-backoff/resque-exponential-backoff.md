# resque-exponential-backoff

**Tag**: web

## 简介

A resque plugin that adds retry/exponential backoff functionality to your
resque jobs.

Simply extend your module/class with this module:

    require 'resque-exponential-backoff'

    class DeliverWebHook
        extend Resque::Plugins::ExponentialBackoff

        def self.perform(url, hook_id, hmac_key)
            heavy_lifting
        end
    end

## 官网

- 主页: http://github.com/lantins/resque-exponential-backoff
- 文档: http://rdoc.info/projects/lantins/resque-exponential-backoff
- RubyGems: https://rubygems.org/gems/resque-exponential-backoff

## 历史版本号

- 0.1.1 (2010-04-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-exponential-backoff
- gem 安装: `gem install resque-exponential-backoff`
- Bundler: `gem "resque-exponential-backoff"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/resque-exponential-backoff-0.1.1.gem
- 版本锁定: `gem "resque-exponential-backoff", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
