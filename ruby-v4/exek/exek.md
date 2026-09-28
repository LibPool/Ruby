# exek

**Tag**: testing, tooling, filesystem

## 简介

Most existing gems that address command execution provide a limited interface
or lack notable features. In contast, Exek seeks to provide comprehensive
support for all of a program's exec needs with one thoughtfully-designed
library.

Intended features:

- A "Command" class that encapsulates argv, env, and IO options, and
  process state.
- Easy-to-use high level interfaces with sensible defaults for running commands
  to completion.
- Comprehensive support for low-level concerns like piping, PTYs, and file
  descriptor magic.
- Utilities for manipulating `sh` script strings, idiomatically building
  argument arrays, and generating reusable interaces for common system commands.
- Tracing and introspection facilities for logging and latency analysis.
- Safety: does not monkeypatch external modules, encourage mixins or use eval.
  Attempts to guide developers away from unsafe practices like shell scripts
  and shell injection.

## 官网

- 主页: https://github.com/justjake/exek
- 文档: https://www.rubydoc.info/gems/exek/0.0.1
- RubyGems: https://rubygems.org/gems/exek

## 历史版本号

- 0.0.1 (2017-07-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/exek
- gem 安装: `gem install exek`
- Bundler: `gem "exek"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/exek-0.0.1.gem
- 版本锁定: `gem "exek", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
