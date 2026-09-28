# lightning

**Tag**: testing, tooling, filesystem

## 简介

Lightning is a commandline framework that lets users wrap commands with shell functions that are able to refer to any filesystem path by its basename. To achieve this, a group of paths to be translated are defined with shell globs. These shell globs, known as a lightning _bolt_, are then applied to commands to produce functions. In addition to translating basenames to full paths, lightning _functions_ can autocomplete these basenames, resolve conflicts if they have the same name, leave any non-basename arguments untouched, and autocomplete directories above and below a basename. To make bolts shareable between users and functions easier to create, lightning has _generators_. A _generator_ generates filesystem-specific globs for a bolt. Lightning comes with some default generators. Users can make their own generators with generator plugins placed under ~/.lightning/generators/.

## 官网

- 主页: http://tagaholic.me/lightning/
- RubyGems: https://rubygems.org/gems/lightning

## 历史版本号

- 0.4.1 (2012-02-24)
- 0.4.0 (2011-04-20)
- 0.3.4 (2011-04-08)
- 0.3.3 (2011-02-08)
- 0.3.2 (2010-04-13)
- 0.3.1 (2010-04-09)
- 0.3.0 (2010-04-09)
- 0.2.1 (2009-10-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/lightning
- gem 安装: `gem install lightning`
- Bundler: `gem "lightning"`
- 最新版本: 0.4.1
- 最新版归档: https://rubygems.org/downloads/lightning-0.4.1.gem
- 版本锁定: `gem "lightning", "~> 0.4.1"`
- 中央仓库: https://rubygems.org/
