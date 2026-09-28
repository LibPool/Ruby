# swerling-synfeld

**Tag**: web, testing, serialization, networking, template, filesystem

## 简介

Synfeld is a web application framework that does practically nothing.  Synfeld is little more than a small wrapper for Rack::Mount (see http://github.com/josh/rack-mount). If you want a web framework that is mostly just going to serve up json blobs, and occasionally serve up some simple content (eg. help files) and media, Synfeld makes that easy.   The sample app below shows pretty much everything there is to know about synfeld, in particular:  * How to define routes. * Simple rendering of erb, haml, html, json, and static files. * In the case of erb and haml, passing variables into the template is demonstrated. * A dynamic action where the status code, headers, and body are created 'manually' (/my/special/route below) * A simple way of creating format sensitive routes (/alphabet.html vs. /alphabet.json) * The erb demo link also demos the rendering of a partial (not visible in the code below, you have to look at the template file examples/public/erb_files/erb_test.erb).

## 官网

- 主页: http://tab-a.slot-z.net
- 文档: https://www.rubydoc.info/gems/swerling-synfeld/0.0.4
- RubyGems: https://rubygems.org/gems/swerling-synfeld

## 历史版本号

- 0.0.1 (2014-08-10)
- 0.0.2 (2014-08-10)
- 0.0.4 (2014-08-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/swerling-synfeld
- gem 安装: `gem install swerling-synfeld`
- Bundler: `gem "swerling-synfeld"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/swerling-synfeld-0.0.4.gem
- 版本锁定: `gem "swerling-synfeld", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
