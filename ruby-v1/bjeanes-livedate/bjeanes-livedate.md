# bjeanes-livedate

**Tag**: web, testing, tooling

## 简介

= Livedate

A simple Rack middleware that parses a dates using Chronic, and 
returns the result in a standardized manner. The idea is to use 
this to verify the input in date input fields using AJAX, to 
provide immediate feedback to the user.


== Usage

Include Livedate in your middleware stack. In Rails, this
is done in environment.rb

  config.gem 'livedate'
  config.middleware.use "Livedate"

Specify the desired date + datetime formats you want too. Default
error message for strings that Chronic can't pass can also 
be provided. The defaults are:

  config.middleware.use "Livedate", 
    :date_format => '%Y-%m-%d',
    :datetime_format => ''%Y-%m-%d %H:%M',
    :invalid_format => ''

This will catch requests to /parsedate. Use GET requests and
provide a parameter 'date' or 'datetime'. The value will be 
parsed by Chronic and returned formatted as 2009-01-01 or
2009-01-01 12:45, depending on the parameter name.


== Scripts

There are two generators available to get simple javascripts 
that use livedate. Both will replace the contents on input
elements with classes .date or .datetime on change with the
result from the Chronic parse.

  script/generate livedate_jquery
  script/generate livedate_prototype

Will put the appropriate version of the script in your
public/javascripts directory. Feel free to change these
if you need a different behavior.

## 官网

- 主页: http://www.erikhansson.com
- RubyGems: https://rubygems.org/gems/bjeanes-livedate

## 历史版本号

- 1.0.0 (2014-08-11)
- 1.1.0 (2011-05-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/bjeanes-livedate
- gem 安装: `gem install bjeanes-livedate`
- Bundler: `gem "bjeanes-livedate"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/bjeanes-livedate-1.1.0.gem
- 版本锁定: `gem "bjeanes-livedate", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
