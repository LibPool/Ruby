# e9_crm

**Tag**: web

## 简介

*NOTE his plugin requires the private e9_base CMS gem and WILL NOT WORK without it.*

CRM Plugin for the e9 CMS
=========================

To use, add as a gem and install by running:

    rails g e9_crm:install

Then modify the installed initializer as per your app, including
the controller module in your desired controllers, with the final
result looking something like this:

 \   require 'e9_crm'

    User.send :include, E9Crm::Backend::ActiveRecord

 \   Rails.configuration.after_initialize do
      [
        MyFirstTrackedController,
 \       MySecondTrackedController
      ].each {|c| c.send(:include, E9Crm::TrackingController) }
    end

NOTE: A few assumptions are made:
---------------------------------

1. \   Your app has a "User" model
2.    Your app has a controller method #current_user to return the
      currently logged in user.

## 官网

- 主页: http://www.e9digital.com
- RubyGems: https://rubygems.org/gems/e9_crm

## 历史版本号

- 0.1.34 (2011-10-14)
- 0.1.33 (2011-10-12)
- 0.1.32 (2011-10-12)
- 0.1.31 (2011-10-12)
- 0.1.30 (2011-10-12)
- 0.1.29 (2011-10-11)
- 0.1.28 (2011-10-07)
- 0.1.27 (2011-10-07)
- 0.1.26 (2011-09-29)
- 0.1.25 (2011-09-26)
- 0.1.24 (2011-09-23)
- 0.1.23 (2011-09-23)
- 0.1.22 (2011-09-21)
- 0.1.21 (2011-09-16)
- 0.1.20 (2011-09-15)
- 0.1.19 (2011-09-14)
- 0.1.18 (2011-09-12)
- 0.1.17 (2011-09-09)
- 0.1.16 (2011-09-07)
- 0.1.14 (2011-06-07)
- 0.1.13 (2011-05-31)
- 0.1.12 (2011-05-27)
- 0.1.11 (2011-05-27)
- 0.1.10 (2011-05-26)
- 0.1.8 (2011-05-25)
- 0.1.7 (2011-05-20)
- 0.1.6 (2011-05-19)
- 0.1.5 (2011-05-18)
- 0.1.4 (2011-05-16)
- 0.1.1 (2011-05-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/e9_crm
- gem 安装: `gem install e9_crm`
- Bundler: `gem "e9_crm"`
- 最新版本: 0.1.34
- 最新版归档: https://rubygems.org/downloads/e9_crm-0.1.34.gem
- 版本锁定: `gem "e9_crm", "~> 0.1.34"`
- 中央仓库: https://rubygems.org/
