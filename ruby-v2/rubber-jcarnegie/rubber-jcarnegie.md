# rubber-jcarnegie

**Tag**: web, testing, devops, filesystem

## 简介

The rubber plugin enables relatively complex multi-instance deployments of RubyOnRails applications to
      Amazon's Elastic Compute Cloud (EC2).  Like capistrano, rubber is role based, so you can define a set
      of configuration files for a role and then assign that role to as many concrete instances as needed. One
      can also assign multiple roles to a single instance. This lets one start out with a single ec2 instance
      (belonging to all roles), and add new instances into the mix as needed to scale specific facets of your
      deployment, e.g. adding in instances that serve only as an 'app' role to handle increased app server load.
      
      Adding deployment tasks for Node.js and others.

## 官网

- 主页: http://github.com/jcarnegie/rubber
- RubyGems: https://rubygems.org/gems/rubber-jcarnegie

## 历史版本号

- 0.0.1 (2011-01-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/rubber-jcarnegie
- gem 安装: `gem install rubber-jcarnegie`
- Bundler: `gem "rubber-jcarnegie"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/rubber-jcarnegie-0.0.1.gem
- 版本锁定: `gem "rubber-jcarnegie", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
