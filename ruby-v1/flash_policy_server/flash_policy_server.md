# flash_policy_server

**Tag**: web, cli, serialization, networking, filesystem

## 简介

This is a simple Ruby-based policy server to serve Flash's crossdomain.xml
    policy file.

    The web is increasingly realtime, but websockets still aren't supported on
    older browser clients. Many server push libraries (e.g. socket.io) attempt
    to use websockets, with a Flash fallback. Others (amqp.js, for instance)
    are Flash only.

    When using Flash sockets, it's necessary to have a policy server running on
    port 843, in order to set cross domain policy. This library does the job.

## 官网

- 主页: http://github.com/futurechimp/flash_policy_server
- 文档: https://www.rubydoc.info/gems/flash_policy_server/0.2.0
- RubyGems: https://rubygems.org/gems/flash_policy_server

## 历史版本号

- 0.2.0 (2018-02-12)
- 0.1.0 (2013-10-12)
- 0.0.9 (2012-01-03)
- 0.0.8 (2011-12-26)
- 0.0.7 (2011-12-25)
- 0.0.6 (2011-12-25)
- 0.0.5 (2011-12-25)
- 0.0.4 (2011-12-25)
- 0.0.3 (2011-12-25)
- 0.0.2 (2011-12-25)
- 0.0.1 (2011-12-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/flash_policy_server
- gem 安装: `gem install flash_policy_server`
- Bundler: `gem "flash_policy_server"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/flash_policy_server-0.2.0.gem
- 版本锁定: `gem "flash_policy_server", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
