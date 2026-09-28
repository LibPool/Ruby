# minitest-coverage

**Tag**: testing, security, data

## 简介

Ruby's contemporary test coverage tools all lie, exaggerating coverage
through false-positives and creating a false sense of security;
minitest-coverage tries to address this.

Coverage Analysis Tools rely on tracing facilities built into ruby’s
VM. You run your tests, and collect data. Seems simple, but that’s a
very flawed approach that buffers your coverage numbers up falsely.
I’ve witnessed false coverage by as much as 60%, but it could be even
worse. Worse, the tracing facilities currently make it impossible to
get truly accurate numbers. Even so, they can be improved to be much
more accurate.

## 官网

- 主页: https://github.com/seattlerb/minitest-coverage
- RubyGems: https://rubygems.org/gems/minitest-coverage

## 历史版本号

- 1.0.0.b3 (2026-01-12)
- 1.0.0.b2 (2017-05-09)
- 1.0.0.b1 (2016-11-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/minitest-coverage
- gem 安装: `gem install minitest-coverage`
- Bundler: `gem "minitest-coverage"`
- 最新版本: 1.0.0.b3
- 最新版归档: https://rubygems.org/downloads/minitest-coverage-1.0.0.b3.gem
- 版本锁定: `gem "minitest-coverage", "~> 1.0.0.b3"`
- 中央仓库: https://rubygems.org/
