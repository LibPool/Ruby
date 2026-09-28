# resque-queue-lock

**Tag**: library

## 简介

A Resque plugin. If you want only one instance of your job
queued at a time, extend it with this module.

For example:

    class ExampleJob
      extend Resque::Jobs::Queue::Lock

      def self.perform(repo_id)
        heavy_lifting
      end
    end

## 官网

- 主页: http://github.com/mashion/resque-queue-lock
- RubyGems: https://rubygems.org/gems/resque-queue-lock

## 历史版本号

- 0.0.1 (2013-01-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-queue-lock
- gem 安装: `gem install resque-queue-lock`
- Bundler: `gem "resque-queue-lock"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/resque-queue-lock-0.0.1.gem
- 版本锁定: `gem "resque-queue-lock", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
