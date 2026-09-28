# bjornblomqvist-input_chronic

**Tag**: web, networking

## 简介

= input_chronic  A simple Rack middleware that parses a dates using Chronic, and  returns the result in a standardized manner. The idea is to use  this to verify the input in date input fields using AJAX, to  provide immediate feedback to the user.  == Usage  Include "input_chronic" in your middleware stack. In Rails, this is done in environment.rb  config.gem 'bjornblomqvist-input_chronic', :lib =&gt; 'input_chronic', :source =&gt; 'http://gems.github.com' config.middleware.use "input_chronic"  This will catch requests to /gems.github.com/bjornblomqvist/input_chronic. Use GET requests and provide a parameter 'date' or 'datetime'. The value will be  parsed by Chronic and returned formatted as 2009-01-01 or 2009-01-01 12:45, depending on the parameter name.  Don't forget to add the javascript found at  /javascript/input_chronic.js  This is also implemented by catching the request before it reaches rails.  To use this on a text input add the class chronic_date or chronic_datetime  &lt;input type="text" class="chronic_datetime" /&gt;  == Copyright  Copyright (c) 2009 Erik Hansson, Bjorn Blomqvist. See LICENSE for details.

## 官网

- 主页: http://github.com/bjornblomqvist/input_chronic
- 文档: https://www.rubydoc.info/gems/bjornblomqvist-input_chronic/1.0.5
- RubyGems: https://rubygems.org/gems/bjornblomqvist-input_chronic

## 历史版本号

- 1.0.0 (2014-08-11)
- 1.0.3 (2014-08-11)
- 1.0.5 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/bjornblomqvist-input_chronic
- gem 安装: `gem install bjornblomqvist-input_chronic`
- Bundler: `gem "bjornblomqvist-input_chronic"`
- 最新版本: 1.0.5
- 最新版归档: https://rubygems.org/downloads/bjornblomqvist-input_chronic-1.0.5.gem
- 版本锁定: `gem "bjornblomqvist-input_chronic", "~> 1.0.5"`
- 中央仓库: https://rubygems.org/
