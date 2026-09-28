# Stencil

**Tag**: web, template, filesystem, data

## 简介

Stencil is a templating library with a number of design goals.

  *  Limited code in templates.  This isn't meant to embed ruby in anything - 
  it allows for simple control structures, since that's typically what you need 
  in a template, but full access to the Ruby
  interpreter is just a tempatation into sin. (From a separation of concerns 
  standpoint.)  There's a certain amount of code available in conditionals and 
  interpolations, since otherwise they're much harder to do...

  *  Easy to extend.  If you do need something extra from a template, not 
  having it in the templating language is frustrating.  It's easy to add 
  features to stencil, since they're described in as well-designed classes.

  * Generic output.  Not everything is a website or a mime-encoded email.  It's 
  nice to be able to spit out generic text from time to time.

  * Data sourced from simple datatypes - hashes and array, referenced with data 
  paths.  Views can be extracted from any object, or built up in code.

## 官网

- 主页: http://stencil-templ.rubyforge.org/
- RubyGems: https://rubygems.org/gems/Stencil

## 历史版本号

- 0.1.1 (2010-01-04)
- 0.1 (2009-12-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/Stencil
- gem 安装: `gem install Stencil`
- Bundler: `gem "Stencil"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/Stencil-0.1.1.gem
- 版本锁定: `gem "Stencil", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
