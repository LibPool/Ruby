# canoser

**Tag**: testing, security, serialization, networking, data

## 简介

A ruby implementation of the canonical serialization for the Libra network. Canonical serialization guarantees byte consistency when serializing an in-memory data structure. It is useful for situations where two parties want to efficiently compare data structures they independently maintain. It happens in consensus where independent validators need to agree on the state they independently compute. A cryptographic hash of the serialized data structure is what ultimately gets compared. In order for this to work, the serialization of the same data structures must be identical when computed by independent validators potentially running different implementations of the same spec in different languages.

## 官网

- 主页: https://github.com/yuan-xy/canoser-ruby.git
- 更新日志: https://github.com/yuan-xy/canoser-ruby/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/canoser

## 历史版本号

- 0.2.1 (2019-10-06)
- 0.1.3 (2019-09-04)
- 0.1.2 (2019-09-02)
- 0.1.1 (2019-08-30)
- 0.1.0 (2019-08-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/canoser
- gem 安装: `gem install canoser`
- Bundler: `gem "canoser"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/canoser-0.2.1.gem
- 版本锁定: `gem "canoser", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
