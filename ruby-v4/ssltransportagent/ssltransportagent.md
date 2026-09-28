# ssltransportagent

**Tag**: web, database, testing, security, networking, data

## 简介

SSL Transport Agent is a foundation for all applications that may be classified as Transport Agents (TA). A TA listens to one or more TCP ports and when a connection is made to a listening port, a process is dispatched to communicate with that connection. The most common examples of this type of application are Mail Transport Agents (commonly known as Mail Servers), HTTPS Server (commonly known as a Web Server), Mail Delivery Agents (DOVECOT, for example), and other applications that exchange data through the internet.

This gem only handles the interface to the network. The application which will process the data (yours) sits on top of this layer.

This gem can operate in plain text or encrypted mode, and provides methods for issuing queries to MySQL and DNS. At the time of this writing, it contains only an AUTH PLAIN authentication method.

The test application is a full, multi-port, multi-process SMTP receiver with TLS encryption and PLAIN authentication which demonstrates how the SSL Transport Agent is used.

This gem is also an excellent demonstration of how to make SSLSockets work, for those interested in such things.

This gem (C) 2015 Michael J. Welch, Ph.D. &lt;mjwelchphd@gmail.com&gt;

Source code and documentation can be found on GitHub: https://github.com/mjwelchphd/ssltransportagent

## 官网

- 主页: http://rubygems.org/gems/ssltransportagentgemtest.rb
- 文档: https://www.rubydoc.info/gems/ssltransportagent/1.11
- RubyGems: https://rubygems.org/gems/ssltransportagent

## 历史版本号

- 1.11-x86_64-linux (2015-12-04)
- 1.10-x86_64-linux (2015-11-26)
- 1.09-x86_64-linux (2015-11-18)
- 1.08-x86_64-linux (2015-11-13)
- 1.07-x86_64-linux (2015-11-08)
- 1.06-x86_64-linux (2015-10-31)
- 1.05-x86_64-linux (2015-10-30)
- 1.04-x86_64-linux (2015-10-30)
- 1.03-x86_64-linux (2015-10-29)
- 1.02-x86_64-linux (2015-10-28)
- 1.01-x86_64-linux (2015-10-21)
- 1.0-x86_64-linux (2015-10-18)
- 0.9-x86_64-linux (2015-10-18)
- 0.8-x86_64-linux (2015-10-15)
- 0.7-x86_64-linux (2015-10-12)
- 0.6-x86_64-linux (2015-10-11)
- 0.5-x86_64-linux (2015-10-10)
- 0.4-x86_64-linux (2015-10-04)
- 0.3-x86_64-linux (2015-10-01)
- 0.2-x86_64-linux (2015-09-30)
- 0.1-x86_64-linux (2015-09-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/ssltransportagent
- gem 安装: `gem install ssltransportagent`
- Bundler: `gem "ssltransportagent"`
- 最新版本: 1.11
- 最新版归档: https://rubygems.org/downloads/ssltransportagent-1.11.gem
- 版本锁定: `gem "ssltransportagent", "~> 1.11"`
- 中央仓库: https://rubygems.org/
