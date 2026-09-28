# rabbit-slide-kou-rubykaigi-2025

**Tag**: web, testing, security, networking, template, tooling

## 简介

I talked about ((<"Goodbye fat gem"|URL:https://rubykaigi.org/2020/presentations/ktou.html>)) at RubyKaigi Takeout 2020. Fat gem is a gem that includes pre-built binaries. Extension libraries can assume that users have build environment with Ruby 2.4 or later. So gems don't need to bundle pre-built binaries for easy to install. Users can build binaries by themselves.

As of 2025, we're still using fat gem...

I discussed how to improve this situation with ruby-installer author, Nokogiri maintainer and RubyGems community in 2022:

  * ((<"[RFC] Allow specifying and installing external dependencies"|URL:https://gist.github.com/postmodern/4c0cbccc0c7eda4585db0fc5267cdd57>))
  * ((<"Standardize +requirements+ field from the specification rubygems/rubygems#1296"|URL:https://github.com/rubygems/rubygems/issues/1296>))

I propose a solution based on these discussions.

## 官网

- 主页: https://slide.rabbit-shocker.org/authors/kou/rubykaigi-2025/
- 源码仓库: https://gitlab.com/ktou/rabbit-slide-kou-rubykaigi-2025
- RubyGems: https://rubygems.org/gems/rabbit-slide-kou-rubykaigi-2025

## 历史版本号

- 2025.4.16.2 (2025-06-02)
- 2025.4.16.1 (2025-04-16)
- 2025.4.16.0 (2025-04-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/rabbit-slide-kou-rubykaigi-2025
- gem 安装: `gem install rabbit-slide-kou-rubykaigi-2025`
- Bundler: `gem "rabbit-slide-kou-rubykaigi-2025"`
- 最新版本: 2025.4.16.2
- 最新版归档: https://rubygems.org/downloads/rabbit-slide-kou-rubykaigi-2025-2025.4.16.2.gem
- 版本锁定: `gem "rabbit-slide-kou-rubykaigi-2025", "~> 2025.4.16.2"`
- 中央仓库: https://rubygems.org/
