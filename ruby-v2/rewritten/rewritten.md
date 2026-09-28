# rewritten

**Tag**: web, database, template, filesystem, data

## 简介

Rewritten is a lookup-based rewriting engine that rewrites requested
    URLs on the fly. The URL manipulations depend on translations found in
    a redis database.

    If a matching translation is found, the result of a request is either a
    redirection or a modification of path and request parameters. For URLs
    without translation entries the request is left unmodified.

    Rewritten takes larges parts from the Resque codebase (which rocks). The
    gem is compromised of four parts:

    1. A Ruby library for creating, modifying and querying translations
    2. A Sinatra app for displaying and managing translations
    3. A Rack app for rewriting and redirecting request (Rack::Rewritten::Url)
    4. A Rack app for substituting URLs in HTML pages with their current translation (Rack::Rewritten::Html)
    5. A Rack app for recording successful request (Rack::Rewritten::Record)

## 官网

- 源码仓库: https://github.com/learnjin/rewritten
- 文档: https://www.rubydoc.info/gems/rewritten/0.16.5
- RubyGems: https://rubygems.org/gems/rewritten

## 历史版本号

- 0.16.5 (2016-03-17)
- 0.16.4 (2016-03-16)
- 0.16.3 (2016-03-16)
- 0.16.2 (2016-03-16)
- 0.16.1 (2015-12-14)
- 0.16.0 (2015-07-31)
- 0.15.2 (2015-06-10)
- 0.15.1 (2015-02-03)
- 0.15.0 (2014-09-18)
- 0.14.2 (2014-08-18)
- 0.14.1 (2014-08-18)
- 0.14.0 (2014-08-18)
- 0.13.1 (2014-08-15)
- 0.13.0 (2014-08-15)
- 0.12.1 (2013-11-19)
- 0.12.0 (2013-11-19)
- 0.11.1 (2013-10-21)
- 0.11.0 (2013-10-18)
- 0.10.0 (2013-06-12)
- 0.9.1 (2013-06-11)
- 0.9.0 (2013-05-15)
- 0.8.2 (2013-05-15)
- 0.8.1 (2013-05-13)
- 0.8.0 (2013-05-13)
- 0.7.0 (2013-05-13)
- 0.6.0 (2013-05-13)
- 0.5.0 (2013-05-12)
- 0.4.0 (2013-05-03)
- 0.3.3 (2013-02-03)
- 0.3.2 (2013-01-24)
- 0.3.1 (2011-12-27)
- 0.3.0 (2011-12-21)
- 0.2.2 (2011-09-27)
- 0.2.1 (2011-09-23)
- 0.2.0 (2011-09-23)
- 0.1.0 (2011-09-12)
- 0.0.4 (2011-09-10)
- 0.0.3 (2011-09-09)
- 0.0.2 (2011-09-06)
- 0.0.1 (2011-08-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/rewritten
- gem 安装: `gem install rewritten`
- Bundler: `gem "rewritten"`
- 最新版本: 0.16.5
- 最新版归档: https://rubygems.org/downloads/rewritten-0.16.5.gem
- 版本锁定: `gem "rewritten", "~> 0.16.5"`
- 中央仓库: https://rubygems.org/
