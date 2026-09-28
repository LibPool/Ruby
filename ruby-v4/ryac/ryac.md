# ryac

**Tag**: filesystem

## 简介

Ryac minifies Ruby source code using Prism AST transformations and TypeProf type inference. It bundles a program's require_relative and autoload graph into one file (dynamic requires become lazy regions), compacts and folds the AST, renames constants, variables and methods with compatibility aliases for the names a caller outside the bundle may still use, and can emit the result as a self-extracting file. Two levels: stable renames a method only when type inference resolved every caller; unstable also renames methods with unresolved callers. Ryac is under active development: its architecture, interfaces and output format may change between releases.

## 官网

- 主页: https://github.com/ahogappa/ryac
- 更新日志: https://github.com/ahogappa/ryac/releases
- RubyGems: https://rubygems.org/gems/ryac

## 历史版本号

- 0.3.0 (2026-09-04)
- 0.2.0 (2026-09-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/ryac
- gem 安装: `gem install ryac`
- Bundler: `gem "ryac"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/ryac-0.3.0.gem
- 版本锁定: `gem "ryac", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
