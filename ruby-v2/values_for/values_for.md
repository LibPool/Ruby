# values_for

**Tag**: database, testing, data

## 简介

values_for makes your ActiveRecord-backed class work with an enumerable type.  Instead of existing 
    ActiveRecord plugins such as enum_fu, which store the enumerable attribute as an integer, values_for 
    stores the content of the enumerable attribute in a varchar column of the database.  The field will
    automatically validate using validates_inclusion_of and accepts all the same options. 

    values_for will also optionally create named scopes, predicate methods, and constants defining the 
    possible values for enumerable types on your model.  By default, however, it avoids polluting your
    model with things you may not need unless these features are specifically requested.

## 官网

- 主页: http://github.com/jsl/values_for
- RubyGems: https://rubygems.org/gems/values_for

## 历史版本号

- 0.1 (2010-10-28)
- 0.0.9 (2010-10-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/values_for
- gem 安装: `gem install values_for`
- Bundler: `gem "values_for"`
- 最新版本: 0.1
- 最新版归档: https://rubygems.org/downloads/values_for-0.1.gem
- 版本锁定: `gem "values_for", "~> 0.1"`
- 中央仓库: https://rubygems.org/
