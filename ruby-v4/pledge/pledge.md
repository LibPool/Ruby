# pledge

**Tag**: testing, filesystem

## 简介

pledge exposes OpenBSD's pledge(2) and unveil(2) system calls to Ruby, allowing
a program to restrict the types of operations the program can do, and the file
system access the program has, after the point of call.  Unlike other similar
systems, pledge and unveil are specifically designed for programs that need to
use a wide variety of operations on initialization, but a fewer number after
initialization (when user input will be accepted).

## 官网

- 主页: https://github.com/jeremyevans/ruby-pledge
- 文档: https://www.rubydoc.info/gems/pledge/1.3.0
- RubyGems: https://rubygems.org/gems/pledge

## 历史版本号

- 1.3.0 (2022-12-19)
- 1.2.0 (2019-07-07)
- 1.1.0 (2019-04-25)
- 1.0.0 (2016-11-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/pledge
- gem 安装: `gem install pledge`
- Bundler: `gem "pledge"`
- 最新版本: 1.3.0
- 最新版归档: https://rubygems.org/downloads/pledge-1.3.0.gem
- 版本锁定: `gem "pledge", "~> 1.3.0"`
- 中央仓库: https://rubygems.org/
