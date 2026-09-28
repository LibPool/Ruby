# ip_library

**Tag**: filesystem

## 简介

IPLibrary
=========

顾名思义，这是一个ip库

Example
=======

本gem中已经带有ip库，默认是gem目录下doc/ip_libraries.txt
默认ip库的格式以IPLibrary::Configuration.separator分组
各组第一行为ip头（192.168.1.1的ip头为192）,其他行各列以英文逗号隔开
各列分别是：起始ip, 结束ip, 省份, 城市, 县区, 行政划分最小字段的拼音(如果有县区则为县区的拼音)

当然，您也可以有自己的ip库
设置ip库的path: IPLibrary::Configuration.file_path = '/home/doc/ip_libraries.txt'
而且，您也可以设置ip库中的列的含义，start_ip、end_ip两列必须有，且必须依次为1、2列
设置其他列：IPLibrary::Configuration.optional_columns = [:province, :city, :district, :pinyin]
除了1、2列，其他列一次为province、city、district、pinyin
然后会动态生成方法：
IPLibrary::Base#ip2province
IPLibrary::Base#ip2city
IPLibrary::Base#ip2district
IPLibrary::Base#ip2pinyin

=============================================

IPLibrary::Base 的方法有：

IPLibrary::Base.ip2province('123.132.254.134')
IPLibrary::Base.ip2province(2072313478)
#=> "山东"

IPLibrary::Base.ip2city('123.132.254.134')
IPLibrary::Base.ip2city(2072313478)
#=> "临沂"

IPLibrary::Base.ip2district('123.132.254.134')
IPLibrary::Base.ip2district(2072313478)
# => ""

IPLibrary::Base.ip2pinyin('123.132.254.134')
IPLibrary::Base.ip2pinyin(2072313478)
#=> "linyi"

## 官网

- 主页: https://github.com/tumayun/ip_library
- RubyGems: https://rubygems.org/gems/ip_library

## 历史版本号

- 0.0.1 (2012-07-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/ip_library
- gem 安装: `gem install ip_library`
- Bundler: `gem "ip_library"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/ip_library-0.0.1.gem
- 版本锁定: `gem "ip_library", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
