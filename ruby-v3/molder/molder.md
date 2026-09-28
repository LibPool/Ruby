# molder

**Tag**: cli, serialization, template, devops, filesystem, data

## 简介

Molder is a handy command line tool for generating and running (in parallel, using a pool of processes with a configurable size) a set of related and yet
different commands. A YAML file defines both the attributes and the command
template, and Molder then merges the two with CLI arguments to give you a
consistent set of commands for, eg. provisioning thousands of virtual hosts in a cloud. The gem is not limnited to any particular cloud, tool, or a command, and can be used across various domains to generate a consistent set of commands based on the YAML-supplied attributes and templates, that might
vary across custom dimensions. For example, you could generate 600 provisioning commands for hosts in EC2, numbered from 1 to 100, but constrained to the zones "a", "b", "c", and data centers "dc" (values: ['us-west2', 'us-east1' ]). Behind the scenes Molder uses another Ruby gem Parallel — for actually running
the provisioning commands.

## 官网

- 主页: https://github.com/kigster/molder
- 文档: https://www.rubydoc.info/gems/molder/0.2.1
- RubyGems: https://rubygems.org/gems/molder

## 历史版本号

- 0.2.1 (2018-04-13)
- 0.2.0 (2018-04-13)
- 0.1.4 (2018-04-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/molder
- gem 安装: `gem install molder`
- Bundler: `gem "molder"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/molder-0.2.1.gem
- 版本锁定: `gem "molder", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
