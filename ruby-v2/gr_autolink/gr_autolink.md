# gr_autolink

**Tag**: web, networking, template

## 简介

This is an adaptation of the extraction of the `auto_link` method from rails
that is the rails_autolink gem.  The `auto_link`
method was removed from Rails in version Rails 3.1.  This gem is meant to
bridge the gap for people migrating...and behaves a little differently from the
parent gem we forked from:

* performs html-escaping of characters such as '&' in strings that are getting
  linkified if the incoming string is not html_safe?
* retains html-safety of incoming string (if input string is unsafe, will return
  unsafe and vice versa)
* fixes at least one bug:
  (<img src="http://some.u.rl"> => <img src="<a href="http://some.u.rl">http://some.u.rl</a>">)
  though can't imagine this is intended behavior, also have trouble believing that
  this was an open bug in rails...

## 官网

- 主页: https://github.com/goodreads/gr_autolink
- 文档: https://www.rubydoc.info/gems/gr_autolink/1.0.13
- RubyGems: https://rubygems.org/gems/gr_autolink

## 历史版本号

- 1.0.13 (2014-03-28)
- 1.0.11 (2012-04-18)
- 1.0.10 (2012-04-02)
- 1.0.9 (2012-03-31)
- 1.0.8 (2012-03-31)
- 1.0.7 (2012-03-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/gr_autolink
- gem 安装: `gem install gr_autolink`
- Bundler: `gem "gr_autolink"`
- 最新版本: 1.0.13
- 最新版归档: https://rubygems.org/downloads/gr_autolink-1.0.13.gem
- 版本锁定: `gem "gr_autolink", "~> 1.0.13"`
- 中央仓库: https://rubygems.org/
