# rugs

**Tag**: web, template

## 简介

= RUGS - RUby Git Setup

A helper script that makes setting up remote git repositories a snap.  

== WARNING: This is still alpha so use it at your own risk!
Note: I don't use alpha/beta in the version numbers until I have a first real release because of how Ruby Gems handles them.

== What is it?

RUGS has three main functions:  

* Creates a local git repository and directory structure using default templates or ones you create.
* Sets up a remote repository to mirror your local one.
* Adds a framework of git hooks allowing you to store and run your own hooks in directly from the repo.

RUGS makes creating remote repos as simple as `rugs create repo_name on server_name`.

RUGS even allows you to automatically embed your Git hooks in the repo itself. No more jumping through hoops to make sure your hooks are maintained with your project; with RUGS you just store your hook scripts in the `git_hooks` directory and they're automatically updated and run. \ 

Once you've set up your project using RUGS you just use Git as you normally would with the exception of your hooks being the in `git_hooks` directory.

## 官网

- 主页: http://mikbe.tk
- RubyGems: https://rubygems.org/gems/rugs

## 历史版本号

- 0.1.1 (2011-09-25)
- 0.1.0 (2011-09-25)
- 0.0.1 (2011-09-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/rugs
- gem 安装: `gem install rugs`
- Bundler: `gem "rugs"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/rugs-0.1.1.gem
- 版本锁定: `gem "rugs", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
