# srcforge

**Tag**: web, testing, networking

## 简介

This script allows you to easily automate the downloading of the latest version of any sourceforge project (as stored up  to 31/12/2006) from any of sourceforge server by having it parse the web pages for the project and extract the latest release. It supports connecting through a proxy if either the  environment variable HTTP_PROXY or http_proxy is defined. Also, downloads can be resumed like wget, in case the  download is abruptly terminated. If .md5 checksums are available, they will also be downloaded and verified using ruby's digest/md5.

## 官网

- 主页: http://www.rubyforge.org/projects/srcforge/
- RubyGems: https://rubygems.org/gems/srcforge

## 历史版本号

- 1.0.2 (2009-07-25)
- 1.0.1 (2009-07-25)
- 1.0.0 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/srcforge
- gem 安装: `gem install srcforge`
- Bundler: `gem "srcforge"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/srcforge-1.0.2.gem
- 版本锁定: `gem "srcforge", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
