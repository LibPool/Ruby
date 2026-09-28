# readorder

**Tag**: cli, filesystem

## 简介

Readorder orders a list of files into a more effective read order.  You would possibly want to use readorder in a case where you know ahead of time that you have a large quantity of files on disc to process.  You can give that list off those files and it will report back to you the order in which you should process them to make most effective use of your disc I/O.  Given a list of filenames, either on the command line or via stdin, readorder will output the filenames in an order that should increase  the I/O throughput when the files corresponding to the filenames are read off of disc.  The output order of the filenames can either be in inode order or physical disc block order.  This is dependent upon operating system support and permission level of the user running readorder.

## 官网

- 主页: http://readorder.rubyforge.org/
- RubyGems: https://rubygems.org/gems/readorder

## 历史版本号

- 2.0.0 (2009-09-24)
- 1.0.0 (2009-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/readorder
- gem 安装: `gem install readorder`
- Bundler: `gem "readorder"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/readorder-2.0.0.gem
- 版本锁定: `gem "readorder", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
