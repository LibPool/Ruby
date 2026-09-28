# army-negative

**Tag**: web, database, testing, data

## 简介

When this gem is loaded and activated inside your rails app, your MySQL
connection adapter for ActiveRecord will be monkey-patched. The patch simply
tweaks it to store all boolean "true" values as negative one instead of
positive one inside your TINYINT columns. It also patches it to recognize
and interpret negative one as "true". Positive one will still be recognized
as true as well.
Used for special cases, such as developing rails apps that must, for
example, work with existing databases that use such a convention.
For a rails app version X.Y.Z, use army-negative version "~> X.Y.0". For
example, a rails 3.0.x app should use "~> 3.0.0" and a 3.1.x app would use
"~> 3.1.0", etc. The exception is that rails 2.3.x apps should just use
"~> 2.0" since 2.3 is the earliest version of rails that's supported.

## 官网

- 主页: http://github.com/zettabyte/army-negative
- RubyGems: https://rubygems.org/gems/army-negative

## 历史版本号

- 3.1.0 (2011-09-14)
- 3.0.0 (2011-09-13)
- 2.0.0 (2011-09-12)
- 1.0.0 (2011-03-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/army-negative
- gem 安装: `gem install army-negative`
- Bundler: `gem "army-negative"`
- 最新版本: 3.1.0
- 最新版归档: https://rubygems.org/downloads/army-negative-3.1.0.gem
- 版本锁定: `gem "army-negative", "~> 3.1.0"`
- 中央仓库: https://rubygems.org/
