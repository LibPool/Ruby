# simpleemail

**Tag**: web, testing, networking, filesystem

## 简介

This package simplifies sending emails outside of the Rails
environment.  It is a wrapper around the ActionMailer package.
Support for smtp over tls is included if you are using Ruby 1.8.7 or
above.  The API provided is very bare, but can be easily extended.
The email configuration is provided through a user-specified
configuration file (identical to the ActionMailer configuration in
environment.rb in Rails except for the added tls option).  This
package is most useful in the situation that a user has a number of
scripts (outside of the Rails environment) that all send very basic
emails (to, from, body, subject).

## 官网

- 主页: http://www.rubyforge.org/projects/simpleemail
- 文档: http://simpleemail.rubyforge.org
- RubyGems: https://rubygems.org/gems/simpleemail

## 历史版本号

- 1.0.2 (2010-01-17)
- 1.0.1 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/simpleemail
- gem 安装: `gem install simpleemail`
- Bundler: `gem "simpleemail"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/simpleemail-1.0.2.gem
- 版本锁定: `gem "simpleemail", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
