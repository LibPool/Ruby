# resque-worker-timeout

**Tag**: filesystem

## 简介

A Resque plugin. If you want set worker timeout, extend it with this module.
For example:
    class TransferFileWorker
      extend Resque::Plugins::WorkerTimeout

      # 10 minutes (default 10 minutes)
      @timeout = 600

      # reenqueue worker if timeout happend (default false)
      @reenqueue_worker = true

      def self.perform(file_name)
        # transfer file
      end
    end

## 官网

- 主页: https://github.com/grantchen/resque-worker-timeout
- 文档: https://www.rubydoc.info/gems/resque-worker-timeout/0.0.2
- RubyGems: https://rubygems.org/gems/resque-worker-timeout

## 历史版本号

- 0.0.2 (2015-05-16)
- 0.0.1 (2015-05-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-worker-timeout
- gem 安装: `gem install resque-worker-timeout`
- Bundler: `gem "resque-worker-timeout"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/resque-worker-timeout-0.0.2.gem
- 版本锁定: `gem "resque-worker-timeout", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
