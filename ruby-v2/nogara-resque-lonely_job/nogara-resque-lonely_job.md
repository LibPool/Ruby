# nogara-resque-lonely_job

**Tag**: library

## 简介

Ensures that for a given queue, only one worker is working on a job at any given time.

Example:

  require 'resque/plugins/lonely_job'

  class StrictlySerialJob
    extend Resque::Plugins::LonelyJob

    @queue = :serial_work

    def self.perform
      # only one at a time in this block, no parallelism allowed for this
      # particular queue
    end
  end

## 官网

- 主页: http://github.com/wallace/resque-lonely_job
- RubyGems: https://rubygems.org/gems/nogara-resque-lonely_job

## 历史版本号

- 0.0.3 (2012-08-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/nogara-resque-lonely_job
- gem 安装: `gem install nogara-resque-lonely_job`
- Bundler: `gem "nogara-resque-lonely_job"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/nogara-resque-lonely_job-0.0.3.gem
- 版本锁定: `gem "nogara-resque-lonely_job", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
