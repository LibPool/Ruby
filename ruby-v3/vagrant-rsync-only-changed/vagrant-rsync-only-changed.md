# vagrant-rsync-only-changed

**Tag**: filesystem

## 简介

Currently Vagrant rsync-auto command will always issue a full rsync when an event is detected during rsync-auto. With this plugin rsync will be called with the parameter --files-from with only the added/changed/removed files and/or directories listed. This will speed up a lot the command for big file trees.

## 官网

- 主页: https://github.com/nuncanada/vagrant-rsync-only-changed
- 文档: https://www.rubydoc.info/gems/vagrant-rsync-only-changed/0.9.1
- RubyGems: https://rubygems.org/gems/vagrant-rsync-only-changed

## 历史版本号

- 0.9.1 (2016-01-13)
- 0.9.0 (2016-01-13)
- 0.8.3 (2016-01-13)
- 0.8.2 (2016-01-12)
- 0.8.0 (2016-01-12)
- 0.7.1 (2016-01-11)
- 0.7.0 (2016-01-11)
- 0.6.0 (2016-01-11)
- 0.5.0 (2016-01-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/vagrant-rsync-only-changed
- gem 安装: `gem install vagrant-rsync-only-changed`
- Bundler: `gem "vagrant-rsync-only-changed"`
- 最新版本: 0.9.1
- 最新版归档: https://rubygems.org/downloads/vagrant-rsync-only-changed-0.9.1.gem
- 版本锁定: `gem "vagrant-rsync-only-changed", "~> 0.9.1"`
- 中央仓库: https://rubygems.org/
