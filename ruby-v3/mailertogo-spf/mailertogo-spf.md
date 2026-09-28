# mailertogo-spf

**Tag**: web

## 简介

An SPF engine that follows include:/redirect= chains, stops at the first
matching mechanism, and counts DNS-querying terms against RFC 7208 §4.6.4's
cap of 10 — so it agrees with what real receivers do instead of
string-matching a token. It also plans the record a domain should publish:
given what is already at the name, merge one include into the existing
record rather than adding a second v=spf1 record beside it. And it prices a
record: what the whole tree costs a receiver that evaluates all of it, term
by term, against the same cap. No Rails, no runtime dependencies, injectable
DNS resolver.

## 官网

- 主页: https://github.com/aluminumio/mailertogo-spf
- 更新日志: https://github.com/aluminumio/mailertogo-spf/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/aluminumio/mailertogo-spf/issues
- RubyGems: https://rubygems.org/gems/mailertogo-spf

## 历史版本号

- 0.2.1 (2026-08-17)
- 0.2.0 (2026-08-17)
- 0.1.0 (2026-08-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/mailertogo-spf
- gem 安装: `gem install mailertogo-spf`
- Bundler: `gem "mailertogo-spf"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/mailertogo-spf-0.2.1.gem
- 版本锁定: `gem "mailertogo-spf", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
