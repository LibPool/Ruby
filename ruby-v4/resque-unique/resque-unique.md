# resque-unique

**Tag**: networking

## 简介

A Resque plugin. If you want only one instance of your job
queued at a time, extend it with this module.

For example:

    class UpdateNetworkGraph
      extend Resque::Plugins::Unique

      def self.perform(repo_id)
        heavy_lifting
      end
    end

## 官网

- 主页: http://github.com/ronny/resque-unique
- RubyGems: https://rubygems.org/gems/resque-unique

## 历史版本号

- 0.1.0 (2012-09-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-unique
- gem 安装: `gem install resque-unique`
- Bundler: `gem "resque-unique"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/resque-unique-0.1.0.gem
- 版本锁定: `gem "resque-unique", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
