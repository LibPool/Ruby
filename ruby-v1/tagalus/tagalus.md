# tagalus

**Tag**: web, serialization, tooling

## 简介

This module encapsulates the API for tagal.us, a site which helps users define tags on twitter or other websites. The basic elements are tags, definitions, and comments - and these 3 objects can be written and read to/from tagal.us using this gem.  There's just 6 useful methods - 3 that read, and 3 that write.  This module uses the Carboni.ca XML base, which means you can set which XML parser it will use - simply use Tagalus.parser = :nokogiri # can be :nokogiri, :hpricot, :rexml, or :libxml to change the parser.

## 官网

- 主页: http://www.carboni.ca/projects/tagalus/
- RubyGems: https://rubygems.org/gems/tagalus

## 历史版本号

- 0.5.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/tagalus
- gem 安装: `gem install tagalus`
- Bundler: `gem "tagalus"`
- 最新版本: 0.5.0
- 最新版归档: https://rubygems.org/downloads/tagalus-0.5.0.gem
- 版本锁定: `gem "tagalus", "~> 0.5.0"`
- 中央仓库: https://rubygems.org/
