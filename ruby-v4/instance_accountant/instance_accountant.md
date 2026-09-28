# instance_accountant

**Tag**: web, devops, filesystem

## 简介

The instance_accountant gem is designed to be used to account
    for hourly resource consumption, such as EC2 instances, using
    Subledger, the double-entry accounting API.

    It can account for both cost (amount owed to AWS) as well as price
    (amount owed to instance owner). If you run hourly-billed instances
    for yourself, or for others, and want real-time usage information
    for yourself, and for those paying you for the instance, then this
    gem is for you. :-)

    instance_accountant keeps state in an "hourfile" that contains the
    timestamp of the last hour accounted for. It is intended to be run
    in --daemon mode at startup. It makes no effort to account for
    instance time when it is not running, so it's important to run it
    immediately upon startup, and to make sure that it is always running.

## 官网

- 主页: https://github.com/subledger/instance_accountant
- 文档: https://www.rubydoc.info/gems/instance_accountant/0.0.4
- RubyGems: https://rubygems.org/gems/instance_accountant

## 历史版本号

- 0.0.4 (2014-11-07)
- 0.0.3 (2014-11-07)
- 0.0.2 (2014-11-05)
- 0.0.1 (2014-11-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/instance_accountant
- gem 安装: `gem install instance_accountant`
- Bundler: `gem "instance_accountant"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/instance_accountant-0.0.4.gem
- 版本锁定: `gem "instance_accountant", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
