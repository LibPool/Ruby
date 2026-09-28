# master_delivery

**Tag**: testing, filesystem

## 简介

Deliver all master files managed in a single master snapshot directory
into the specified directory while maintaining the hierarchy of the
master snapshot directory. If the destination file already exists,
back it up first and then deliver the master file.

The difference with rsync is that master_delivery creates a symlinks
instead of copying the master files. They are symlinks, so you have to
keep in mind that you have to keep the master files in the same location,
but it also has the advantage that the master file is updated at the same
time when you directly make changes to the delivered file.

Do you have any experience that the master file is getting old gradually?
master_delivery can prevent this.

If the master directory is git or svn managed, you can manage revisions
of files that are delivered here and there at once with commands
like git diff and git commit.

## 官网

- 主页: https://github.com/shinyaohtani/master_delivery/tree/master/README.md
- 源码仓库: https://github.com/shinyaohtani/master_delivery
- 更新日志: https://github.com/shinyaohtani/master_delivery/tree/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/master_delivery

## 历史版本号

- 1.0.7 (2020-05-11)
- 1.0.6 (2020-05-06)
- 1.0.5 (2020-05-03)
- 1.0.4 (2020-04-28)
- 1.0.3 (2020-04-28)
- 1.0.2 (2020-04-27)
- 1.0.1 (2020-04-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/master_delivery
- gem 安装: `gem install master_delivery`
- Bundler: `gem "master_delivery"`
- 最新版本: 1.0.7
- 最新版归档: https://rubygems.org/downloads/master_delivery-1.0.7.gem
- 版本锁定: `gem "master_delivery", "~> 1.0.7"`
- 中央仓库: https://rubygems.org/
