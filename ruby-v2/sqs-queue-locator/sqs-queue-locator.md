# sqs-queue-locator

**Tag**: web

## 简介

Amazon SQS queue names need to be unique at the account level.
This gem implements a simple naming convention of <environment>-<queue-name> to
allow your app to have keep track of queues per environment.

For the development environment, an extra prefix is added based on your machine's
hostname so that multiple developers can work at the same time without stepping
on each others' queues.

## 官网

- 主页: http://github.com/flipstone/sqs-queue-locator
- RubyGems: https://rubygems.org/gems/sqs-queue-locator

## 历史版本号

- 0.0.2 (2012-06-28)
- 0.0.1 (2012-05-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/sqs-queue-locator
- gem 安装: `gem install sqs-queue-locator`
- Bundler: `gem "sqs-queue-locator"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/sqs-queue-locator-0.0.2.gem
- 版本锁定: `gem "sqs-queue-locator", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
