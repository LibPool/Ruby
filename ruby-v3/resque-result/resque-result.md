# resque-result

**Tag**: serialization

## 简介

If you want to be able fetch the result from a Resque
job's perform method.  Results will be encoded using JSON.

  For example:

      require 'resque-result'

      class MyJob
        extend Resque::Plugins::Result

        def self.perform(meta_id, big_num)
          factor(big_num)
        end
      end

      meta0 = MyJob.enqueue(3574406403731)
      meta0.enqueued_at # => 'Wed May 19 13:42:41 -0600 2010'
      meta0.meta_id # => '03c9e1a045ad012dd20500264a19273c'

      # later
      meta1 = MyJob.get_meta('03c9e1a045ad012dd20500264a19273c')
      meta1.succeeded? # => true
      meta1.result # => [ 1299709, 2750159 ]

## 官网

- 主页: http://github.com/lmarlow/resque-result
- RubyGems: https://rubygems.org/gems/resque-result

## 历史版本号

- 1.0.1 (2010-09-11)
- 1.0.0 (2010-06-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-result
- gem 安装: `gem install resque-result`
- Bundler: `gem "resque-result"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/resque-result-1.0.1.gem
- 版本锁定: `gem "resque-result", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
