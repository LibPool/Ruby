# multi_rails

**Tag**: web, testing, networking, template, filesystem

## 简介

#### MultiRails by Relevance, http://thinkrelevance.com Rob Sanheim - MultiRails lead  MultiRails lets you test your Rails plugin or app against many versions of Rails in one sweep.  #### DESCRIPTION:  MultiRails allows easy testing against multiple versions of Rails for your Rails specific gem or plugin.  It also has tentative support testing Rails applications against multiple versions of Rails.  Use MultiRails to hook in Rails 2.0 testing in your continuous integration.  Still working on Rails 2.0 support?  Use MultiRails to see where your test suite falls down against the 2.0 preview releases of Rails.  MultiRails was initially developed by members of Relevance while developing Streamlined against edge Rails.  To see how Streamlined uses MultiRails, go to http://trac.streamlinedframework.org.  #### FEATURES:  * easily test plugins/extensions using a require from your test_helper.rb and a require in your RakeFile * rake tasks to test against a specified version of Rails, the latest version, or all versions * tentative support for testing plain Rails apps against multiple versions of Rails * Uses rubygems for version management of Rails  #### TODOs:  * improve docs on how to override what files are required by multi_rails * maybe add ability to load plain Rails versions -- ie checked out copies not in RubyGems  #### NOTES:  * (__For Rails apps only__) multi_rails will rename your vendor/rails directory to vendor/rails.off if it finds one within your rails app.  We have to do this to make Rails fall back to RubyGems rails.  Multi_rails will rename back to the correct vendor/rails when done testing, so it will not interrupt your app in normal use. * (__For Rails apps only__) multi_rails needs to add a line to top of your environment.rb to hook into -- see the instructions below for more details

## 官网

- 主页: http://multi-rails.rubyforge.org/
- RubyGems: https://rubygems.org/gems/multi_rails

## 历史版本号

- 0.0.4 (2009-07-25)
- 0.0.3 (2009-07-25)
- 0.0.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/multi_rails
- gem 安装: `gem install multi_rails`
- Bundler: `gem "multi_rails"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/multi_rails-0.0.4.gem
- 版本锁定: `gem "multi_rails", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
