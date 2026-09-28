# mop

**Tag**: web, cli, networking, filesystem

## 简介

Make OK for Public.  A simplistic pre-filter (not (yet|ever) a substitute for manual examination).

== Usage

 mop < /var/log/nginx/error_log > cleaned_file
 vim cleaned_file
 # ☝ check for anything it might've missed
 jist -co cleaned_file
 # ☝ upload, copy its URL to clipboard, open in browser

== Note

This thing is really in its beginning phases. It currently:

* Deletes too much
* Leaves too much

However, all Issues will be addressed.  Just file 'em at:
https://github.com/rking/mop/issues

## 官网

- 主页: https://github.com/exad/mop
- RubyGems: https://rubygems.org/gems/mop

## 历史版本号

- 0.0.6 (2013-01-05)
- 0.0.5 (2013-01-05)
- 0.0.4 (2013-01-05)
- 0.0.3 (2013-01-05)
- 0.0.2 (2013-01-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/mop
- gem 安装: `gem install mop`
- Bundler: `gem "mop"`
- 最新版本: 0.0.6
- 最新版归档: https://rubygems.org/downloads/mop-0.0.6.gem
- 版本锁定: `gem "mop", "~> 0.0.6"`
- 中央仓库: https://rubygems.org/
