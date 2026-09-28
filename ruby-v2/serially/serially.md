# serially

**Tag**: testing

## 简介

Have you ever had a class whose instances required a series of background tasks to run serially, strictly one after another? Than Serially is for you.
Declare the tasks using a simple DSL in the order you want them to to run. The tasks for each instance will run inside a separate Resque job, in a queue you specify. The next task will run only if the previous one has finished successfully. All task runs are written to DB and can be inspected.

## 官网

- 主页: http://github.com/mikemarsian/serially
- 文档: https://www.rubydoc.info/gems/serially/0.4.3
- RubyGems: https://rubygems.org/gems/serially

## 历史版本号

- 0.4.3 (2016-01-16)
- 0.4.2 (2016-01-16)
- 0.4.1 (2016-01-16)
- 0.4.0 (2016-01-16)
- 0.3.1 (2016-01-09)
- 0.3.0 (2016-01-09)
- 0.2.0 (2016-01-04)
- 0.1.3 (2016-01-04)
- 0.1.2 (2016-01-01)
- 0.1.1 (2016-01-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/serially
- gem 安装: `gem install serially`
- Bundler: `gem "serially"`
- 最新版本: 0.4.3
- 最新版归档: https://rubygems.org/downloads/serially-0.4.3.gem
- 版本锁定: `gem "serially", "~> 0.4.3"`
- 中央仓库: https://rubygems.org/
