# javascript_safe_logger

**Tag**: web, cli, networking, template, tooling, filesystem

## 简介

== Rails 3.1 and up javascript asset for Paul Irish console.log wrapper

This gem makes a javascript log method available as a Rails 3.1 asset

* see http://paulirish.com/2009/log-a-lightweight-wrapper-for-consolelog
* see https://github.com/paulirish/html5-boilerplate

== Usage

in your javascript

    log('inside coolFunc', this, arguments);
    // or simple
    log('hello world!');

and in coffeescript

    log 'inside coolFunc', this, arguments
    # or simple
    log 'hello world!'


== Install

1. Update the Gemfile in your rails project, add the following line

    gem 'javascript_safe_logger'

2. Update the /app/assets/javascript/application.js file

    A. Manually update the file, add this before other requires

        //= require safe_logger

    B. Or use the generator to update the application.js file

        rails generate javascript_safe_logger

== License

Paul Irish released the javascript code with the {The Unlicense}[http://unlicense.org/] (aka: public domain),
so this gem is also released with the same license.


== Ruby Gems

* https://rubygems.org/gems/javascript_safe_logger

## 官网

- 主页: https://github.com/house9/javascript_safe_logger
- 文档: https://www.rubydoc.info/gems/javascript_safe_logger/0.1.0
- RubyGems: https://rubygems.org/gems/javascript_safe_logger

## 历史版本号

- 0.1.0 (2013-05-31)
- 0.0.4 (2012-02-07)
- 0.0.3 (2011-06-25)
- 0.0.2 (2011-06-25)
- 0.0.1 (2011-06-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/javascript_safe_logger
- gem 安装: `gem install javascript_safe_logger`
- Bundler: `gem "javascript_safe_logger"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/javascript_safe_logger-0.1.0.gem
- 版本锁定: `gem "javascript_safe_logger", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
