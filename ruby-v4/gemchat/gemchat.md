# gemchat

**Tag**: web, cli, networking, filesystem

## 简介

gemchat indexes the documentation for the gems in your project's own bundle and
serves BM25 search over it from the command line, with no account, no API key and
no network.

It is a local tool, not the hosted gemchat.org service. An optional mode can defer
to gemchat.org if you would rather not keep a local index.

Direct dependencies are indexed by default and ri documentation is generated
locally, because Bundler installs gems without documentation. Results carry the
exact locked version and real API signatures, which is the point: an agent can
look up how to call a library without reading a 1500-line lockfile into context.

## 官网

- 主页: https://github.com/zoras/gemchat
- 更新日志: https://github.com/zoras/gemchat/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/gemchat

## 历史版本号

- 0.1.0 (2026-10-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/gemchat
- gem 安装: `gem install gemchat`
- Bundler: `gem "gemchat"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/gemchat-0.1.0.gem
- 版本锁定: `gem "gemchat", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
