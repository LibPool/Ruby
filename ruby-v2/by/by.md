# by

**Tag**: web, cli, networking

## 简介

by is a library preloader for ruby designed to speed up process startup.
It uses a client/server approach, where the server loads the libraries and
listens on a UNIX socket, and the client connects to that socket to run
processes.  For each client connection, the server forks a worker process,
which uses the current directory, stdin, stdout, stderr, and environment
of the client process.  The worker process then processes the arguments
provided by the client. The client process waits until the worker process
closes the socket, which the worker process attempts to do right before
it exits.

## 官网

- 主页: http://github.com/jeremyevans/by
- 源码仓库: https://github.com/jeremyevans/by
- 更新日志: https://github.com/jeremyevans/by/blob/master/CHANGELOG
- 问题追踪: https://github.com/jeremyevans/by/issues
- RubyGems: https://rubygems.org/gems/by

## 历史版本号

- 1.1.0 (2024-11-06)
- 1.0.1 (2023-02-09)
- 1.0.0 (2023-02-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/by
- gem 安装: `gem install by`
- Bundler: `gem "by"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/by-1.1.0.gem
- 版本锁定: `gem "by", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
