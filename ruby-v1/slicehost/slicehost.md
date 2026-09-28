# slicehost

**Tag**: web, testing, networking, devops

## 简介

This library provides a simple set of helper methods to manage slices and DNS zones/records on your Slicehost account (http://slicehost.com).  == Capistrano tasks  There are two capistrano tasks: cap slicehost:zone:add       # Create DNS zone cap slicehost:zone:mx:google # Add Google Apps MX records  To your config/deploy.rb, add the following:  require &quot;slicehost/recipes/capistrano&quot; if Capistrano::Version::MAJOR &gt;= 2 # Used to setup/update DNS registry of url =&gt; ip set :domain_mapping, &quot;myurl.com&quot; =&gt; &quot;123.456.789.012&quot;  == Underlying API  The current API is very alpha. It was just the simplest thing that worked. There are unit tests demonstrating it working and everything.   Future releases will have a nicer, class-based API.   Contact: Dr Nic Williams, drnicwilliams@gmail.com

## 官网

- 主页: http://slicehost.rubyforge.org
- RubyGems: https://rubygems.org/gems/slicehost

## 历史版本号

- 0.2.1 (2009-07-25)
- 0.2.0 (2009-07-25)
- 0.1.1 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/slicehost
- gem 安装: `gem install slicehost`
- Bundler: `gem "slicehost"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/slicehost-0.2.1.gem
- 版本锁定: `gem "slicehost", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
