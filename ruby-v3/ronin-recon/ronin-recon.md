# ronin-recon

**Tag**: web, filesystem, data

## 简介

ronin-recon is a micro-framework and tool for performing reconnaissance.
ronin-recon uses multiple workers which process different data types
(IP, host, URL, etc) and produce new values. ronin-recon contains built-in
recon workers and supports loading additional 3rd-party workers from Ruby
files or 3rd-party git repositories. ronin-recon has a unique queue design
and uses asynchronous I/O to maximize efficiency. ronin-recon can lookup
IPs addresses, nameservers, mailservers, bruteforce sub-domains, port scan
IPs, discover services, and spider websites.

## 官网

- 源码仓库: https://github.com/ronin-rb/ronin-recon
- 文档: https://ronin-rb.dev/docs/ronin-recon
- 更新日志: https://github.com/ronin-rb/ronin-recon/blob/main/ChangeLog.md
- 问题追踪: https://github.com/ronin-rb/ronin-recon/issues
- RubyGems: https://rubygems.org/gems/ronin-recon

## 历史版本号

- 0.1.0 (2024-07-22)
- 0.1.0.rc2 (2024-07-15)
- 0.1.0.rc1 (2024-06-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/ronin-recon
- gem 安装: `gem install ronin-recon`
- Bundler: `gem "ronin-recon"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/ronin-recon-0.1.0.gem
- 版本锁定: `gem "ronin-recon", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
