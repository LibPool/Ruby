# resque-progress

**Tag**: library

## 简介

A Resque plugin that provides helpers for progress updates from within your 
jobs.

For example:

    class MyJob
      extend Resque::Plugins::Progress

      def self.perform(meta_id, *args)
        (0..10).each do |i|
          at(i, 10, "Lifted #{num} heavy things. #{10-num} more to go!")
          heavy_lifting(i)
        end
      end
    end

    meta0 = MyJob.enqueue('stuff')
    meta0.progress.num_complete # => 0
    meta0.progress.total # => 10
    meta0.progress.percent # => 100
    meta0.progress.message # => nil

    # later
    meta1 = MyJob.get_meta('03c9e1a045ad012dd20500264a19273c')
    meta1.progress.num_complete # => 4
    meta1.progress.total # => 10
    meta1.progress.percent # => 40
    meta1.progress.message # => 'Lifted 4 heavy things. 6 more to go!'

## 官网

- 主页: http://github.com/idris/resque-progress
- 问题追踪: http://github.com/idris/resque-progress/issues
- RubyGems: https://rubygems.org/gems/resque-progress

## 历史版本号

- 1.0.1 (2010-08-25)
- 1.0.0 (2010-08-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-progress
- gem 安装: `gem install resque-progress`
- Bundler: `gem "resque-progress"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/resque-progress-1.0.1.gem
- 版本锁定: `gem "resque-progress", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
