# puma-daemon

**Tag**: web, testing, security, devops

## 简介

In version 5.0 the authors of the popular Ruby web server Puma chose to remove the 
daemonization support from Puma, because the code wasn't wall maintained,
and because other and better options exist for production deployments. For example
systemd, Docker/Kubernetes, Heroku, etc. 

Having said that, it was neat and often useful to daemonize Puma in development.
This gem adds this support to Puma 5 & 6 (hopefully) without breaking anything in Puma
itself.

So, if you want to use the latest and greatest Puma 5+, but prefer to keep using built-in
daemonization, this gem if for you.

## 官网

- 主页: https://github.com/kigster/puma-daemon
- 更新日志: https://github.com/kigster/puma-daemon/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/puma-daemon

## 历史版本号

- 0.5.0 (2024-12-04)
- 0.3.2 (2023-06-22)
- 0.3.0 (2023-03-14)
- 0.2.3 (2023-03-14)
- 0.2.2 (2023-03-07)
- 0.1.2 (2021-03-05)
- 0.1.1 (2021-01-24)
- 0.1.0 (2021-01-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/puma-daemon
- gem 安装: `gem install puma-daemon`
- Bundler: `gem "puma-daemon"`
- 最新版本: 0.5.0
- 最新版归档: https://rubygems.org/downloads/puma-daemon-0.5.0.gem
- 版本锁定: `gem "puma-daemon", "~> 0.5.0"`
- 中央仓库: https://rubygems.org/
