# ec2_templater

**Tag**: web, template, devops

## 简介

Ec2Templater provides a means of EC2 service discovery by templating your server config. It works by periodically querying AWS for the list of running EC2 instances, rendering a template, then running a notify command if it has changed. Using this setup you can provide, for example, a haproxy config that updates based on instances that are available filtered by tag

## 官网

- 主页: https://github.com/reinteractive/ec2_templater
- 文档: https://www.rubydoc.info/gems/ec2_templater/0.1.0
- RubyGems: https://rubygems.org/gems/ec2_templater

## 历史版本号

- 0.1.0 (2016-03-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/ec2_templater
- gem 安装: `gem install ec2_templater`
- Bundler: `gem "ec2_templater"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/ec2_templater-0.1.0.gem
- 版本锁定: `gem "ec2_templater", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
