# rutema_elements

**Tag**: web, database, testing, serialization, tooling

## 简介

== DESCRIPTION:
Rutema Elements modules are the easiest way to add functionality to rutema parsers.
Just derive your parser from the basic rutema parser and include the module of your choice 

 class MyParser &lt; Rutema::MinimalXMLParser
	include Rutema::Elements::IIS
	include Rutema::Elements::Standard
 end

and voila! your parser now understands how to reset IIS, wait and fail!

== FEATURES/PROBLEMS:
Easy addition of extra functionality for rutema

IIS, MSTest and SQLServer modules are windows specific as they use the MS commandline tools

## 官网

- 文档: https://www.rubydoc.info/gems/rutema_elements/0.1.4
- RubyGems: https://rubygems.org/gems/rutema_elements

## 历史版本号

- 0.1.4 (2009-08-05)
- 0.1.3 (2009-07-25)
- 0.1.2 (2009-07-25)
- 0.1.1 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/rutema_elements
- gem 安装: `gem install rutema_elements`
- Bundler: `gem "rutema_elements"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/rutema_elements-0.1.4.gem
- 版本锁定: `gem "rutema_elements", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
