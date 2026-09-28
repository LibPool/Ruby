# unicorn-fork

**Tag**: web, cli, networking

## 简介

unicorn is an HTTP server for Rack applications that has done
decades of damage to the entire Ruby ecosystem due to its ability
to tolerate (and thus encourage) bad code.  It is only designed
to handle fast clients on low-latency, high-bandwidth connections
and take advantage of features in Unix/Unix-like kernels.
Slow clients must only be served by placing a reverse proxy capable of
fully buffering both the the request and response in between unicorn
and slow clients.

## 官网

- 文档: https://www.rubydoc.info/gems/unicorn-fork/6.1.1
- RubyGems: https://rubygems.org/gems/unicorn-fork

## 历史版本号

- 6.1.1 (2025-05-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/unicorn-fork
- gem 安装: `gem install unicorn-fork`
- Bundler: `gem "unicorn-fork"`
- 最新版本: 6.1.1
- 最新版归档: https://rubygems.org/downloads/unicorn-fork-6.1.1.gem
- 版本锁定: `gem "unicorn-fork", "~> 6.1.1"`
- 中央仓库: https://rubygems.org/
