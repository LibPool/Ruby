# activestorage-aws-record

**Tag**: devops, data

## 简介

A metadata backend that lets Active Storage store its Blob, Attachment, and
VariantRecord rows in Amazon DynamoDB (through the aws-record gem) instead of
Active Record. Blob bytes still flow through any Active Storage Service
(Disk, S3, ...); only the metadata lives in DynamoDB. Implements the generic
custom Active Storage backend contract.

## 官网

- 主页: https://github.com/thomaswitt/activestorage-aws-record
- 更新日志: https://github.com/thomaswitt/activestorage-aws-record/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/activestorage-aws-record

## 历史版本号

- 0.1.0 (2026-06-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/activestorage-aws-record
- gem 安装: `gem install activestorage-aws-record`
- Bundler: `gem "activestorage-aws-record"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/activestorage-aws-record-0.1.0.gem
- 版本锁定: `gem "activestorage-aws-record", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
