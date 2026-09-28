# hash_set_operators

**Tag**: library

## 简介

== DESCRIPTION:  * Adds +, -, and &amp; methods to Hashes  == SYNOPSIS:  require 'rubygems' require 'hash_set_operators'  {:controller =&gt; :user, :action =&gt; :edit} + {:action =&gt; :show, :id =&gt; 1} # =&gt; {:controller =&gt; :user, :action =&gt; :show, :id =&gt; 1}  {:controller =&gt; :user, :action =&gt; :edit} - {:action =&gt; :show, :id =&gt; 1} # =&gt; {:controller =&gt; :user}  {:controller =&gt; :user, :action =&gt; :edit} &amp; {:action =&gt; :show, :id =&gt; 1} # =&gt; {:action =&gt; :edit}  == INSTALL:

## 官网

- 文档: https://www.rubydoc.info/gems/hash_set_operators/0.1.0
- RubyGems: https://rubygems.org/gems/hash_set_operators

## 历史版本号

- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/hash_set_operators
- gem 安装: `gem install hash_set_operators`
- Bundler: `gem "hash_set_operators"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/hash_set_operators-0.1.0.gem
- 版本锁定: `gem "hash_set_operators", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
