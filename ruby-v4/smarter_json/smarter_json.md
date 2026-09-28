# smarter_json

**Tag**: testing, serialization, tooling, filesystem, data

## 简介

A lenient, fast JSON processor for Ruby. It extracts strict JSON, NDJSON, JSONL, JSON5, HJSON-style config, and the messy JSON-ish input humans and LLMs actually write — comments, trailing commas, single / unquoted / smart quotes, Python and JS keywords, a UTF-8 BOM, and more all parse to the same Ruby objects, with no modes or flags to set. Where a traditional parser stops at the first deviation and throws away the whole document, SmarterJSON keeps going — it optimizes for getting your data out, not for policing the JSON spec. It reads multi-document NDJSON / JSONL in one call (and streams it with a block), and in benchmarks its C extension matches or beats Oj on nearly every file. SmarterJSON is opinionated: we want your JSON processing to be successful.

## 官网

- 主页: https://github.com/tilo/smarter_json
- 源码仓库: https://github.com/tilo/smarter_json/tree/main
- 文档: https://github.com/tilo/smarter_json#readme
- 更新日志: https://github.com/tilo/smarter_json/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/tilo/smarter_json/issues
- RubyGems: https://rubygems.org/gems/smarter_json

## 历史版本号

- 1.2.6 (2026-07-03)
- 1.2.5 (2026-07-02)
- 1.2.4 (2026-07-01)
- 1.2.3 (2026-06-28)
- 1.2.2 (2026-06-19)
- 1.2.1 (2026-06-17)
- 1.2.0 (2026-06-16)
- 1.1.2 (2026-06-12)
- 1.1.1 (2026-06-11)
- 1.1.0 (2026-06-09)
- 1.0.0 (2026-06-09)
- 0.9.9 (2026-06-07)
- 0.9.2 (2026-06-03)
- 0.8.0 (2026-06-03)
- 0.7.0 (2026-06-03)
- 0.6.0 (2026-06-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/smarter_json
- gem 安装: `gem install smarter_json`
- Bundler: `gem "smarter_json"`
- 最新版本: 1.2.6
- 最新版归档: https://rubygems.org/downloads/smarter_json-1.2.6.gem
- 版本锁定: `gem "smarter_json", "~> 1.2.6"`
- 中央仓库: https://rubygems.org/
