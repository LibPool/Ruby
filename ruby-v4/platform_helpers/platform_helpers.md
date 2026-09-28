# platform_helpers

**Tag**: testing

## 简介

Override's some Ruby classes to add methods making for uniform calls.  For example, :to_bool is common to Nil, nil, TrueClass, FalseClass, String, Float, Date, ActiveRecord::Associations::HasOneAssociation and ActiveRecord::Associations::HasManyAssociation.  

There are a few compatibility features bridging the gaps between ruby1.8 and ruby1.9 as well.  With the modification of String to Enumerable in ruby1.9, methods have been added so that you can grep and itterate over each line, in all ruby versions.

Code is self explanatory, for other aspects.

## 官网

- 主页: http://cyberconnect.biz/opensource
- RubyGems: https://rubygems.org/gems/platform_helpers

## 历史版本号

- 0.1.3 (2011-10-24)
- 0.1.2 (2011-10-02)
- 0.1.0 (2011-08-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/platform_helpers
- gem 安装: `gem install platform_helpers`
- Bundler: `gem "platform_helpers"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/platform_helpers-0.1.3.gem
- 版本锁定: `gem "platform_helpers", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
