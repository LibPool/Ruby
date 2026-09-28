# medusa-crawler

**Tag**: web, database, testing, networking

## 简介

== Medusa: a ruby crawler framework {rdoc-image:https://badge.fury.io/rb/medusa-crawler.svg}[https://rubygems.org/gems/medusa-crawler] rdoc-image:https://github.com/brutuscat/medusa-crawler/workflows/Ruby/badge.svg?event=push

Medusa is a framework for the ruby language to crawl and collect useful information about the pages
it visits. It is versatile, allowing you to write your own specialized tasks quickly and easily.

=== Features

* Choose the links to follow on each page with +focus_crawl+
* Multi-threaded design for high performance
* Tracks +301+ HTTP redirects
* Allows exclusion of URLs based on regular expressions
* Records response time for each page
* Obey _robots.txt_ directives (optional, but recommended)
* In-memory or persistent storage of pages during crawl, provided by Moneta[https://github.com/moneta-rb/moneta]
* Inherits OpenURI behavior (redirects, automatic charset and encoding detection, proxy configuration options).

<b>Do you have an idea or a suggestion? {Open an issue and talk about it}[https://github.com/brutuscat/medusa-crawler/issues/new]</b>

=== Examples

Medusa is versatile and to be used programatically, you can start with one or multiple URIs:

    require 'medusa'

    Medusa.crawl('https://www.example.com', depth_limit: 2)

Or you can pass a block and it will yield the crawler back, to manage configuration or drive its crawling focus:

    require 'medusa'

    Medusa.crawl('https://www.example.com', depth_limit: 2) do |crawler|
      crawler.discard_page_bodies = some_flag

      # Persist all the pages state across crawl-runs.
      crawler.clear_on_startup = false
      crawler.storage = Medusa::Storage.Moneta(:Redis, 'redis://redis.host.name:6379/0')

      crawler.skip_links_like(/private/)

      crawler.on_pages_like(/public/) do |page|
        logger.debug "[public page]  #{page.url} took #{page.response_time} found #{page.links.count}"
      end

      # Use an arbitrary logic, page by page, to continue customize the crawling.
      crawler.focus_crawl(/public/) do |page|
        page.links.first
      end
    end

## 官网

- 主页: https://github.com/brutuscat/medusa-crawler
- 源码仓库: https://github.com/brutuscat/medusa-crawler/tree/v1.0.0
- 问题追踪: https://github.com/brutuscat/medusa-crawler/issues
- RubyGems: https://rubygems.org/gems/medusa-crawler

## 历史版本号

- 2.0.0.pre.2 (2026-08-26)
- 1.0.0 (2020-08-17)
- 1.0.0.pre.2 (2020-08-14)
- 1.0.0.pre.1 (2020-08-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/medusa-crawler
- gem 安装: `gem install medusa-crawler`
- Bundler: `gem "medusa-crawler"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/medusa-crawler-1.0.0.gem
- 版本锁定: `gem "medusa-crawler", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
