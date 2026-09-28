# resque-lonely_job

**Tag**: library

## 简介

💎 Ensures that for a given queue, only one worker is working on a job at any given time.

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

- 主页: https://resque-lonely-job.galtzo.com
- 源码仓库: https://github.com/resque/resque-lonely_job/tree/v1.1.4
- 文档: https://www.rubydoc.info/gems/resque-lonely_job/1.1.4
- 更新日志: https://github.com/resque/resque-lonely_job/blob/v1.1.4/CHANGELOG.md
- 问题追踪: https://github.com/resque/resque-lonely_job/issues
- RubyGems: https://rubygems.org/gems/resque-lonely_job

## 历史版本号

- 1.1.4 (2026-08-27)
- 1.1.3 (2014-08-13)
- 1.0.2 (2014-02-10)
- 1.0.1 (2014-01-05)
- 1.0.0 (2014-01-05)
- 0.0.4 (2013-01-28)
- 0.0.3 (2012-06-14)
- 0.0.2 (2012-05-24)
- 0.0.1 (2012-05-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-lonely_job
- gem 安装: `gem install resque-lonely_job`
- Bundler: `gem "resque-lonely_job"`
- 最新版本: 1.1.4
- 最新版归档: https://rubygems.org/downloads/resque-lonely_job-1.1.4.gem
- 版本锁定: `gem "resque-lonely_job", "~> 1.1.4"`
- 中央仓库: https://rubygems.org/
