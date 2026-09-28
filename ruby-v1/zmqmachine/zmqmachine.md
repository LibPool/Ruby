# zmqmachine

**Tag**: networking, filesystem

## 简介

ZMQMachine is another Ruby implementation of the reactor pattern but this
time using 0mq sockets rather than POSIX sockets.

Unlike the great Eventmachine ruby project and the Python Twisted
project which work with POSIX sockets, ZMQMachine is inherently threaded. The
0mq sockets backing the reactor use a thread pool for performing
their work so already it is different from most other reactors. Also, a
single program may create multiple reactor instances which runs in
its own thread. All activity within the reactor is single-threaded
and asynchronous.

It is possible to extend the 0mq library to "poll" normal file
descriptors. This isn't on my roadmap but patches are accepted.

## 官网

- 主页: http://github.com/chuckremes/zmqmachine
- RubyGems: https://rubygems.org/gems/zmqmachine

## 历史版本号

- 0.7.1 (2011-12-01)
- 0.6.0 (2011-10-24)
- 0.5.2 (2011-09-13)
- 0.5.0 (2011-05-03)
- 0.4.0 (2010-12-22)
- 0.3.2 (2010-08-31)
- 0.3.1 (2010-08-16)
- 0.3.0 (2010-08-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/zmqmachine
- gem 安装: `gem install zmqmachine`
- Bundler: `gem "zmqmachine"`
- 最新版本: 0.7.1
- 最新版归档: https://rubygems.org/downloads/zmqmachine-0.7.1.gem
- 版本锁定: `gem "zmqmachine", "~> 0.7.1"`
- 中央仓库: https://rubygems.org/
