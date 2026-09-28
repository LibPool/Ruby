# dbdump_command

**Tag**: web, cli, database, data

## 简介

This plugin adds a dbdump command which dumps your Rails database out.

This master branch supports Rails 3.0 and above, as a gem command.
For Rails 2.3, use the rails_2_3 branch from github and install as a plugin.

Like rails dbconsole, it takes your database connection details from
config/database.yml, and supports mysql, mysql2, postgresql, and sqlite.

It takes the same options as rails dbconsole, ie. -p to supply the password
to your dump program for mysql and postgresql.   (Note that for mysql, this
means that the password is visible when other users on the system run 'ps'.
Postgresql does not have this problem as it uses an environment variable set
in ENV before execing and so not visible in ps.)

## 官网

- 主页: http://github.com/willbryant/dbdump_command
- 文档: https://www.rubydoc.info/gems/dbdump_command/1.3.0
- RubyGems: https://rubygems.org/gems/dbdump_command

## 历史版本号

- 1.3.0 (2013-07-06)
- 0.2.1 (2012-08-18)
- 0.2.0 (2012-08-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/dbdump_command
- gem 安装: `gem install dbdump_command`
- Bundler: `gem "dbdump_command"`
- 最新版本: 1.3.0
- 最新版归档: https://rubygems.org/downloads/dbdump_command-1.3.0.gem
- 版本锁定: `gem "dbdump_command", "~> 1.3.0"`
- 中央仓库: https://rubygems.org/
