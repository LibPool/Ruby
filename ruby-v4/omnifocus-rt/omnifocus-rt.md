# omnifocus-rt

**Tag**: web, testing, serialization, networking, template, filesystem

## 简介

Plugin for omnifocus gem to provide rt BTS synchronization.

The first time this runs it creates a yaml file in your home directory
for the rt url, username, password, default queue and query.

The query is optional.  If you don't supply it omnifocus-rt will pull all
tickets from the default queue assigned to the specified user.

The use a custom query you must supply it in the config file.  omnifocus-rt
uses the REST interface to RT.  More information about query formatting is
available here: http://wiki.bestpractical.com/view/REST

Example:
    :rt_url:   rt
    :queue:    QA
    :username: user
    :password: pass
    :query:    "Queue='QA'ANDOwner='Nobody'ANDStatus!='rejected'"

## 官网

- 主页: https://github.com/seattlerb/omnifocus-rt
- 文档: https://www.rubydoc.info/gems/omnifocus-rt/1.0.2
- RubyGems: https://rubygems.org/gems/omnifocus-rt

## 历史版本号

- 1.0.2 (2015-05-11)
- 1.0.1 (2011-08-04)
- 1.0.0 (2009-12-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/omnifocus-rt
- gem 安装: `gem install omnifocus-rt`
- Bundler: `gem "omnifocus-rt"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/omnifocus-rt-1.0.2.gem
- 版本锁定: `gem "omnifocus-rt", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
