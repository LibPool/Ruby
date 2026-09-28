# kanon

**Tag**: serialization, filesystem

## 简介

A YAML file becomes a frozen tree of nodes with dotted access, and the values
that belong to the environment are declared in that same file. A read that
misses a mandatory value fails naming every absent variable at once, and a
typo in a key raises instead of returning nil. ERB tags keep working, so a
file that already reads the environment that way needs no rewriting. The
standard library only, with the config directory and the environment name
injected from outside.

## 官网

- 主页: https://github.com/MaksimenkoPG/kanon
- 更新日志: https://github.com/MaksimenkoPG/kanon/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/kanon

## 历史版本号

- 0.1.0 (2026-09-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/kanon
- gem 安装: `gem install kanon`
- Bundler: `gem "kanon"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/kanon-0.1.0.gem
- 版本锁定: `gem "kanon", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
