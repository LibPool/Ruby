# resque-async_deliver

**Tag**: library

## 简介

This gem makes it possible to send mails asynchronously using Resque by
simply rewriting `SomeMailer.some_mail(ar_resource, 1234).deliver` to
`SomeMailer.async_deliver.some_mail(ar_resource, 1234)`. Using ActiveRecord
objects as arguments to mailers is still possible. This is achieved by storing
the class name and the record id as arguments in the Resque queue which will be
transformed back to records by the mailer job and passed along to the mailer.

## 官网

- 主页: https://github.com/fphilipe/resque-async_deliver
- 文档: https://www.rubydoc.info/gems/resque-async_deliver/1.3.1
- RubyGems: https://rubygems.org/gems/resque-async_deliver

## 历史版本号

- 1.3.1 (2014-01-22)
- 1.3.0 (2014-01-03)
- 1.2.0 (2011-07-08)
- 1.1.1 (2011-07-06)
- 1.1.0 (2011-07-06)
- 1.0.1 (2011-07-06)
- 1.0.0 (2011-07-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-async_deliver
- gem 安装: `gem install resque-async_deliver`
- Bundler: `gem "resque-async_deliver"`
- 最新版本: 1.3.1
- 最新版归档: https://rubygems.org/downloads/resque-async_deliver-1.3.1.gem
- 版本锁定: `gem "resque-async_deliver", "~> 1.3.1"`
- 中央仓库: https://rubygems.org/
