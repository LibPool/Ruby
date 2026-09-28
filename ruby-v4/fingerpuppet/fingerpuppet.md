# fingerpuppet

**Tag**: web, testing, security, filesystem

## 简介

`fingerpuppet` is a simple library and commandline tool to interact with Puppet's REST API
without needing to have Puppet itself installed. This may be integrated, for example,
into a provisioning tool to allow your provisioning process to remotely sign certificates
of newly built systems. Alternatively, you could use it to request known facts about
a node from your Puppet Master, or even to request a catalog for a node to, for example,
perform acceptance testing against a new version of Puppet before upgrading your
production master.

Install the binford2k/fingerpuppet puppet module to get a class that can automatically
configure your `auth.conf` file under Puppet Enterprise, where that file is managed.

## 官网

- 主页: http://github.com/binford2k/fingerpuppet
- 文档: https://www.rubydoc.info/gems/fingerpuppet/0.0.4
- RubyGems: https://rubygems.org/gems/fingerpuppet

## 历史版本号

- 0.0.4 (2014-05-10)
- 0.0.2 (2013-04-04)
- 0.0.1 (2013-03-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/fingerpuppet
- gem 安装: `gem install fingerpuppet`
- Bundler: `gem "fingerpuppet"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/fingerpuppet-0.0.4.gem
- 版本锁定: `gem "fingerpuppet", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
