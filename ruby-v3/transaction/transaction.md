# transaction

**Tag**: cli, database

## 简介

Record status along with other relevant information of
  transactions or tasks. These tasks can be a cron job, large background jobs or
  a simple method. Any task can be plugged into a transaction block. Transaction
  uses Redis to store the current status along with other information.
  The events within the transaction block can be published via Pubsub client
  (ex. Pusher, PubNub or any valid pubsub client).These events can be
  subscribed in the client app for the live status of the transaction.

## 官网

- 主页: https://github.com/t2013anurag/transaction
- 文档: https://www.rubydoc.info/gems/transaction/1.0.0
- RubyGems: https://rubygems.org/gems/transaction

## 历史版本号

- 1.0.0 (2019-08-11)
- 0.1.7 (2019-07-21)
- 0.1.6.beta (2019-07-19)
- 0.1.5 (2019-07-19)
- 0.1.4 (2019-07-18)
- 0.1.3 (2019-07-18)
- 0.1.2 (2019-07-18)
- 0.1.1 (2019-07-18)
- 0.1.0 (2019-07-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/transaction
- gem 安装: `gem install transaction`
- Bundler: `gem "transaction"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/transaction-1.0.0.gem
- 版本锁定: `gem "transaction", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
