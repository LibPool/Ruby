# msnav

**Tag**: web, database, tooling, data

## 简介

A pure-Ruby daemon (ruby-lsp style) serving the coderag navigation API —
cross-service go-to-definition, references, hover, and CodeLens targets —
from a coderag SQLite index. Built to run inside a Ruby devcontainer with
no Python: the host builds the index with coderag, the container mounts
the shared data dir and runs `msnav up`.

## 官网

- 主页: https://github.com/YaroslavZahoruiko/msnav
- 问题追踪: https://github.com/YaroslavZahoruiko/msnav/issues
- RubyGems: https://rubygems.org/gems/msnav

## 历史版本号

- 0.3.0 (2026-07-06)
- 0.2.0 (2026-07-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/msnav
- gem 安装: `gem install msnav`
- Bundler: `gem "msnav"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/msnav-0.3.0.gem
- 版本锁定: `gem "msnav", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
