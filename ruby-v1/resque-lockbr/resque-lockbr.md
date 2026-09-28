# resque-lockbr

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
- RubyGems: https://rubygems.org/gems/resque-lockbr

## 历史版本号

- 1.1.1br (2013-04-10)
- 1.1.0br (2013-04-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-lockbr
- gem 安装: `gem install resque-lockbr`
- Bundler: `gem "resque-lockbr"`
- 最新版本: 1.1.1br
- 最新版归档: https://rubygems.org/downloads/resque-lockbr-1.1.1br.gem
- 版本锁定: `gem "resque-lockbr", "~> 1.1.1br"`
- 中央仓库: https://rubygems.org/
