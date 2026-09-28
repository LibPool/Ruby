# ditz

**Tag**: web, cli, database, template, filesystem, data

## 简介

Ditz is a simple, light-weight distributed issue tracker designed to work with distributed version control systems like git, darcs, Mercurial, and Bazaar. It can also be used with centralized systems like SVN.  Ditz maintains an issue database directory on disk, with files written in a line-based and human-editable format. This directory can be kept under version control, alongside project code.  Ditz provides a simple, console-based interface for creating and updating the issue database files, and some basic static HTML generation capabilities for producing world-readable status pages (for a demo, see the ditz ditz page).  Ditz includes a robust plugin system for adding commands, model fields, and modifying output. See PLUGINS.txt for documentation on the pre-shipped plugins.  Ditz currently offers no central public method of bug submission.   == USING DITZ  There are several different ways to use Ditz:  1. Treat issue change the same as code change: include it as part of commits, and merge it with changes from other developers, resolving conflicts in the usual manner. 2. Keep the issue database in the repository but in a separate branch. Issue changes can be managed by your VCS, but is not tied directly to code commits. 3. Keep the issue database separate and not under VCS at all.

## 官网

- 主页: http://ditz.rubyforge.org
- RubyGems: https://rubygems.org/gems/ditz

## 历史版本号

- 0.1.1 (2009-07-25)
- 0.5 (2009-07-25)
- 0.4 (2009-07-25)
- 0.3 (2009-07-25)
- 0.2 (2009-07-25)
- 0.1.2 (2009-07-25)
- 0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/ditz
- gem 安装: `gem install ditz`
- Bundler: `gem "ditz"`
- 最新版本: 0.5
- 最新版归档: https://rubygems.org/downloads/ditz-0.5.gem
- 版本锁定: `gem "ditz", "~> 0.5"`
- 中央仓库: https://rubygems.org/
