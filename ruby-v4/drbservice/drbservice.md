# drbservice

**Tag**: security, filesystem

## 简介

DRbService is a framework we use at LAIKA for creating authenticated
SSL-encrypted DRb services that provide access to privileged operations
without the need to give shell access to everyone.

There are a few examples in the `examples/` directory of the gem, which
are stripped-down versions of the services we actually use.

The current implementation is kind of a hack, but I intend to 
eventually finish a DRb protocol that does the same thing in a more
elegant, less-hackish way, as well as a tool that can generate 
a new service along with support files for one of several different 
runtime environments.

If you're curious, see the `drb/authsslprotocol.rb` file for the 
protocol. This will replace the current method-hiding code in 
`drbservice.rb`, but existing services should be able to switch over
quite easily. Or that's the intention.

## 官网

- 主页: https://bitbucket.org/ged/drbservice
- RubyGems: https://rubygems.org/gems/drbservice

## 历史版本号

- 1.0.4 (2011-08-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/drbservice
- gem 安装: `gem install drbservice`
- Bundler: `gem "drbservice"`
- 最新版本: 1.0.4
- 最新版归档: https://rubygems.org/downloads/drbservice-1.0.4.gem
- 版本锁定: `gem "drbservice", "~> 1.0.4"`
- 中央仓库: https://rubygems.org/
