# lnbackup

**Tag**: web, testing, filesystem

## 简介

Lnbackup is a hardlink backup system for hard drives. 

Lnbackup operates in a way similar to the '--link-dest' switch in rsync.

It creates incremental backups using hardlinks so that each backup seems like a
full backup. Additionaly it can make (using hardlinks) bootable mirror from the
latest backup.

Obviously the target filesystem of lnbackup needs to support hardlinks.

It's run on ~200 servers for several years and it is considered stable.

Read the man page for more information.

## 官网

- 主页: https://github.com/martinpovolny/lnbackup
- RubyGems: https://rubygems.org/gems/lnbackup

## 历史版本号

- 2.4 (2012-11-25)
- 2.3 (2012-11-24)
- 2.2 (2012-11-08)
- 2.1 (2012-11-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/lnbackup
- gem 安装: `gem install lnbackup`
- Bundler: `gem "lnbackup"`
- 最新版本: 2.4
- 最新版归档: https://rubygems.org/downloads/lnbackup-2.4.gem
- 版本锁定: `gem "lnbackup", "~> 2.4"`
- 中央仓库: https://rubygems.org/
