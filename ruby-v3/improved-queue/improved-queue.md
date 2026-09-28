# improved-queue

**Tag**: testing, data

## 简介

A simple elaboration on Ruby's native SizedQueue which allows using the queue
object to re-awaken a blocked thread and cause it to abandon its blocking
enqueue/dequeue operation. Useful for simplifying program logic, reducing the
need for external flags/Muteces (yes, I said Muteces), and for cleanly
resolving queues on program termination without risk of data loss or deadlock.

Why use this queue? There are two reasons. For one thing, under several
circumstances it is _considerably_ faster than Ruby's native SizedQueue. I
admit I'm not entirely sure why, but I have tested this on multiple platforms
and it seems to hold true as a generality. You can feel free to confirm or
dispel that this advantage holds for your use case at your own leisure.

The second reason is the aforementioned simplification of program logic.
In the case that all data passing through the queues must be preserved on
program termination, SizedQueue can require some elaborate trickery to ensure
that even the most remote possibility of deadlock is removed.
ImprovedSizedQueue solves this problem by making it possible to use the queue
to pass control messages between threads, irrespective of the queue's actual
content.

## 官网

- 主页: http://rubygems.org/gems/improved-queue
- 文档: https://www.rubydoc.info/gems/improved-queue/1.0
- RubyGems: https://rubygems.org/gems/improved-queue

## 历史版本号

- 1.0 (2013-10-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/improved-queue
- gem 安装: `gem install improved-queue`
- Bundler: `gem "improved-queue"`
- 最新版本: 1.0
- 最新版归档: https://rubygems.org/downloads/improved-queue-1.0.gem
- 版本锁定: `gem "improved-queue", "~> 1.0"`
- 中央仓库: https://rubygems.org/
