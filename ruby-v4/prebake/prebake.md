# prebake

**Tag**: devops, filesystem

## 简介

Prebake speeds up bundle install by skipping native gem compilation. It fetches precompiled binaries for gems like puma, nokogiri, pg, grpc, and bootsnap from a shared cache instead of compiling C extensions from source. Drop-in Bundler plugin - one line in your Gemfile, no other changes needed. Works out of the box with the hosted cache at gems.prebake.in, or self-host with S3-compatible storage (AWS S3, Cloudflare R2, Backblaze B2, MinIO) or Gemstash. Works with Ruby 3.2+ and Ruby 4.0 on any platform.

## 官网

- 主页: https://github.com/gembakery/prebake
- RubyGems: https://rubygems.org/gems/prebake

## 历史版本号

- 0.3.3 (2026-09-23)
- 0.3.2 (2026-09-13)
- 0.3.1 (2026-04-23)
- 0.3.0 (2026-04-23)
- 0.2.10 (2026-04-20)
- 0.2.9 (2026-03-31)
- 0.2.8 (2026-03-30)
- 0.2.7 (2026-03-30)
- 0.2.6 (2026-03-30)
- 0.2.5 (2026-03-30)
- 0.2.4 (2026-03-30)
- 0.2.3 (2026-03-30)
- 0.2.2 (2026-03-24)
- 0.2.1 (2026-03-24)
- 0.2.0 (2026-03-23)
- 0.1.0 (2026-03-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/prebake
- gem 安装: `gem install prebake`
- Bundler: `gem "prebake"`
- 最新版本: 0.3.3
- 最新版归档: https://rubygems.org/downloads/prebake-0.3.3.gem
- 版本锁定: `gem "prebake", "~> 0.3.3"`
- 中央仓库: https://rubygems.org/
