# nogara-resque-loner

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

- 主页: http://github.com/jayniz/resque-loner
- RubyGems: https://rubygems.org/gems/nogara-resque-loner

## 历史版本号

- 1.2.1 (2012-08-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/nogara-resque-loner
- gem 安装: `gem install nogara-resque-loner`
- Bundler: `gem "nogara-resque-loner"`
- 最新版本: 1.2.1
- 最新版归档: https://rubygems.org/downloads/nogara-resque-loner-1.2.1.gem
- 版本锁定: `gem "nogara-resque-loner", "~> 1.2.1"`
- 中央仓库: https://rubygems.org/
