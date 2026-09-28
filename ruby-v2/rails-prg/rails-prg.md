# rails-prg

**Tag**: web

## 简介

Secure applications disable browser history and internal cache.
  Unfortunately, this causes problems with most browsers when following
  the standard Rails pattern for displaying errors.

  For full protection from ERR_CACHE_MISS (in Chrome with no-cache, no-store),
  and equivalent in other browsers, the pattern should be altered to follow
  a full POST-REDIRECT-GET patten.

  This way the browser will always have a consistent back-button history to
  traverse without triggering browser errors.

## 官网

- 主页: https://github.com/tommeier/rails-prg
- 文档: https://www.rubydoc.info/gems/rails-prg/0.1.1
- RubyGems: https://rubygems.org/gems/rails-prg

## 历史版本号

- 0.1.1 (2014-03-19)
- 0.1.0 (2014-03-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails-prg
- gem 安装: `gem install rails-prg`
- Bundler: `gem "rails-prg"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/rails-prg-0.1.1.gem
- 版本锁定: `gem "rails-prg", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
