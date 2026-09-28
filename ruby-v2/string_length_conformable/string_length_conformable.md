# string_length_conformable

**Tag**: web, database, data

## 简介

This gem resolves basically two problems.
  

  ---
  

  1. MySQL for strings(VARCHAR(255)) by default has limit 255 characters. And when developer left this attribute without any length validation, then it's possible to face with situation when user unintentionally or intentionally will pass in text field more characters. So, then, probably you will get 500...
  

  ---
  

  2. PostgreSQL. The maximum number of characters for variable unlimited length types (text, varchar) is undefined. There is a limit of size in bytes for all string types: In any case, the longest possible character string that can be stored is about 1 GB.
  And when developer left this attribute without any length validation, then it's possible to face with situation when user unintentionally or intentionally will try to full up your database with lots of GB of 'important' info.
  

  ---
  

  Both of this cases, I guess, are not very pleasant.
  


  This gem adds default length validation for all string attributes.
  Except those which are already vlidated in standart rails way.

## 官网

- 主页: https://github.com/Yaponcik/string_length_conformable
- 文档: https://www.rubydoc.info/gems/string_length_conformable/0.2.3
- RubyGems: https://rubygems.org/gems/string_length_conformable

## 历史版本号

- 0.2.3 (2018-10-25)
- 0.2.2 (2018-10-22)
- 0.2.1 (2018-10-22)
- 0.1.0 (2018-10-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/string_length_conformable
- gem 安装: `gem install string_length_conformable`
- Bundler: `gem "string_length_conformable"`
- 最新版本: 0.2.3
- 最新版归档: https://rubygems.org/downloads/string_length_conformable-0.2.3.gem
- 版本锁定: `gem "string_length_conformable", "~> 0.2.3"`
- 中央仓库: https://rubygems.org/
