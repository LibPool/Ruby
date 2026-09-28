# divshare

**Tag**: web, cli, filesystem

## 简介

divshare
========

Description
-----------

The divshare gem makes it easier to use the Divshare API. To use it, you need
to create a Divshare account and sign up for an API key.

Usage
-----

Here's a brief walkthrough of the basic operations (see `examples/` for more information):

    require 'divshare'

    # Set these for your divshare account
    api_key    = 'your api key'
    api_secret = 'your api secret'
    email      = 'your login email address'
    password   = 'your password'
    filename   = 'a file you want to upload'

    client = Divshare::Client.new(api_key, api_secret)
    client.login(email, password)
    all_my_files = client.get_user_files
    all_my_files.each do |f| 
      print "#{f.file_name} (#{f.file_size}) "
      puts "was last downloaded #{Time.at(f.last_downloaded_at.to_i)}"
    end
    ticket = client.get_upload_ticket
    uploaded_id = client.upload(ticket, filename)
    puts "#{filename} uploaded with new id: #{uploaded_id}"
    client.logout

Now, going through the same script step-by-step. Use your Divshare API
key and secret (comes with key) to create a client:

    client = Divshare::Client.new(api_key, api_secret)

Login using the credentials for your Divshare account:

    client.login(email, password)

Get an array of all of your files:

    all_my_files = client.get_user_files

Do something with the files:

    all_my_files.each do |f| 
      print "#{f.file_name} (#{f.file_size}) "
      puts "was last downloaded #{Time.at(f.last_downloaded_at.to_i)}"
    end

Upload a file, and capture its id:

    ticket = client.get_upload_ticket
    uploaded_id = client.upload(ticket, filename)

Logout

    client.logout

Installation
------------

Install using rubygems:

    sudo gem install divshare 

Or clone from github

    git clone git://github.com/wasnotrice/divshare.git

## 官网

- 主页: http://github.com/wasnotrice/divshare
- RubyGems: https://rubygems.org/gems/divshare

## 历史版本号

- 0.3.1 (2009-11-19)
- 0.3.0 (2009-11-10)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/divshare
- gem 安装: `gem install divshare`
- Bundler: `gem "divshare"`
- 最新版本: 0.3.1
- 最新版归档: https://rubygems.org/downloads/divshare-0.3.1.gem
- 版本锁定: `gem "divshare", "~> 0.3.1"`
- 中央仓库: https://rubygems.org/
