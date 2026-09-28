# hakto

**Tag**: web, testing, security, networking, filesystem

## 简介

Hakto Safe SDBM Wrapper
=======================

## Introduction

Hakto Safe SDBM Wrapper is a safe wrapper of SDBM library. Hakto has compatibility of instance method's interface that is in SDBM class.

Hakto enables to tighten up a code that uses SDBM library like following codes.

**before**

    class Klass
      def initialize(db_path)
        @db_path = db_path
      end
      
      def method1
        SDBM.open(@db_path) do |dbm|
          dbm["hoge"] = "HOGE"
        end
      end
      
      def method2
        SDBM.open(@db_path) do |dbm|
          dbm["hoge"]
        end
      end
      
      :
      
    end            

**after**

    class Klass
      def initialize(db_path)
        @sdb = Hakto::SafeSDBM.new(db_path)
      end
      
      def method1
        sdb["hoge"] = "HOGE"
      end
      
      def method2
        sdb["hoge"]
      end
      
      :
      
    end            



## Operation Environment

We checked good operation within following environment.

- Linux（openSUSE 12.2）・Mac OS X 10.8.2
- Ruby 1.9.3

## Architectonics

- **bin**
- **doc** :: Rdoc documents.
- **lib**
  - **hakto**
    - **safe_sdbm.rb** :: Class of SafeSDBM
- **LICENSE**
- **Rakefile** :: Rakefile that is used to generate gem file
- **README.md**
- **README_jp.md**
- **test** :: Unit tests
  - **tb_safe_sdbm.rb** :: Unit test for SafeSDBM
  
## Install

Download hakto-x.y.z.gem, then execute following command to install Hakto.

`$ sudo gem install hakto-x.y.z.gem`

On the other hand, you can install from RubyGems.org to use following command.

`$ sudo gem install hakto`

Also you can install Hakto without gem. Allocate the safe_sdbm.rb where is ruby interpreter can load Hakto.

## Sample code

See tb_safe_sdbm.rb file. It is an unit test code, and it doubles with sample code.

## API document

See following website: [http://quellencode.org/hakto-doc/](http://quellencode.org/hakto-doc/ "")

## About Author

Moza USANE  
[http://blog.quellencode.org/](http://blog.quellencode.org/ "")  
mozamimy@quellencode.org

## 官网

- 主页: http://blog.quellencode.org/
- 源码仓库: https://github.com/mozamimy/hakto
- 文档: http://quellencode.org/hakto-doc/
- RubyGems: https://rubygems.org/gems/hakto

## 历史版本号

- 0.1.0 (2012-12-08)
- 0.0.1 (2012-12-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/hakto
- gem 安装: `gem install hakto`
- Bundler: `gem "hakto"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/hakto-0.1.0.gem
- 版本锁定: `gem "hakto", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
