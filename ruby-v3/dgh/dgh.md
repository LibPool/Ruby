# dgh

**Tag**: filesystem

## 简介

Dgh helps when you have to manually downgrade a large amount of packages.
It requires the user to generate a file with `apt-cache policy` output for all
installed packages, which it then reads. It looks for packages that have a
currently installed version that doesn't exist in any repository, and prints
those. This includes both locally generated packages that never did exist in
any repository, and more crucially, packages that have been upgraded from e.g.
a PPA that has since been removed from the system.

## 官网

- 主页: http://github.com/ilkka/dgh
- RubyGems: https://rubygems.org/gems/dgh

## 历史版本号

- 0.1.4 (2011-11-09)
- 0.1.3 (2011-09-18)
- 0.1.2 (2011-05-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/dgh
- gem 安装: `gem install dgh`
- Bundler: `gem "dgh"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/dgh-0.1.4.gem
- 版本锁定: `gem "dgh", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
