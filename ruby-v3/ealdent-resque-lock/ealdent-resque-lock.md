# ealdent-resque-lock

**Tag**: networking

## 简介

A Resque plugin. If you want only one instance of your job
queued at a time, extend it with this module. This version
stores the timestamp in the lock.

For example:

    class UpdateNetworkGraph
      extend Resque::Jobs::Locked

      def self.perform(repo_id)
        heavy_lifting
      end
    end

## 官网

- 主页: http://github.com/ealdent/resque-lock
- RubyGems: https://rubygems.org/gems/ealdent-resque-lock

## 历史版本号

- 1.0.0 (2011-11-17)
- 0.1.2 (2010-10-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/ealdent-resque-lock
- gem 安装: `gem install ealdent-resque-lock`
- Bundler: `gem "ealdent-resque-lock"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/ealdent-resque-lock-1.0.0.gem
- 版本锁定: `gem "ealdent-resque-lock", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
