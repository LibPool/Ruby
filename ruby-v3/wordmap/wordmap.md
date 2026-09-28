# wordmap

**Tag**: data

## 简介

Wordmap is a simple way to lookup data directly from disk, bypassing RAM. It uses pread (no buffering), and takes advantage of SSD's constant seek time. The data is stored in equal size "cells" making it easy to calculate where things are located based on vectors.

## 官网

- 主页: https://github.com/maxim/wordmap
- 更新日志: https://github.com/maxim/wordmap/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/wordmap

## 历史版本号

- 0.3.0 (2023-08-04)
- 0.2.0 (2020-09-16)
- 0.1.0 (2020-09-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/wordmap
- gem 安装: `gem install wordmap`
- Bundler: `gem "wordmap"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/wordmap-0.3.0.gem
- 版本锁定: `gem "wordmap", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
