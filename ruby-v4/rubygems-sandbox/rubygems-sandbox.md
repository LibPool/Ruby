# rubygems-sandbox

**Tag**: filesystem

## 简介

The sandbox plugin for rubygems helps you manage your command-line
tools and their dependencies. Sandboxed gems are installed in their
own private rubygem repositories with all of their dependencies. This
means that you don't have to have a rat's nest of gems in your global
repository in order to run popular command-tools like rdoc, flog,
flay, rcov, etc.

gem sandbox has the following sub-commands:

  * install gem_name ...             - install 1 or more gems
  * plugin  gem_name plugin_name ... - install a gem and plugins for it
  * remove  gem_name ...             - uninstall 1 or more gems
  * help                             - show this output

Once you install gem sandbox will output something like:

    Copy the following scripts to any directory in your path to use them:

    cp /Users/USER/.gem/sandboxes/GEM/bin/TOOL _in_your_$PATH_

Copy the scripts to a directory in your path (eg ~/bin or /usr/bin)
and you're good to go.

## 官网

- 主页: http://www.zenspider.com/projects/rubygems-sandbox.html
- 源码仓库: https://github.com/seattlerb/rubygems-sandbox
- RubyGems: https://rubygems.org/gems/rubygems-sandbox

## 历史版本号

- 1.3.2 (2024-08-27)
- 1.3.1 (2019-12-13)
- 1.3.0 (2014-08-06)
- 1.2.0 (2014-02-11)
- 1.1.1 (2011-12-15)
- 1.1.0 (2011-09-28)
- 1.0.0 (2011-07-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/rubygems-sandbox
- gem 安装: `gem install rubygems-sandbox`
- Bundler: `gem "rubygems-sandbox"`
- 最新版本: 1.3.2
- 最新版归档: https://rubygems.org/downloads/rubygems-sandbox-1.3.2.gem
- 版本锁定: `gem "rubygems-sandbox", "~> 1.3.2"`
- 中央仓库: https://rubygems.org/
