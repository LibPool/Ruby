# mikehale-daemons

**Tag**: web, testing, networking

## 简介

This is Daemons 1.0.10 with the addition of Chris Kline's fix from http://blog.rapleaf.com/dev/?p=19  Includes ability to change the process uid/gid. Also logdir can be specified seperate from piddir.  Daemons provides an easy way to wrap existing ruby scripts (for example a self-written server) to be run as a daemon and to be controlled by simple start/stop/restart commands.  If you want, you can also use daemons to run blocks of ruby code in a daemon process and to control these processes from the main application.  Besides this basic functionality, daemons offers many advanced features like exception backtracing and logging (in case your ruby script crashes) and monitoring and automatic restarting of your processes if they crash.  Daemons includes the daemonize.rb script written by Travis Whitton to do the daemonization process.

## 官网

- 主页: http://github.com/mikehale/daemons
- 文档: https://www.rubydoc.info/gems/mikehale-daemons/1.0.12.4
- RubyGems: https://rubygems.org/gems/mikehale-daemons

## 历史版本号

- 1.0.12.1 (2014-08-11)
- 1.0.12.2 (2014-08-11)
- 1.0.12.3 (2014-08-11)
- 1.0.12.4 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/mikehale-daemons
- gem 安装: `gem install mikehale-daemons`
- Bundler: `gem "mikehale-daemons"`
- 最新版本: 1.0.12.4
- 最新版归档: https://rubygems.org/downloads/mikehale-daemons-1.0.12.4.gem
- 版本锁定: `gem "mikehale-daemons", "~> 1.0.12.4"`
- 中央仓库: https://rubygems.org/
