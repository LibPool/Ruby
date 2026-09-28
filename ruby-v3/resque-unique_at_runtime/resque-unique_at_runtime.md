# resque-unique_at_runtime

**Tag**: library

## 简介

Ensures that for a given queue, only one worker is working on a job at any given time.

Example:

  require 'resque/plugins/unique_at_runtime'

  class StrictlySerialJob
    include Resque::Plugins::UniqueAtRuntime

    @queue = :serial_work

    def self.perform
      # only one at a time in this block, no parallelism allowed for this
      # particular queue
    end
  end

## 官网

- 主页: https://resque-unique-at-runtime.galtzo.com
- 源码仓库: https://github.com/resque/resque-unique_at_runtime/tree/v4.0.2
- 文档: https://www.rubydoc.info/gems/resque-unique_at_runtime/4.0.2
- 更新日志: https://github.com/resque/resque-unique_at_runtime/blob/v4.0.2/CHANGELOG.md
- 问题追踪: https://github.com/resque/resque-unique_at_runtime/issues
- RubyGems: https://rubygems.org/gems/resque-unique_at_runtime

## 历史版本号

- 4.0.2 (2026-08-27)
- 4.0.1 (2018-11-15)
- 4.0.0 (2018-11-15)
- 3.0.2 (2018-11-10)
- 3.0.1 (2018-11-10)
- 3.0.0 (2018-11-08)
- 2.0.4 (2018-09-10)
- 2.0.3 (2017-11-17)
- 2.0.2 (2017-11-17)
- 2.0.1 (2017-10-01)
- 2.0.0 (2017-10-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-unique_at_runtime
- gem 安装: `gem install resque-unique_at_runtime`
- Bundler: `gem "resque-unique_at_runtime"`
- 最新版本: 4.0.2
- 最新版归档: https://rubygems.org/downloads/resque-unique_at_runtime-4.0.2.gem
- 版本锁定: `gem "resque-unique_at_runtime", "~> 4.0.2"`
- 中央仓库: https://rubygems.org/
