# resque-lock

**Tag**: networking

## 简介

A Resque plugin. If you want only one instance of your job
queued at a time, extend it with this module.

For example:

    class UpdateNetworkGraph
      extend Resque::Jobs::Locked

      def self.perform(repo_id)
        heavy_lifting
      end
    end

## 官网

- 主页: http://github.com/defunkt/resque-lock
- RubyGems: https://rubygems.org/gems/resque-lock

## 历史版本号

- 1.1.0 (2012-11-08)
- 1.0.0 (2011-08-18)
- 0.1.1 (2010-04-01)
- 0.1.0 (2010-04-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-lock
- gem 安装: `gem install resque-lock`
- Bundler: `gem "resque-lock"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/resque-lock-1.1.0.gem
- 版本锁定: `gem "resque-lock", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
