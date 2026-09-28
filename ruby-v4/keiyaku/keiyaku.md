# keiyaku

**Tag**: web, cli, testing, serialization

## 简介

Generates Ruby clients from OpenAPI documents that carry only what is
specific to one API — an operation table and the schema fields. Transport,
parameter serialization, casting and error mapping live in a shared
runtime, so a nineteen-operation client is about seventy lines. A schema
becomes a frozen value type with RBS emitted beside it, so terse Ruby
costs nothing in tooling. Constructs it cannot translate faithfully are
refused at generation time rather than emitted as plausible guesses.

## 官网

- 主页: https://github.com/onyxblade/keiyaku
- 更新日志: https://github.com/onyxblade/keiyaku/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/keiyaku

## 历史版本号

- 0.1.0 (2026-07-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/keiyaku
- gem 安装: `gem install keiyaku`
- Bundler: `gem "keiyaku"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/keiyaku-0.1.0.gem
- 版本锁定: `gem "keiyaku", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
