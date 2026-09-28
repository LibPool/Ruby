# boxey

**Tag**: testing, filesystem

## 简介

Boxey provides the [] element reference operator to ActiveRecord classes.

# Installation

Add this line to your Gemfile:

`gem 'boxey'`

# Configuration

With the boxey gem installed, all ActiveRecord classes gain the [] method, which fetches by the class's primary_key by default.

You may specify additional fields, presumably fields that validate uniqueness, by calling the boxey method.

    class User < ActiveRecord::Base
      boxey :id, :login, :email
      validates :login, uniqueness: true
      validates :email, uniqueness: true
    end

# Use

Given the configuration above:

`User[1]` returns the first User with an id (or login or email) of `1`.

`User['me@example.com']` returns the first User with an email (or id or login) of `'me@example.com'`.

`[]` returns `nil` if no match is found.

## 官网

- 主页: http://github.com/roguevalley/boxey
- 源码仓库: https://github.com/roguevalley/boxey
- RubyGems: https://rubygems.org/gems/boxey

## 历史版本号

- 1.0 (2012-11-19)
- 0.0.5 (2012-10-19)
- 0.0.3 (2012-10-12)
- 0.0.2 (2012-10-12)
- 0.0.1 (2012-10-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/boxey
- gem 安装: `gem install boxey`
- Bundler: `gem "boxey"`
- 最新版本: 1.0
- 最新版归档: https://rubygems.org/downloads/boxey-1.0.gem
- 版本锁定: `gem "boxey", "~> 1.0"`
- 中央仓库: https://rubygems.org/
