# ruby-reddit

**Tag**: library

## 简介

== FEATURES/PROBLEMS:  * Scrapes links from reddit's hot page and new page.  == SYNOPSIS:  require &quot;reddit&quot;  # Get all the links from the &quot;hot&quot; page links = Reddit.read :hot  # Check out the links! for link in links puts link.rank puts link.site_id puts link.url puts link.title puts link.date end  # Get all the links from the first page of the ruby subreddit ruby_links = Reddit.read :ruby  # Get all the links from the second page of the ruby subreddit ruby_links_2 = Reddit.read :ruby, :page =&gt; 1   == REQUIREMENTS:  * hpricot * open-uri * mechanize

## 官网

- 文档: https://www.rubydoc.info/gems/ruby-reddit/0.2.0
- RubyGems: https://rubygems.org/gems/ruby-reddit

## 历史版本号

- 0.2.0 (2009-07-25)
- 0.1.1 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruby-reddit
- gem 安装: `gem install ruby-reddit`
- Bundler: `gem "ruby-reddit"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/ruby-reddit-0.2.0.gem
- 版本锁定: `gem "ruby-reddit", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
