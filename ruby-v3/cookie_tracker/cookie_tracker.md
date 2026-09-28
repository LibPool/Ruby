# cookie_tracker

**Tag**: web, cli, networking, template

## 简介

The cookie_tracker easily synchronizes settings stored in cookies with instance variables of the same name available for use in controllers and views. This gem allows you to
    declare a hash of parameters along with default values that you wish to be loaded/stored in the user's cookies during each page load. Each parameter will be loaded into it's own instance 
    variable of the same name for easy access in controllers and views. If the parameter is passed in the params[] hash, the new value will automatically be stored in the correct cookie and 
    replace the old or default value. This makes it easy to track various options that a user can select on a page, such as items per page, search queries, and custom display settings. 
    If a user clicks off to another page on your site, their settings will be remembered when they return. You can declare the default cookie lifetime options in an initializer
    or override them at runtime. If you prefer to use the session store over the cookie jar, there is a method for that as well. You can override the default cookie options by creating an
    initializer. Visit the github page https://github.com/DanKnox/CookieTracker

## 官网

- 主页: https://github.com/DanKnox/CookieTracker
- 源码仓库: https://github.com/DanKnox/CookieTracker/
- 文档: http://rubydoc.info/github/DanKnox/CookieTracker/master/frames
- 问题追踪: https://github.com/DanKnox/CookieTracker/issues
- RubyGems: https://rubygems.org/gems/cookie_tracker

## 历史版本号

- 1.2.0 (2011-12-18)
- 1.0.0 (2011-12-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/cookie_tracker
- gem 安装: `gem install cookie_tracker`
- Bundler: `gem "cookie_tracker"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/cookie_tracker-1.2.0.gem
- 版本锁定: `gem "cookie_tracker", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
