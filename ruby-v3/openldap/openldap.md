# openldap

**Tag**: web, testing

## 简介

A simple, but feature-complete Ruby binding for OpenLDAP's libldap. 

This binding is intended as an alternative for [ruby-ldap][] for libraries or applications which require a more complete implementation of the LDAP protocol (according to [RFC4511][]) than it provides.

Additions or changes:

* Referrals for add, modify, delete, modrdn, compare
* Controls for add, modify, delete, modrdn, compare
* Asynchronous and synchronous APIs
* Detailed exception class hierarchy for results instead of just one
  class for all non-success results.
* Complete [RFC4511][] support:
  - extended operations and results
  - unsolicited notifications
  - continuation references
  - intermediate responses
  - alias deferencing
  - etc.
* Cleanly abandon terminated operations where supported
* Memory-handling cleanup to avoid leaks, corruption, and other
  problems experienced in the wild.
* Drop deprecated non-_ext variants of operations which have a 
  modern equivalent.
* M17n for Ruby 1.9.x.
* Improved test coverage

**NOTE:** This library is still under development, and should not be considered to be feature-complete or production-ready.

This project's versions follow the [Semantic Versioning Specification][semver].

## 官网

- 主页: http://bitbucket.org/ged/ruby-openldap
- RubyGems: https://rubygems.org/gems/openldap

## 历史版本号

- 0.0.1pre11 (2011-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/openldap
- gem 安装: `gem install openldap`
- Bundler: `gem "openldap"`
- 最新版本: 0.0.1pre11
- 最新版归档: https://rubygems.org/downloads/openldap-0.0.1pre11.gem
- 版本锁定: `gem "openldap", "~> 0.0.1pre11"`
- 中央仓库: https://rubygems.org/
