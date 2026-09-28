# iana_converter

**Tag**: web, database, data

## 简介

This gem is designed to provide a modular, complete, open-source, crowd-sourced mapping of the 650+ IANA/OLSON timezones of the world into Rails' 146 'important' timezones.
  A search for an existing solution showed that this has been an issue since the inception of ActiveSupport::Timezone as far back as 2012. Approaches which have been suggested included such ideas as: Making your own RTree in a spatially aware database and searching on boundaries, just don't use those timezones (yeah, that makes sense), rely on your users to set their own timezone (doesn't help if you do automated onboarding), find a better sourcing API for timezones based on GeoLookup (they almost all use OLSON/IANA).
  Rather than doing any of those things, it made more sense to simply complete the mapping that ActiveSupport::Timezone started on and then seemingly abandoned.

## 官网

- 主页: https://github.com/jkarnesPerfectCube/iana_converter
- RubyGems: https://rubygems.org/gems/iana_converter

## 历史版本号

- 0.0.4 (2018-09-17)
- 0.0.3 (2018-09-15)
- 0.0.2 (2018-09-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/iana_converter
- gem 安装: `gem install iana_converter`
- Bundler: `gem "iana_converter"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/iana_converter-0.0.4.gem
- 版本锁定: `gem "iana_converter", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
