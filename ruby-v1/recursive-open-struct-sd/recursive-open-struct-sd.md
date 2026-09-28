# recursive-open-struct-sd

**Tag**: web, networking

## 简介

RecursiveOpenStruct is a subclass of OpenStruct. It differs from
OpenStruct in that it allows nested hashes to be treated in a recursive
fashion. For example:

    ros = RecursiveOpenStruct.new({ :a =&gt; { :b =&gt; 'c' } })
    ros.a.b # 'c'

Also, nested hashes can still be accessed as hashes:

    ros.a_as_a_hash # { :b =&gt; 'c' }

&gt; This is a fork of the original recursive-open-struct
&gt; to include a fix for https://github.com/aetherknight/recursive-open-struct/issues/46

## 官网

- 主页: http://github.com/aetherknight/recursive-open-struct
- 文档: https://www.rubydoc.info/gems/recursive-open-struct-sd/1.0.2
- RubyGems: https://rubygems.org/gems/recursive-open-struct-sd

## 历史版本号

- 1.0.2 (2016-10-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/recursive-open-struct-sd
- gem 安装: `gem install recursive-open-struct-sd`
- Bundler: `gem "recursive-open-struct-sd"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/recursive-open-struct-sd-1.0.2.gem
- 版本锁定: `gem "recursive-open-struct-sd", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
