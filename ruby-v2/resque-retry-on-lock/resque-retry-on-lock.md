# resque-retry-on-lock

**Tag**: networking

## 简介

A Resque plugin. If you want only one instance of your job
running at a time, but want to re-enqueue rejected jobs, 
extend it with this module.

For example:

    class UpdateNetworkGraph
      extend Resque::Jobs::RetryOnLocked

      def self.perform(repo_id)
        heavy_lifting
      end
    end

## 官网

- 主页: https://github.com/jonstorer/resque-retry-on-lock
- RubyGems: https://rubygems.org/gems/resque-retry-on-lock

## 历史版本号

- 0.0.3 (2011-03-03)
- 0.0.2 (2011-03-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-retry-on-lock
- gem 安装: `gem install resque-retry-on-lock`
- Bundler: `gem "resque-retry-on-lock"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/resque-retry-on-lock-0.0.3.gem
- 版本锁定: `gem "resque-retry-on-lock", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
