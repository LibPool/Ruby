# Sutto-em-redis

**Tag**: web, cli, database, networking, data

## 简介

An EventMachine[http://rubyeventmachine.com/] based library for interacting with the very cool Redis[http://code.google.com/p/redis/] data store by Salvatore 'antirez' Sanfilippo. Modeled after eventmachine's implementation of the memcached protocol, and influenced by Ezra Zygmuntowicz's {redis-rb}[http://github.com/ezmobius/redis-rb/tree/master] library (distributed as part of Redis).  This library is only useful when used as part of an application that relies on Event Machine's event loop.  It implements an EM-based client protocol, which leverages the non-blocking nature of the EM interface to acheive significant parallelization without threads.  WARNING: this library is my first attempt to write an evented client protocol, and isn't currently used in production anywhere.  All that bit in the license about not being warranted to work for any particular purpose really applies.

## 官网

- 文档: https://www.rubydoc.info/gems/Sutto-em-redis/0.1.1
- RubyGems: https://rubygems.org/gems/Sutto-em-redis

## 历史版本号

- 0.1.1 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/Sutto-em-redis
- gem 安装: `gem install Sutto-em-redis`
- Bundler: `gem "Sutto-em-redis"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/Sutto-em-redis-0.1.1.gem
- 版本锁定: `gem "Sutto-em-redis", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
