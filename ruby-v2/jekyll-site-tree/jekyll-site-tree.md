# jekyll-site-tree

**Tag**: web, serialization, template, tooling, filesystem

## 简介

A jekyll generator which creates a site-tree consisting of all the files in the output (built) path of a jekyll website.

For a site with a structure like:
  - /foo.md
  - /bar.html
  - /posts/2019/15/10/hello-world.md
  - /posts/2019/15/10/lo-and-behold.md
  - /assets/styles/main.scss

You'll recieve an XML unordered list like:
  - foo
  - bar
  - posts/2019/15/10
    - hello-world
    - lo-and-behold
  - assets/styles
    - main

## 官网

- 文档: https://www.rubydoc.info/gems/jekyll-site-tree/0.0.1
- RubyGems: https://rubygems.org/gems/jekyll-site-tree

## 历史版本号

- 0.0.1 (2019-11-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/jekyll-site-tree
- gem 安装: `gem install jekyll-site-tree`
- Bundler: `gem "jekyll-site-tree"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/jekyll-site-tree-0.0.1.gem
- 版本锁定: `gem "jekyll-site-tree", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
