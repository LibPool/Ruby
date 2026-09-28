# ScopedProxy

**Tag**: web

## 简介

== SYNOPSIS:  Allows storing scopes as names; that way you can address subsets of your model space by meaningful names.    require 'scoped_proxy'    # Railsers: You might want to call this in environment.rb   class User &lt; ActiveRecord::Base scoped_proxy :role do |role| { :find =&gt; { :conditions =&gt; ['role = ?', role] } } end scoped_proxy :deleted, :find =&gt; { :conditions =&gt; 'deleted_at is not null' } end  admins = User.role('admin') admins.count              # =&gt; 12 admins.find(:all)         # =&gt; [ ... ]  User.deleted.count        # =&gt; a number  This implementation also brings (NEW, SHINY) default proxies. That means you can have a proxy in effect when no other proxy is in effect.    class User &lt; ActiveRecord::Base default_proxy :find =&gt; { :conditions =&gt; 'deleted_at is null' } end  User.find(:all)   # only finds users that aren't deleted

## 官网

- 主页: http://rubyforge.org/projects/swissrb
- RubyGems: https://rubygems.org/gems/ScopedProxy

## 历史版本号

- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/ScopedProxy
- gem 安装: `gem install ScopedProxy`
- Bundler: `gem "ScopedProxy"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/ScopedProxy-1.0.0.gem
- 版本锁定: `gem "ScopedProxy", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
