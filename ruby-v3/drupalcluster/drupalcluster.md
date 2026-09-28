# drupalcluster

**Tag**: web, cli, testing, networking, tooling, devops, filesystem, data

## 简介

+drupalcluster+  is a command line tool to quickly
deploy a Drupal hosting cluster of a scalable amount [2..5]
of virtual webservers.

!! AWS identity is required for this script !!
Your AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY should be either
environment variables, or set in ~/.aws/credentials.

The configuration file contains additional details for the cluster,
including an ssh KeyName that's needed to access the servers.
The KeyName defaults to 'Drupal', easiest if it's precreated.
   $HOME/.drc/drupalcluster.conf

This is a demo version only, builds Drupal on HTTP connection.
Don't use it seriously. 
Especially, don't post personal/sensitive data on your Drupal site.

==== Commands

  create name      -- Creates a Drupal hosting cluster
  check [name]     -- Checks the status of creation/deletion 
  delete name      -- Deletes permanently the given cluster
  test name|url    -- Sends a simple HTTP GET to the URL (of the given cluster)
  attack instance  -- Permanently terminates the given server instance
  list             -- Lists the recently created/deleted clusters.

-----------------------

*** Please contribute to add rspec's ***

## 官网

- 主页: https://github.com/zellerede/drupalcluster
- 文档: https://www.rubydoc.info/gems/drupalcluster/0.1.2
- RubyGems: https://rubygems.org/gems/drupalcluster

## 历史版本号

- 0.1.2 (2017-11-05)
- 0.1.1 (2017-11-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/drupalcluster
- gem 安装: `gem install drupalcluster`
- Bundler: `gem "drupalcluster"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/drupalcluster-0.1.2.gem
- 版本锁定: `gem "drupalcluster", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
