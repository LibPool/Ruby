# ruby-serial

**Tag**: serialization

## 简介

Library serializing Ruby objects, optimized in many ways:
* Space efficient: Use MessagePack (binary compact storage) and don't serialize twice the same object
* Keep shared objects: if an object is shared by others, serialization still keeps the reference and does not duplicate objects in memory
* Gives the ability to fine tune which attributes of your objects are to be serialized
* Keeps backward compatibility with previously serialized versions.

## 官网

- 主页: http://ruby-serial.sourceforge.net
- 文档: https://www.rubydoc.info/gems/ruby-serial/1.0.3.20130731
- RubyGems: https://rubygems.org/gems/ruby-serial

## 历史版本号

- 1.0.3.20130731 (2013-07-31)
- 1.0.2.20130725 (2013-07-25)
- 1.0.1.20130709 (2013-07-09)
- 1.0.0.20130705 (2013-07-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruby-serial
- gem 安装: `gem install ruby-serial`
- Bundler: `gem "ruby-serial"`
- 最新版本: 1.0.3.20130731
- 最新版归档: https://rubygems.org/downloads/ruby-serial-1.0.3.20130731.gem
- 版本锁定: `gem "ruby-serial", "~> 1.0.3.20130731"`
- 中央仓库: https://rubygems.org/
