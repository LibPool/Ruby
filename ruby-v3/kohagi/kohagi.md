# kohagi

**Tag**: serialization, tooling

## 简介

Drives the kohagi binary's stdin/stdout JSONL protocol from Ruby: builds the
command, spawns it without deadlocking on the pipe buffer, maps exit codes to
outcomes, and returns id-tagged embeddings. Shells out to an installed kohagi
binary and ships no native code of its own.

## 官网

- 主页: https://github.com/takahashim/kohagi-ruby
- 更新日志: https://github.com/takahashim/kohagi-ruby/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/kohagi

## 历史版本号

- 0.1.0 (2026-07-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/kohagi
- gem 安装: `gem install kohagi`
- Bundler: `gem "kohagi"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/kohagi-0.1.0.gem
- 版本锁定: `gem "kohagi", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
