# ryansch-resque-loner

**Tag**: testing

## 简介

Makes sure that for special jobs, there can be only one job with the same workload in one queue.

Example:
    class CacheSweeper 

       include Resque::Plugins::UniqueJob

       @queue = :cache_sweeps

       def self.perform(article_id)
         # Cache Me If You Can...
       end
    end

## 官网

- 主页: http://github.com/ryansch/resque-loner
- RubyGems: https://rubygems.org/gems/ryansch-resque-loner

## 历史版本号

- 1.0.1.2 (2011-11-08)
- 1.0.1.1 (2011-11-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/ryansch-resque-loner
- gem 安装: `gem install ryansch-resque-loner`
- Bundler: `gem "ryansch-resque-loner"`
- 最新版本: 1.0.1.2
- 最新版归档: https://rubygems.org/downloads/ryansch-resque-loner-1.0.1.2.gem
- 版本锁定: `gem "ryansch-resque-loner", "~> 1.0.1.2"`
- 中央仓库: https://rubygems.org/
