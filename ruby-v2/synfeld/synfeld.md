# synfeld

**Tag**: web, testing, serialization, networking, template, filesystem

## 简介

Synfeld is a web application framework that does practically nothing.

Synfeld is little more than a small wrapper for Rack::Mount (see
http://github.com/josh/rack-mount).  If you want a web framework that is
mostly just going to serve up json blobs, and occasionally serve up some
simple content (eg. help files) and media, Synfeld makes that easy.

The sample app below shows pretty much everything there is to know about
synfeld, in particular:

* How to define routes.
* Simple rendering of erb, haml, html, json, and static files.
* In the case of erb and haml, passing variables into the template is
demonstrated.
* A dynamic action where the status code, headers, and body are created
'manually' (/my/special/route below)
* A simple way of creating format sensitive routes (/alphabet.html vs.
/alphabet.json)
* The erb demo link also demos the rendering of a partial (not visible in the
code below, you have to look at the template file
  examples/public/erb_files/erb_test.erb).

## 官网

- 主页: http://github.com/swerling/synfeld
- RubyGems: https://rubygems.org/gems/synfeld

## 历史版本号

- 0.0.7 (2015-02-05)
- 0.0.6 (2012-09-06)
- 0.0.5 (2012-06-26)
- 0.0.4 (2009-10-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/synfeld
- gem 安装: `gem install synfeld`
- Bundler: `gem "synfeld"`
- 最新版本: 0.0.7
- 最新版归档: https://rubygems.org/downloads/synfeld-0.0.7.gem
- 版本锁定: `gem "synfeld", "~> 0.0.7"`
- 中央仓库: https://rubygems.org/
