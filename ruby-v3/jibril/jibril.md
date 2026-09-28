# jibril

**Tag**: web, serialization

## 简介

Simple chef-inspired configuration management tool. While chef is awesome,
it has crazy high requirements (mainly memory-wise) for managing like
8 devices I have.

Ansible would be great IF all my devices were reachable, however some are
behind NATs.

Jibril tries to solve both issue. It's designed to be light on the server
(raspberry pi is enough), with one server (so NATs are not an issue)
and ruby DSL for the configuration scripts (so like chef, I don't like the
way ansible uses yaml for this).

## 官网

- 主页: https://github.com/graywolf/jibril
- 文档: https://www.rubydoc.info/gems/jibril/0.0.1
- RubyGems: https://rubygems.org/gems/jibril

## 历史版本号

- 0.0.1 (2018-01-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/jibril
- gem 安装: `gem install jibril`
- Bundler: `gem "jibril"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/jibril-0.0.1.gem
- 版本锁定: `gem "jibril", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
