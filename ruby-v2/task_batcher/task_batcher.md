# task_batcher

**Tag**: database, data

## 简介

Some tasks, like database inserts, are much more efficient to process in a
batch.  However, we generally want our tasks to be processed "soon" even if
there's only one task.  The TaskBatcher gem groups tasks by a taskname
parameter, and starts a timer when the first task comes in.  After the batch
timer expires, it processes all tasks that it received in that time.  (The
caller provides the block to process the tasks.)

Uses EventMachine under the hood.  May be combined with Messenger for
durability guarantees.

## 官网

- 主页: http://github.com/apartmentlist
- RubyGems: https://rubygems.org/gems/task_batcher

## 历史版本号

- 0.1.0 (2013-04-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/task_batcher
- gem 安装: `gem install task_batcher`
- Bundler: `gem "task_batcher"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/task_batcher-0.1.0.gem
- 版本锁定: `gem "task_batcher", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
