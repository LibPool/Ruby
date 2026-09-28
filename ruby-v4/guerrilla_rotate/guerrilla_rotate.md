# guerrilla_rotate

**Tag**: web, testing, networking, template, filesystem, data

## 简介

GuerrillaRotate
==============

This plugin lets you have multiple view pages for the one action, so that you
can rotate through different views in order to test which one is the most
effective.  This is known as A/B testing, split testing or side-by-side
testing.

It will automatically switch between the different views for different web
requests (uses .rand so is pseudo random, not round-robin or anything).  The
particular view is sticky for a (rails) session, so that once that view has been
chosen for that visitor they will see the same, consistent view each time.

It integrates automagically into
[Rubaidh::GoogleAnalytics](http://github.com/rubaidh/google_analytics) by
setting the override_trackpageview to the name of the unique view file (instead
of the action-based URL) so you can track it easily in Google Analytics.

Without that you'll want to track it by putting different tracking codes in each
of your view templates.

Example
-------

So, in your views you will create some new templates with something (can be
anything including nothing) between the template name and the first part of the
extension.  So you might have the following files for the products/index action:

    app/views/products/index.html.erb
    app/views/products/index_alt.html.erb
    app/views/products/index_new.html.erb

Then all you need to do is tell your controller to rotate for that action:

### app/controllers/products_controller.rb
    class ProductsController < ApplicationController
      guerrilla_rotate :index, :show

      # etc..

    end

NB: guerrilla_rotate is also aliased as guerilla_rotate for the alternative
spelling and typos.

Copyright &copy; 2009 Jason King, released under the MIT license

## 官网

- 主页: http://github.com/JasonKing/guerrilla_rotate
- RubyGems: https://rubygems.org/gems/guerrilla_rotate

## 历史版本号

- 0.1.0 (2010-02-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/guerrilla_rotate
- gem 安装: `gem install guerrilla_rotate`
- Bundler: `gem "guerrilla_rotate"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/guerrilla_rotate-0.1.0.gem
- 版本锁定: `gem "guerrilla_rotate", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
