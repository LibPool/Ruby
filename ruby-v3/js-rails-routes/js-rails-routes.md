# js-rails-routes

**Tag**: web, cli, networking, template, filesystem

## 简介

+js-rails-routes+ is a utility for generating JavaScript equivalents to the +&lt;route&gt;_path+
functions provided by {Ruby on Rails}[https://github.com/rails/rails].  This allows you
to do very similar things in your {+ejs+}[https://rubygems.org/gems/ejs/] JavaScript templates as you would in your +erb+
ruby templates.  You can move html rendering to the client and keep it looking very 
similar to how it would look on the server.

For example, if you have a model +Item+ and a simple route to list all the items, a link
to that items page (using an explicit +a+ anchor tag instead of the Rails +link_to+)
would look the same in either an +erb+ file or an +ejs+ file:

    &lt;a href="&lt;%= items_path() %&gt;"&gt;List all Items&lt;/a&gt;

This gem was originally developed as part of the {MVCoffee}[http://mvcoffee.org] suite of tools, and integrates strongly with the {mvcoffee.js}[https://github.com/kirkbowers/mvcoffee] CoffeeScript MVC framework.

## 官网

- 主页: https://github.com/kirkbowers/js-rails-routes
- 文档: https://www.rubydoc.info/gems/js-rails-routes/1.0.0
- RubyGems: https://rubygems.org/gems/js-rails-routes

## 历史版本号

- 1.0.0 (2015-12-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/js-rails-routes
- gem 安装: `gem install js-rails-routes`
- Bundler: `gem "js-rails-routes"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/js-rails-routes-1.0.0.gem
- 版本锁定: `gem "js-rails-routes", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
