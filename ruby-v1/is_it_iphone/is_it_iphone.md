# is_it_iphone

**Tag**: web, testing, networking, template

## 简介

The code to check for the iPhone user agent is from http://developer.apple.com.  This doesn't have any dependencies.  - in app/controllers/application.rb  require 'is_it_iphone' class ApplicationController &lt; ActionController::Base include IsItIPhone before_filter :adjust_format_for_iphone # Always show iPhone views end  You will have these functions:    iphone_user_agent? Returns true if the user agent is an iPhone. (as spec'ed on http://developer.apple.com)  iphone_request? Returns true if the request came from an iPhone. Override being an iPhone with ?format=xxxx in the URL.  adjust_format_for_iphone Call when you want to show iPhone views to iPhone users. Note: It is recommended by Apple that you default to showing your &quot;normal&quot; html page to iPhone users and allow them to choose if they want an iPhone version.  With Rails 2.0, you can use its multiview capabilities by simply adding this to your app:  - in config/initializers/mime_types.rb  Mime::Type.register_alias &quot;text/html&quot;, :iphone  Then, just create your views using suffices of iphone.erb instead of html.erb:  index.iphone.erb show.iphone.erb etc.  Note: you will probably want to use a Web library specific for iPhone applications.  FWIW, I use Da shcode (in the iPhone SDK) to write and debug the iPhone application and then integrate it with my  Rails project.

## 官网

- 主页: http://isitiphone.rubyforge.org
- RubyGems: https://rubygems.org/gems/is_it_iphone

## 历史版本号

- 1.0.0 (2009-07-25)
- 0.1.1 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/is_it_iphone
- gem 安装: `gem install is_it_iphone`
- Bundler: `gem "is_it_iphone"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/is_it_iphone-1.0.0.gem
- 版本锁定: `gem "is_it_iphone", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
