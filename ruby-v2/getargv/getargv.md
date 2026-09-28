# getargv

**Tag**: web, networking, filesystem

## 简介

== Getargv
Getargv is a gem that allows you to query the arguments of other processes as an array or string.

This gem only supports macOS because the +KERN_PROCARGS2+ sysctl only exists in xnu kernels, BSD or Linux users should just read <code>/proc/$PID/cmdline</code> which is much easier and faster, Solaris users should use pargs.

This gem requires you have {libgetargv}[https://getargv.narzt.cam/] installed.

To limit the getargv gem to Apple OSs add it to your Gemfile like so:

  gem "getargv", "~> 0.3.21", platforms: :ruby, install_if: RbConfig::CONFIG["host_os"].include?("darwin")

## 官网

- 主页: https://getargv.narzt.cam/
- 源码仓库: https://github.com/getargv/getargv.rb
- 文档: https://rubydoc.info/gems/getargv/Getargv
- 更新日志: https://github.com/getargv/getargv.rb/blob/v0.3.21/CHANGELOG.md
- 问题追踪: https://github.com/getargv/getargv.rb/issues
- RubyGems: https://rubygems.org/gems/getargv

## 历史版本号

- 0.3.21-universal-darwin (2026-08-12)
- 0.3.20-universal-darwin (2026-07-24)
- 0.3.19-universal-darwin (2026-04-24)
- 0.3.18-universal-darwin (2026-03-28)
- 0.3.17-universal-darwin (2026-03-21)
- 0.3.16-universal-darwin (2026-03-21)
- 0.3.15-universal-darwin (2026-03-20)
- 0.3.14-universal-darwin (2026-03-19)
- 0.3.13-universal-darwin (2026-02-22)
- 0.3.12-universal-darwin (2026-01-07)
- 0.3.11-universal-darwin (2025-10-10)
- 0.3.10-universal-darwin (2025-05-09)
- 0.3.9-universal-darwin (2025-03-23)
- 0.3.8-universal-darwin (2025-01-24)
- 0.3.7-universal-darwin (2024-08-05)
- 0.3.6-universal-darwin (2024-05-28)
- 0.3.5-universal-darwin (2023-12-29)
- 0.3.4-universal-darwin (2023-12-29)
- 0.3.3-universal-darwin (2023-12-29)
- 0.3.2-universal-darwin (2023-12-29)
- 0.3.0-universal-darwin (2023-03-08)
- 0.2.0-universal-darwin (2023-01-05)
- 0.1.0-x86_64-darwin-21 (2023-01-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/getargv
- gem 安装: `gem install getargv`
- Bundler: `gem "getargv"`
- 最新版本: 0.3.21
- 最新版归档: https://rubygems.org/downloads/getargv-0.3.21.gem
- 版本锁定: `gem "getargv", "~> 0.3.21"`
- 中央仓库: https://rubygems.org/
