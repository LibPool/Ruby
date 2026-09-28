# mail-single_file_delivery

**Tag**: web, testing, networking, template, filesystem

## 简介

# Single File Delivery Method for Mail gem

## Summary
This gem is a delivery-method plug-in for [mail](https://github.com/mikel/mail)
that delivers all mail to a single file for testing.

The Mail gem already provides a file delivery-method that appends a copy of each message
to a file named after each message recipient,
but I want them to all go to a single file 
so that I can monitor them from another window with `tail -f my-file`,
or `cat my-named-pipe` while I hand-test the web interface from a browser.

Of course this is _in addition to_ running automated tests with Rspec and Cucumber.
At some point in development, I want to actually see the pages and enter my own inputs
and perhaps display the mail messages in an HTML reader.

## Synopsis

    Mail.defaults do
      delivery_method SingleFileDelivery => '/tmp/my-file.txt'
    end

## 官网

- 主页: https://github.com/lsiden/mail-single_file_delivery
- RubyGems: https://rubygems.org/gems/mail-single_file_delivery

## 历史版本号

- 0.0.1 (2012-01-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/mail-single_file_delivery
- gem 安装: `gem install mail-single_file_delivery`
- Bundler: `gem "mail-single_file_delivery"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/mail-single_file_delivery-0.0.1.gem
- 版本锁定: `gem "mail-single_file_delivery", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
