# logrotate

**Tag**: testing, filesystem

## 简介

This package is a library of methods that perform log rotation on files and 
directories.  The log rotate methods allow the caller to specify options (via
parameters) such as how many rotated files to keep, what type of
extension to place on the rotated file (date or a simple count), and
whether to zip the rotated files.  Live log files (currently being
written to by a live process) can be rotated as well.  The post_rotate
option is useful in that context, as it can be used to send a HUP
signal to notify the live process to reopen its log file.

This package was inspired by the need to have a library version of the
unix logrotate tool.  The unix logrotate tool requires the user to
specify options in a config file, and is usually invoked through cron.

Directories can be rotated with this library.  However, the gzip option
does not work with directories.  In this case, please zip/tar the directory
in question before invoking this library.

## 官网

- 主页: http://www.rubyforge.org/projects/logrotate
- 文档: http://logrotate.rubyforge.org
- RubyGems: https://rubygems.org/gems/logrotate

## 历史版本号

- 1.2.1 (2010-01-17)
- 1.2.0 (2009-10-21)
- 1.1.0 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/logrotate
- gem 安装: `gem install logrotate`
- Bundler: `gem "logrotate"`
- 最新版本: 1.2.1
- 最新版归档: https://rubygems.org/downloads/logrotate-1.2.1.gem
- 版本锁定: `gem "logrotate", "~> 1.2.1"`
- 中央仓库: https://rubygems.org/
