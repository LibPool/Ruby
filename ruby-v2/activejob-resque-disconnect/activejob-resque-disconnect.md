# activejob-resque-disconnect

**Tag**: database, data

## 简介

If you're using ActiveRecord with Resque, a new database connection will get opened
    for each worker process. When the worker completes, this connection is left open by
    default, which is pretty bad. This adapter closes the connection when the job has_rdoc
    finished executing.

## 官网

- 主页: http://github.com/gocardless/activejob-resque-disconnect
- 文档: https://www.rubydoc.info/gems/activejob-resque-disconnect/0.1.0
- RubyGems: https://rubygems.org/gems/activejob-resque-disconnect

## 历史版本号

- 0.1.0 (2015-01-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/activejob-resque-disconnect
- gem 安装: `gem install activejob-resque-disconnect`
- Bundler: `gem "activejob-resque-disconnect"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/activejob-resque-disconnect-0.1.0.gem
- 版本锁定: `gem "activejob-resque-disconnect", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
