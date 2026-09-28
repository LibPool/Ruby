# nogara-rubber

**Tag**: web, testing, devops, filesystem

## 简介

The rubber plugin enables relatively complex multi-instance deployments of RubyOnRails applications to
      Amazon's Elastic Compute Cloud (EC2).  Like capistrano, rubber is role based, so you can define a set
      of configuration files for a role and then assign that role to as many concrete instances as needed. One
      can also assign multiple roles to a single instance. This lets one start out with a single ec2 instance
      (belonging to all roles), and add new instances into the mix as needed to scale specific facets of your
      deployment, e.g. adding in instances that serve only as an 'app' role to handle increased app server load.

## 官网

- 主页: http://github.com/wr0ngway/rubber
- RubyGems: https://rubygems.org/gems/nogara-rubber

## 历史版本号

- 1.7.2 (2010-11-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/nogara-rubber
- gem 安装: `gem install nogara-rubber`
- Bundler: `gem "nogara-rubber"`
- 最新版本: 1.7.2
- 最新版归档: https://rubygems.org/downloads/nogara-rubber-1.7.2.gem
- 版本锁定: `gem "nogara-rubber", "~> 1.7.2"`
- 中央仓库: https://rubygems.org/
