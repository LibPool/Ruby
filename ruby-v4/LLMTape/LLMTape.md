# LLMTape

**Tag**: web, cli, testing, serialization

## 简介

It wraps any LLM client with a tiny DSL. In test environement, it records “tapes” (YAML fixtures of real LLM calls) and replays them on subsequent runs; when a tape is stale, it re-records to keep tests current. Production stays clean and safe, while CI avoids hammering the API every run--yielding deterministic tests, faster pipelines, and fewer tokens spent.

## 官网

- 主页: https://github.com/amitleshed/LLMTape
- RubyGems: https://rubygems.org/gems/LLMTape

## 历史版本号

- 0.6.0 (2025-09-01)
- 0.4.0 (2025-09-01)
- 0.3.0 (2025-09-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/LLMTape
- gem 安装: `gem install LLMTape`
- Bundler: `gem "LLMTape"`
- 最新版本: 0.6.0
- 最新版归档: https://rubygems.org/downloads/LLMTape-0.6.0.gem
- 版本锁定: `gem "LLMTape", "~> 0.6.0"`
- 中央仓库: https://rubygems.org/
