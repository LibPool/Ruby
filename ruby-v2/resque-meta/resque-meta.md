# resque-meta

**Tag**: web, data

## 简介

A Resque plugin.  If you want to be able to add metadata for a job
to track anything you want, extend it with this module.

For example:

    require 'resque-meta'

    class MyJob
      extend Resque::Plugins::Meta

      def self.perform(meta_id, *args)
        heavy_lifting
      end
    end

    meta0 = MyJob.enqueue('stuff')
    meta0.enqueued_at # => 'Wed May 19 13:42:41 -0600 2010'
    meta0.meta_id # => '03c9e1a045ad012dd20500264a19273c'
    meta0['foo'] = 'bar' # => 'bar'
    meta0.save

    # later
    meta1 = MyJob.get_meta('03c9e1a045ad012dd20500264a19273c')
    meta1.job_class # => MyJob
    meta1.enqueued_at # => 'Wed May 19 13:42:41 -0600 2010'
    meta1['foo'] # => 'bar'

## 官网

- 主页: http://github.com/lmarlow/resque-meta
- 文档: https://www.rubydoc.info/gems/resque-meta/2.0.1
- RubyGems: https://rubygems.org/gems/resque-meta

## 历史版本号

- 2.0.1 (2013-11-27)
- 2.0.0 (2012-12-05)
- 1.0.3 (2011-02-10)
- 1.0.2 (2010-11-04)
- 1.0.1 (2010-09-11)
- 1.0.0 (2010-06-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-meta
- gem 安装: `gem install resque-meta`
- Bundler: `gem "resque-meta"`
- 最新版本: 2.0.1
- 最新版归档: https://rubygems.org/downloads/resque-meta-2.0.1.gem
- 版本锁定: `gem "resque-meta", "~> 2.0.1"`
- 中央仓库: https://rubygems.org/
