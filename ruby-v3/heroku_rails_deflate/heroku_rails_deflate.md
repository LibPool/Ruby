# heroku_rails_deflate

**Tag**: web, filesystem

## 简介

This gem is designed for use by Rails applications running on Heroku. For others, the better approach is to use a frontend server such as nginx or Apache. However, the Heroku Cedar stack is no longer fronted by a file server, and there is no automatic provision for gzipping responses. This gem activates Rack::Deflate for all requests. In addition, we serve up the gzipped versions of our precompiled assets, taking advantage of the higher compression ratio used during precompilation, and reducing CPU load at request time.

## 官网

- 主页: http://github.com/mattolson/heroku_rails_deflate
- 文档: https://www.rubydoc.info/gems/heroku_rails_deflate/1.0.3
- RubyGems: https://rubygems.org/gems/heroku_rails_deflate

## 历史版本号

- 1.0.3 (2014-02-18)
- 1.0.2 (2014-02-13)
- 1.0.1 (2013-08-02)
- 1.0.0 (2013-04-03)
- 0.2.1 (2013-04-02)
- 0.2.0 (2013-04-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/heroku_rails_deflate
- gem 安装: `gem install heroku_rails_deflate`
- Bundler: `gem "heroku_rails_deflate"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/heroku_rails_deflate-1.0.3.gem
- 版本锁定: `gem "heroku_rails_deflate", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
