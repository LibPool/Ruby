# rubocop-hash_inspect

**Tag**: testing

## 简介

A RuboCop cop that statically detects Ruby code relying on the pre-Ruby 3.4
Hash#inspect output format (e.g. {:sym=>1}). Ruby 3.4 changed Hash#inspect to
produce {sym: 1, "str" => 2}, breaking tests that hardcode the old format.
Run as part of `pdk validate` to catch incompatibilities before upgrading to
Puppet 9 (Ruby 4).

## 官网

- 主页: https://github.com/puppetlabs/rubocop-hash_inspect
- 更新日志: https://github.com/puppetlabs/rubocop-hash_inspect/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/puppetlabs/rubocop-hash_inspect/issues
- RubyGems: https://rubygems.org/gems/rubocop-hash_inspect

## 历史版本号

- 0.2.0 (2026-06-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/rubocop-hash_inspect
- gem 安装: `gem install rubocop-hash_inspect`
- Bundler: `gem "rubocop-hash_inspect"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/rubocop-hash_inspect-0.2.0.gem
- 版本锁定: `gem "rubocop-hash_inspect", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
