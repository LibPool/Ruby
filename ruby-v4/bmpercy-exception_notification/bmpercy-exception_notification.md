# bmpercy-exception_notification

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
*
* NOTE: in environment.rb, specify :lib => 'exception_notifier'

## 官网

- 主页: http://github.com/bmpercy/exception_notification
- RubyGems: https://rubygems.org/gems/bmpercy-exception_notification

## 历史版本号

- 2.0.5 (2009-11-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/bmpercy-exception_notification
- gem 安装: `gem install bmpercy-exception_notification`
- Bundler: `gem "bmpercy-exception_notification"`
- 最新版本: 2.0.5
- 最新版归档: https://rubygems.org/downloads/bmpercy-exception_notification-2.0.5.gem
- 版本锁定: `gem "bmpercy-exception_notification", "~> 2.0.5"`
- 中央仓库: https://rubygems.org/
