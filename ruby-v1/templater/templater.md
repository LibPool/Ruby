# templater

**Tag**: cli, testing, template, tooling, filesystem

## 简介

Templater has the ability to both copy files from A to B and also to render templates using ERB. Templater consists of four parts:

- Actions (File copying routines, templates generation and directories creation routines).
- Generators (set of rules).
- Manifolds (generator suites).
- The command line interface.

Hierarchy is pretty simple: manifold has one or many public and private generators. Public ones are supposed to be called
by end user. Generators have one or more action that specify what they do, where they take files, how they name resulting
files and so forth.

## 官网

- 主页: http://github.com/jnicklas/templater
- RubyGems: https://rubygems.org/gems/templater

## 历史版本号

- 1.0.0 (2009-09-24)
- 0.1.6 (2009-07-25)
- 0.1.5 (2009-07-25)
- 0.1.4 (2009-07-25)
- 0.1.3 (2009-07-25)
- 0.1.2 (2009-07-25)
- 0.1.1 (2009-07-25)
- 0.1 (2009-07-25)
- 0.3.4 (2009-07-25)
- 0.3.3 (2009-07-25)
- 0.3.2 (2009-07-25)
- 0.3.1 (2009-07-25)
- 0.3.0 (2009-07-25)
- 0.2.2 (2009-07-25)
- 0.2.1 (2009-07-25)
- 0.2 (2009-07-25)
- 0.5.0 (2009-07-25)
- 0.4.5 (2009-07-25)
- 0.4.4 (2009-07-25)
- 0.4.3 (2009-07-25)
- 0.4.2 (2009-07-25)
- 0.4.1 (2009-07-25)
- 0.4.0 (2009-07-25)
- 0.3.5 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/templater
- gem 安装: `gem install templater`
- Bundler: `gem "templater"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/templater-1.0.0.gem
- 版本锁定: `gem "templater", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
