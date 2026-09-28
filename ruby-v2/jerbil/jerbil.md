# jerbil

**Tag**: web, cli, networking

## 简介

Provides a reliable Object Request Broker and a simple framework for ruby-based services.
Jerbil servers run on each machine in the system and share information on registering
services. This ensures no single point of failure - machines can come and go (orderly or disorderly)
and the network extends or heals as they do. For services there is a parent class that hides 
all of the jerbil server interactions so that new services can be written without having
to write any distributing code. Clients can also be written using an interface that
can find one or more services on the network and connect to each or the first. Finally, there
are scripts to start and stop the Jerbil server and any Services so that the whole thing
can be quickly installed and integrated with your system.

## 官网

- 主页: https://github.com/osburn-sharp
- 源码仓库: https://github.com/osburn-sharp/jerbil
- 文档: http://rubydoc.info/github/osburn-sharp/jerbil/frames
- 问题追踪: https://github.com/osburn-sharp/jerbil/issues
- RubyGems: https://rubygems.org/gems/jerbil

## 历史版本号

- 1.4.8 (2014-10-26)
- 1.4.7 (2014-10-21)
- 1.4.6 (2014-10-17)
- 1.4.5 (2014-10-17)
- 1.3.3 (2013-09-30)
- 1.2.2 (2012-11-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/jerbil
- gem 安装: `gem install jerbil`
- Bundler: `gem "jerbil"`
- 最新版本: 1.4.8
- 最新版归档: https://rubygems.org/downloads/jerbil-1.4.8.gem
- 版本锁定: `gem "jerbil", "~> 1.4.8"`
- 中央仓库: https://rubygems.org/
