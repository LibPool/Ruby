# jekyll-plugin-include

**Tag**: template, filesystem

## 简介

A Jekyll liquid tag plugin which allows includes directly from plugins' `_include` directories, with optional ability to override with files present in site includes_dir (if they exist).

Normally, Jekyll's `include` tag can only search for files in the site's single configured includes directory (and that of the *theme* plugin, if it using one). That means that if a plugin wants to provide you with a template/fragment via includes, the best it can do is ask you to copy it into your own repo manually.

This plugin then makes it easy to use includes that ship *with* a plugin directly *from* a plugin. And if a modified version of the file is provided in the site's own includes directory, it can intelligently use that one instead!

And for plugin developers, this provides a way to ship and use includes without leaning on the user to manage the unmodified files themselves.

## 官网

- 主页: https://github.com/decipher-media/jekyll-plugin-include
- 文档: https://www.rubydoc.info/gems/jekyll-plugin-include/0.1.1
- RubyGems: https://rubygems.org/gems/jekyll-plugin-include

## 历史版本号

- 0.1.1 (2018-09-24)
- 0.1.0 (2018-09-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/jekyll-plugin-include
- gem 安装: `gem install jekyll-plugin-include`
- Bundler: `gem "jekyll-plugin-include"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/jekyll-plugin-include-0.1.1.gem
- 版本锁定: `gem "jekyll-plugin-include", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
