# onesie

**Tag**: web, networking, template, filesystem

## 简介

A Rack middleware to make URLs in one-page webapps easier.

In a couple of recent projects, I've needed to avoid full page
refreshes as much as possible. In the first, I wanted to keep an
embedded music player active while the user was browsing. In the
second, I just wanted fancier transitions between pages.

It's possible to do this in an ad-hoc way, but I very quickly got
tired of hacking things together. Enter Onesie.

Onesie congealed from these requirements:

* I want a one-page web app,
* But I want the back button to work,
* And I want search engines to still index some stuff,
* And I (mostly) don't want to change the way I write a Rails/Sinatra app.

If someone visits <tt>http://example.org/meta/contact</tt>, I want
them to be redirected to <tt>http://example.org/blah/#/meta/contact</tt>,
but after the redirection I still want the original route to be
rendered for search engine indexing, etc.

When Onesie gets a request, it looks to see if under your preferred
one-page app path ("blah" in the example above). If it's not, Onesie
sets the current request's path in the session and redirects to your
app path.

If a request is under the one-page app path, the "real" request's path
is retrieved from the session and used for subsequent routing and
rendering. This means that, as above, a request for

    http://example.org/meta/contact

Will be redirected to

    http://example.org/blah/#/meta/contact

But still render the correct action in the wrapped app, even though
URL fragments aren't passed to the server.

This is a terrible explanation. I'll write a sample app or something
soon.

## 官网

- 主页: http://github.com/jbarnette/onesie
- RubyGems: https://rubygems.org/gems/onesie

## 历史版本号

- 1.0.0 (2010-08-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/onesie
- gem 安装: `gem install onesie`
- Bundler: `gem "onesie"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/onesie-1.0.0.gem
- 版本锁定: `gem "onesie", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
