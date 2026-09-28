# nanoc-cachebuster

**Tag**: web, cli, networking, template, tooling, filesystem

## 简介

Your website should use far-future expires headers on static assets, to make
the best use of client-side caching. But when a file is cached, updates won't
get picked up. Cache busting is the practice of making the filename of a
cached asset unique to its content, so it can be cached without having to
worry about future changes.

This gem adds a filter and some helper methods to Nanoc, the static site
generator, to simplify the process of making asset filenames unique. It helps
you output fingerprinted filenames, and refer to them from your source files.

It works on images, javascripts and stylesheets. It is extracted from the
nanoc-template project at http://github.com/avdgaag/nanoc-template.

## 官网

- 主页: https://github.com/avdgaag/nanoc-cachebuster
- 文档: https://www.rubydoc.info/gems/nanoc-cachebuster/0.4.0
- RubyGems: https://rubygems.org/gems/nanoc-cachebuster

## 历史版本号

- 0.4.0 (2016-07-25)
- 0.3.1 (2012-05-24)
- 0.3.0 (2012-02-26)
- 0.2.0 (2012-02-14)
- 0.1.2 (2011-05-27)
- 0.1.1 (2011-05-24)
- 0.1.0 (2011-05-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/nanoc-cachebuster
- gem 安装: `gem install nanoc-cachebuster`
- Bundler: `gem "nanoc-cachebuster"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/nanoc-cachebuster-0.4.0.gem
- 版本锁定: `gem "nanoc-cachebuster", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
