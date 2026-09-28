# fault_tolerant_router

**Tag**: web, testing, networking, filesystem

## 简介

A daemon, running in background on a Linux router or firewall, monitoring the state of multiple internet uplinks and changing the routing accordingly. LAN/DMZ internet traffic (outgoing connections) is load balanced between the uplinks using Linux multipath routing. The daemon monitors the state of the uplinks by routinely pinging well known IP addresses (Google public DNS servers, etc.) through each outgoing interface: once an uplink goes down, it is excluded from the multipath routing, when it comes back up, it is included again. An uplink may be assigned to a priority group: lower priority uplinks will only be used if all higher priority ones are down. That's useful to only use pay-per-traffic uplinks if no regular uplink is working. All of the routing changes are notified to the administrator by email. Fault Tolerant Router is well tested and has been used in production for several years, in several sites. See https://github.com/drsound/fault_tolerant_router for full documentation.

## 官网

- 主页: https://github.com/drsound/fault_tolerant_router
- 问题追踪: https://github.com/drsound/fault_tolerant_router/issues
- RubyGems: https://rubygems.org/gems/fault_tolerant_router

## 历史版本号

- 1.2.0 (2016-07-05)
- 1.1.0 (2015-06-28)
- 1.0.1 (2015-03-10)
- 1.0.0 (2015-02-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/fault_tolerant_router
- gem 安装: `gem install fault_tolerant_router`
- Bundler: `gem "fault_tolerant_router"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/fault_tolerant_router-1.2.0.gem
- 版本锁定: `gem "fault_tolerant_router", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
