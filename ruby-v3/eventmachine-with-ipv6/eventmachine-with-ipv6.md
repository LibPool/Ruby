# eventmachine-with-ipv6

**Tag**: web, cli, testing, networking, filesystem, data

## 简介

EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal
of EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.

The present alternative version 'eventmachine-with-ipv6' contains some
crucial fixes for datagrams (UDP) and IPv6 developed since 2010 by
Carsten Bormann and Iñaki Baz Castillo.  This is needed for many
applications in 2012, but might detract from the stability achieved
for other typical uses of the base eventmachine.  It is otherwise
identical with base eventmachine.  Install either base eventmachine or
this version eventmachine-with-ipv6.  If you have installed both, use
gem 'eventmachine-with-ipv6'
before
require 'eventmachine'
Alternatively use Bundler and write this in your gemfile:
gem "eventmachine", :git => "git://github.com/cabo/eventmachine"

Please send all bugs in this version to https://github.com/cabo/eventmachine/issues

## 官网

- 主页: http://github.com/cabo/eventmachine
- RubyGems: https://rubygems.org/gems/eventmachine-with-ipv6

## 历史版本号

- 1.0.0.beta.4.ipv6.0 (2012-02-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/eventmachine-with-ipv6
- gem 安装: `gem install eventmachine-with-ipv6`
- Bundler: `gem "eventmachine-with-ipv6"`
- 最新版本: 1.0.0.beta.4.ipv6.0
- 最新版归档: https://rubygems.org/downloads/eventmachine-with-ipv6-1.0.0.beta.4.ipv6.0.gem
- 版本锁定: `gem "eventmachine-with-ipv6", "~> 1.0.0.beta.4.ipv6.0"`
- 中央仓库: https://rubygems.org/
