# mussegam-csvscan

**Tag**: filesystem, data

## 简介

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

- 主页: http://github.com/mussegam/csvscan
- RubyGems: https://rubygems.org/gems/mussegam-csvscan

## 历史版本号

- 0.1.0 (2010-01-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/mussegam-csvscan
- gem 安装: `gem install mussegam-csvscan`
- Bundler: `gem "mussegam-csvscan"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/mussegam-csvscan-0.1.0.gem
- 版本锁定: `gem "mussegam-csvscan", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
