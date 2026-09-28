# sploit

**Tag**: web, security, networking

## 简介

Grab and eval Ruby code via HTTP. You don't care about security, right?

This gem is Dr. Nic's fault. We were looking for an easy way to run
Ruby code that was publicly available on a web server, and though
we've all written something to do this a time or two, we couldn't find
a convenient gem.

I hacked up a quick example:

    ruby -rubygems -ropen-uri -e \
      'eval open("http://gist.github.com/raw/473222/snippet.rb").read' \
      jbarnette dr-nic-magic-awesome

...but why use a simple Ruby one-liner when we can go overboard and
package it as a gem? While we're at it, why not add a tiny bit of
extra sugar for Gists?

This is not an original idea. It's been done a ton of times before,
but this one is ours. Don't use it for anything real or it'll melt
your face.

## 官网

- 主页: http://github.com/jbarnette/sploit
- RubyGems: https://rubygems.org/gems/sploit

## 历史版本号

- 1.0.0 (2010-07-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/sploit
- gem 安装: `gem install sploit`
- Bundler: `gem "sploit"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/sploit-1.0.0.gem
- 版本锁定: `gem "sploit", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
