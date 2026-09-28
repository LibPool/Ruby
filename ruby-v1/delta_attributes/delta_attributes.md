# delta_attributes

**Tag**: web, database, testing, networking

## 简介

This gem makes updating specified number fields by ActiveRecord in unusual way.

    Instead of generating sql script to update value in usual way like this:

      UPDATE users
      SET money = 10
      WHERE id = 1;

    It replaces it with

      UPDATE users
      SET money = money + delta
      WHERE id = 1;

    where delta is difference between old value and new value of that field.

    This solves problem with simultaneous updating of the same field by different threads
    (problem known as race condition).

    Source code: https://github.com/izbor/delta_attributes

## 官网

- 主页: https://github.com/izbor/delta_attributes
- 文档: https://www.rubydoc.info/gems/delta_attributes/1.0.3
- RubyGems: https://rubygems.org/gems/delta_attributes

## 历史版本号

- 1.0.3 (2013-09-24)
- 1.0.2 (2013-08-30)
- 0.0.4 (2012-11-21)
- 0.0.3 (2012-11-20)
- 0.0.2 (2012-11-20)
- 0.0.1 (2012-11-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/delta_attributes
- gem 安装: `gem install delta_attributes`
- Bundler: `gem "delta_attributes"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/delta_attributes-1.0.3.gem
- 版本锁定: `gem "delta_attributes", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
