# ruby-test-ide

**Tag**: web, testing, serialization, networking, filesystem

## 简介

ruby-test-ide serves a browser IDE for any Ruby project. Note: Still a work in progress
Instead of static analysis or type-annotation files, it evaluates your code in sandboxed
workers and asks the live objects what they can do (irb-style completion,
hover docs via ri, per-line debugger annotations, go-to-definition from
Method#source_location). For code paths the buffer can't safely execute —
network calls, mocked edges — it runs your test suite (any framework, via
.ruby_ide.yaml) with a TracePoint observer preloaded and learns the
argument/return types your code really used.

## 官网

- 主页: https://github.com/SamuelGarrattIqa/ruby-test-ide
- 文档: https://www.rubydoc.info/gems/ruby-test-ide/0.1.0
- RubyGems: https://rubygems.org/gems/ruby-test-ide

## 历史版本号

- 0.1.0 (2026-07-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruby-test-ide
- gem 安装: `gem install ruby-test-ide`
- Bundler: `gem "ruby-test-ide"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/ruby-test-ide-0.1.0.gem
- 版本锁定: `gem "ruby-test-ide", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
