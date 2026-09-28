# http_url_validation_improved

**Tag**: web, testing, networking

## 简介

a Rails gem that allows you to validate a URL 
entered in a form. It validates if the URL exists by hitting it with a HEAD 
request.

The improved version includes retries for common patterns when the head request is refused before giving a failure notice.

It also looks up a SITE_URL constant to the user agent in the headers.

Also has the option to also check that the URL returns content of 
a specified type.

## 官网

- 主页: http://github.com/kete/http_url_validation_improved
- RubyGems: https://rubygems.org/gems/http_url_validation_improved

## 历史版本号

- 1.3.1 (2012-06-15)
- 1.3.0 (2011-02-04)
- 1.2.0 (2010-06-15)
- 1.1.1 (2010-06-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/http_url_validation_improved
- gem 安装: `gem install http_url_validation_improved`
- Bundler: `gem "http_url_validation_improved"`
- 最新版本: 1.3.1
- 最新版归档: https://rubygems.org/downloads/http_url_validation_improved-1.3.1.gem
- 版本锁定: `gem "http_url_validation_improved", "~> 1.3.1"`
- 中央仓库: https://rubygems.org/
