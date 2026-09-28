# resque-alive

**Tag**: web, networking, devops

## 简介

resque-alive adds a Kubernetes Liveness probe to a Resque instance.

How?

resque-alive provides a small rack application which
exposes HTTP endpoint to return the "Aliveness" of the Resque
instance. Aliveness is determined by the presence of an
auto-expiring key. resque-alive schedules a "heartbeat"
job to periodically refresh the expiring key - in the event the
Resque instance can"t process the job, the key expires and the
instance is marked as unhealthy.

## 官网

- 主页: https://github.com/indiebrain/resque-alive
- 更新日志: https://github.com/indiebrain/resque-alive/blob/master/changelog.txt
- RubyGems: https://rubygems.org/gems/resque-alive

## 历史版本号

- 0.1.0 (2020-09-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-alive
- gem 安装: `gem install resque-alive`
- Bundler: `gem "resque-alive"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/resque-alive-0.1.0.gem
- 版本锁定: `gem "resque-alive", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
