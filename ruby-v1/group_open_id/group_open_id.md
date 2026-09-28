# group_open_id

**Tag**: web, cli, networking

## 简介

== DESCRIPTION:  Wrapper library for myID.net's Group ID API  == FEATURES/PROBLEMS:  * TBD  == SYNOPSIS:  require 'group_open_id'  # Initialize a client GroupOpenID::Client.app_key = 'your_application_key' client = GroupOpenID::Client.new('user_open_id_url', 'user_key') group_id = GroupOpenID::URI.new('http://ruby.myid.net', client)  # Get the membership location puts group_id.membership_location # =&gt; 'http://some.url/'  # Get member lists puts group_id.members # =&gt; array of GroupOpenID::Member   # Determine where a given open_id is the member of a group id puts group_id.member?('http://deepblue.myid.net') # =&gt; true

## 官网

- 文档: https://www.rubydoc.info/gems/group_open_id/0.1.2
- RubyGems: https://rubygems.org/gems/group_open_id

## 历史版本号

- 0.1.2 (2009-07-25)
- 0.1.1 (2009-07-25)
- 0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/group_open_id
- gem 安装: `gem install group_open_id`
- Bundler: `gem "group_open_id"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/group_open_id-0.1.2.gem
- 版本锁定: `gem "group_open_id", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
