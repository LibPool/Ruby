# activerecord-mysql2-retry-ext

**Tag**: web, database

## 简介

Something with the combination of Rails 3.1, Mysql2 0.3.x, Capybara,
    Selenium/Webkit/etc causes Mysql to raise exceptions where the connection is
    waiting on a result. This gem provides an auto-retry capability with the
    Mysql2Adapter to retry any query execution up to 5 times. This is a a temporary
    solution until the real issue with the above libraries/frameworks are resolved. This
    should NOT be used in production.

## 官网

- 主页: https://github.com/zdennis/activerecord-mysql2-retry-ext
- RubyGems: https://rubygems.org/gems/activerecord-mysql2-retry-ext

## 历史版本号

- 0.2.0 (2012-10-05)
- 0.1.0 (2011-09-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/activerecord-mysql2-retry-ext
- gem 安装: `gem install activerecord-mysql2-retry-ext`
- Bundler: `gem "activerecord-mysql2-retry-ext"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/activerecord-mysql2-retry-ext-0.2.0.gem
- 版本锁定: `gem "activerecord-mysql2-retry-ext", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
