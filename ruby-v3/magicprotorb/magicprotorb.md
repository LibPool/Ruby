# magicprotorb

**Tag**: tooling, filesystem

## 简介

magicprotorb lets you `require "magicprotorb/foo/bar_pb"` and have foo/bar.proto
compiled to descriptors and registered at require time. The dotted require path
mirrors the canonical proto path 1:1, so the require name, the file location, and
the descriptor name can never drift apart. A small Rust extension (built on the
pure-Rust protox compiler) turns .proto text into a FileDescriptorSet, which is
then registered through the stock protobuf DescriptorPool — making the resulting
message classes indistinguishable from generated ones.

## 官网

- 主页: https://github.com/grpyc/magicproto-rb
- RubyGems: https://rubygems.org/gems/magicprotorb

## 历史版本号

- 0.1.0 (2026-05-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/magicprotorb
- gem 安装: `gem install magicprotorb`
- Bundler: `gem "magicprotorb"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/magicprotorb-0.1.0.gem
- 版本锁定: `gem "magicprotorb", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
