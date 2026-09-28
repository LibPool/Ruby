# ziltoid

**Tag**: data

## 简介

There are many software applications that aim to watch processes, and keep them alive and clean. Some of them are well known: god, monit, bluepill.
  All have good and bad sides. One of the bad sides is that each alternative is based on a deamon that computes data and then sleeps for a while. Who is monitoring this particular deamon ? What if this process suddenly stops ? Also, you often need root rights to run those tools. On some hosting environments (mainly in shared hosting), this is an issue.
  Ziltoid is an attempt to solve those issues using the crontab system, which comes with many good sides : it's on every system, it launches a task periodically then waits for an amount of time, it doesn't need monitoring, it can send emails to warn of an error and it can run any script.

## 官网

- 主页: https://github.com/meuble/ziltoid
- 问题追踪: https://github.com/meuble/ziltoid/issues
- RubyGems: https://rubygems.org/gems/ziltoid

## 历史版本号

- 1.0.2 (2018-08-06)
- 1.0.1 (2018-08-06)
- 1.0.0 (2014-12-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/ziltoid
- gem 安装: `gem install ziltoid`
- Bundler: `gem "ziltoid"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/ziltoid-1.0.2.gem
- 版本锁定: `gem "ziltoid", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
