# super_exception_notifier

**Tag**: web, cli, testing, networking, template, filesystem

## 简介

Allows customization of:
* Specify which level of notification you would like with an array of optional styles of notification (email, webhooks)
* the sender address of the email
* the recipient addresses
* the text used to prefix the subject line
* the HTTP status codes to notify for
* the error classes to send emails for
* alternatively, the error classes to not notify for
* whether to send error emails or just render without sending anything
* the HTTP status and status code that gets rendered with specific errors
* the view path to the error page templates
* custom errors, with custom error templates
* define error layouts at application or controller level, or use the controller's own default layout, or no layout at all
* get error notification for errors that occur in the console, using notifiable method
* Override the gem's handling and rendering with explicit rescue statements inline.
* Hooks into `git blame` output so you can get an idea of who (may) have introduced the bug
* Hooks into other website services (e.g. you can send exceptions to to Switchub.com)
* Can notify of errors occurring in any class/method using notifiable { method }
* Can notify of errors in Rake tasks using NotifiedTask.new instead of task
* Works with Hoptoad Notifier, so you can notify via SEN and/or Hoptoad for any particular errors.
* Tested with Rails 2.3.x, should work with rails 2.2.x, and is apparently not yet compatible with rails 3.

## 官网

- 主页: http://github.com/pboling/exception_notification
- 文档: http://rdoc.info/projects/pboling/exception_notification
- 问题追踪: http://github.com/pboling/exception_notification/issues
- RubyGems: https://rubygems.org/gems/super_exception_notifier

## 历史版本号

- 3.1.0 (2014-01-19)
- 3.0.16 (2014-01-19)
- 3.0.15 (2014-01-19)
- 3.0.14 (2014-01-19)
- 3.0.13 (2010-06-30)
- 3.0.12 (2010-06-25)
- 3.0.11 (2010-06-18)
- 3.0.10 (2010-06-18)
- 3.0.9 (2010-06-18)
- 3.0.8 (2010-06-12)
- 3.0.7 (2010-06-12)
- 3.0.6 (2010-05-14)
- 3.0.5 (2010-05-13)
- 3.0.4 (2010-05-13)
- 3.0.2 (2010-05-13)
- 3.0.1 (2010-05-13)
- 2.0.8 (2010-01-29)
- 2.0.7 (2009-12-30)
- 2.0.6 (2009-12-30)
- 2.0.5 (2009-12-30)
- 2.0.4 (2009-11-05)
- 2.0.3 (2009-11-05)
- 2.0.2 (2009-10-23)
- 2.0.1 (2009-10-23)
- 2.0.0 (2009-10-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/super_exception_notifier
- gem 安装: `gem install super_exception_notifier`
- Bundler: `gem "super_exception_notifier"`
- 最新版本: 3.1.0
- 最新版归档: https://rubygems.org/downloads/super_exception_notifier-3.1.0.gem
- 版本锁定: `gem "super_exception_notifier", "~> 3.1.0"`
- 中央仓库: https://rubygems.org/
