# wrangler

**Tag**: web, networking, template

## 简介

A gem for handling exceptions thrown inside your Rails app. If you include the
gem in your application controller, wrangler will render the error pages you
configure for each exception or HTTP error code. It will also handle notifying
you via email when certain exceptions are raised. Allows for configuration of
which exceptions map to which error pages, which exceptions result in emails
being sent. Also allows for asynchronous email sending via delayed job so that
error pages don't take forever to load (but delayed_job is not required for
sending email; wrangler will automatically send email synchronously if
delayed_job is not available. . See README for lots of info on how to
get started and what configuration options are available.

## 官网

- 主页: http://github.com/bmpercy/wrangler
- RubyGems: https://rubygems.org/gems/wrangler

## 历史版本号

- 0.1.26 (2011-01-18)
- 0.1.25 (2010-09-22)
- 0.1.24 (2010-09-04)
- 0.1.23 (2010-08-01)
- 0.1.22 (2010-06-16)
- 0.1.21 (2010-05-19)
- 0.1.20 (2010-05-04)
- 0.1.19 (2010-04-12)
- 0.1.18 (2010-04-09)
- 0.1.17 (2010-04-03)
- 0.1.16 (2010-03-31)
- 0.1.15 (2010-03-29)
- 0.1.14 (2010-02-19)
- 0.1.13 (2010-02-10)
- 0.1.12 (2010-01-05)
- 0.1.11 (2009-12-01)
- 0.1.10 (2009-11-30)
- 0.1.9 (2009-11-30)
- 0.1.8 (2009-11-30)
- 0.1.7 (2009-11-30)
- 0.1.6 (2009-11-30)
- 0.1.5 (2009-11-30)
- 0.1.4 (2009-11-20)
- 0.1.3 (2009-11-20)
- 0.1.2 (2009-11-17)
- 0.1.1 (2009-11-13)
- 0.1.0 (2009-11-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/wrangler
- gem 安装: `gem install wrangler`
- Bundler: `gem "wrangler"`
- 最新版本: 0.1.26
- 最新版归档: https://rubygems.org/downloads/wrangler-0.1.26.gem
- 版本锁定: `gem "wrangler", "~> 0.1.26"`
- 中央仓库: https://rubygems.org/
