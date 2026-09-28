# n6udp-csvscan

**Tag**: filesystem, data

## 简介

Updated for Ruby 2.X

This is a packaged version of CSVScan, written by MoonWolf. If you can read Japanese, checkout README.ja for whatever he said.

On a 10,000 line file:

    time cat example.csv | ruby fastercsv_benchmark.rb

    real	0m8.804s
    user	0m8.502s
    sys	0m0.304s

    time cat example.csv | ruby csvscan_benchmark.rb 

    real	0m0.860s
    user	0m0.782s
    sys	0m0.088s

## 官网

- 主页: http://github.com/sandofsky/csvscan
- 文档: https://www.rubydoc.info/gems/n6udp-csvscan/0.1.1
- RubyGems: https://rubygems.org/gems/n6udp-csvscan

## 历史版本号

- 0.1.1 (2021-01-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/n6udp-csvscan
- gem 安装: `gem install n6udp-csvscan`
- Bundler: `gem "n6udp-csvscan"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/n6udp-csvscan-0.1.1.gem
- 版本锁定: `gem "n6udp-csvscan", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
