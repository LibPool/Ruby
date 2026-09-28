# resque-loner

**Tag**: testing

## 简介

Makes sure that for special jobs, there can be only one job with the same
workload in one queue.

Example:
    class CacheSweeper
       include Resque::Plugins::UniqueJob

       @queue = :cache_sweeps

       def self.perform(article_id)
         # Cache Me If You Can...
       end
    end

## 官网

- 主页: http://github.com/jayniz/resque-loner
- 问题追踪: https://github.com/jayniz/resque-loner/issues
- RubyGems: https://rubygems.org/gems/resque-loner

## 历史版本号

- 1.3.0 (2014-03-24)
- 1.2.1 (2012-04-27)
- 1.2.0 (2012-01-11)
- 1.0.1 (2011-07-15)
- 0.1.3 (2010-11-19)
- 0.1.2 (2010-08-03)
- 0.1.1 (2010-06-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-loner
- gem 安装: `gem install resque-loner`
- Bundler: `gem "resque-loner"`
- 最新版本: 1.3.0
- 最新版归档: https://rubygems.org/downloads/resque-loner-1.3.0.gem
- 版本锁定: `gem "resque-loner", "~> 1.3.0"`
- 中央仓库: https://rubygems.org/
