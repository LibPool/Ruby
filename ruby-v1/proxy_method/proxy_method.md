# proxy_method

**Tag**: library

## 简介

The purpose of this gem is to prevent directly running the inherited
    methods you choose to block at either the class or instance level, and
    instead do one of two things: run an alternative block which may or may
    not invoke the original method, or simply raise an error message.

    The error message can be customized. The original method can still be
    called under a different name. The entire object or class can return
    "unproxied" versions of themselves to preserve the original functionality.

    This was originally created to help enforce the use of interactors over
    directly calling ActiveRecord methods like create, save, and update. As
    with any metaprogramming, this gives you plenty of rope to hang yourself
    if you try to get too "clever". Treat this library like salt; use
    sparingly, because over time its cumulative effect will kill you :)

## 官网

- 主页: https://github.com/Intellifarm/proxy_method
- 文档: https://www.rubydoc.info/gems/proxy_method/1.2.9
- RubyGems: https://rubygems.org/gems/proxy_method

## 历史版本号

- 1.2.9 (2020-01-11)
- 1.2.8 (2020-01-10)
- 1.2.7 (2020-01-09)
- 1.2.6 (2020-01-08)
- 1.2.5 (2020-01-07)
- 1.2.3 (2020-01-06)
- 1.2.2 (2020-01-04)
- 1.2.1 (2020-01-02)
- 1.2.0 (2019-12-30)
- 1.1.2 (2019-12-29)
- 1.1.1 (2019-12-28)
- 1.1.0 (2019-12-27)
- 1.0.0 (2019-12-21)
- 0.1.3 (2019-12-20)
- 0.1.2 (2019-12-19)
- 0.1.1 (2019-12-18)
- 0.1.0 (2019-12-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/proxy_method
- gem 安装: `gem install proxy_method`
- Bundler: `gem "proxy_method"`
- 最新版本: 1.2.9
- 最新版归档: https://rubygems.org/downloads/proxy_method-1.2.9.gem
- 版本锁定: `gem "proxy_method", "~> 1.2.9"`
- 中央仓库: https://rubygems.org/
