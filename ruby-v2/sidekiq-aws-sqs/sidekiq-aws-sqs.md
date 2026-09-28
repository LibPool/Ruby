# sidekiq-aws-sqs

**Tag**: cli, testing, devops

## 简介

sidekiq-aws-sqs is a Sidekiq extension that provides an easy way to poll and process messages from AWS SQS (Simple Queue Service) queues within a Sidekiq worker. It uses the SafePoller gem under the hood to safely poll messages at a specified interval, and gracefully handle shutdown events to avoid losing messages. It also integrates with Sidekiq's lifecycle events to start and stop the polling process automatically, and provides a simple interface to configure the SQS client and polling options.

## 官网

- 主页: https://github.com/nejdetkadir/sidekiq-aws-sqs
- RubyGems: https://rubygems.org/gems/sidekiq-aws-sqs

## 历史版本号

- 0.0.1 (2023-04-25)
- 0.0.0 (2023-04-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq-aws-sqs
- gem 安装: `gem install sidekiq-aws-sqs`
- Bundler: `gem "sidekiq-aws-sqs"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/sidekiq-aws-sqs-0.0.1.gem
- 版本锁定: `gem "sidekiq-aws-sqs", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
