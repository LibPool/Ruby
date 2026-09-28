# developing_gems

**Tag**: filesystem

## 简介

Include development gems, but only if we're not in production.
Provides a method (DevelopingGems.gems) that can be invoked in the Gemfile, and 
one (DevelopingGems.requires) that can be used in the code to require the gems.

The standard list of development gems is:
- pry
- pry-stack_explorer
- pry-doc

This may be overridden in two ways:
- The DevelopingGems.gems and DevelopingGems.requires methods take an optional 
  argument that is an array of gem names, which it will use.
- If a $DEVELOPING_GEMS environment variable exists, it will be used. It is 
  expected to be a list of gem names, separated by spaces.

## 官网

- 主页: https://github.com/rleber/developing_gems
- 更新日志: https://github.com/rleber/developing_gems/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/developing_gems

## 历史版本号

- 0.1.2 (2025-06-11)
- 0.1.1 (2025-06-11)
- 0.1.0 (2025-06-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/developing_gems
- gem 安装: `gem install developing_gems`
- Bundler: `gem "developing_gems"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/developing_gems-0.1.2.gem
- 版本锁定: `gem "developing_gems", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
