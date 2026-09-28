# wr0ngway-rubber

**Tag**: web, testing, devops, filesystem

## 简介

The rubber plugin enables relatively complex multi-instance deployments of RubyOnRails applications to AmazonÕs Elastic Compute Cloud (EC2).  Like capistrano, rubber is role based, so you can define a set of configuration files for a role and then assign that role to as many concrete instances as needed. One can also assign multiple roles to a single instance. This lets one start out with a single ec2 instance (belonging to all roles), and add new instances into the mix as needed to scale specific facets of your deployment, e.g. adding in instances that serve only as an 'app' role to handle increased app server load.

## 官网

- 主页: http://github.com/wr0ngway/rubber
- 文档: https://www.rubydoc.info/gems/wr0ngway-rubber/1.0.1
- RubyGems: https://rubygems.org/gems/wr0ngway-rubber

## 历史版本号

- 1.0.0 (2014-08-10)
- 1.0.1 (2014-08-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/wr0ngway-rubber
- gem 安装: `gem install wr0ngway-rubber`
- Bundler: `gem "wr0ngway-rubber"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/wr0ngway-rubber-1.0.1.gem
- 版本锁定: `gem "wr0ngway-rubber", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
