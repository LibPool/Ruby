# ruby_timeout_safe

**Tag**: testing

## 简介

ruby-timeout-safe is a Ruby library that provides a safe and reliable timeout
functionality for executing Ruby blocks. It uses Ruby's threading and monotonic
time to ensure that timeouts are enforced even in the presence of blocking operations
or long-running computations.

The gem defines a `RubyTimeoutSafe` module with a `timeout` method that executes a given
Ruby block with a specified timeout duration. If the block execution exceeds the timeout,
a `Timeout::Error` exception is raised.

This implementation leverages Ruby's built-in threading and monotonic time functions to
provide a robust timeout mechanism.

## 官网

- 主页: https://github.com/sebyx07/ruby-timeout-safe
- RubyGems: https://rubygems.org/gems/ruby_timeout_safe

## 历史版本号

- 1.0.1 (2024-08-28)
- 1.0.0 (2024-08-27)
- 0.2.0 (2024-07-05)
- 0.1.0 (2024-07-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruby_timeout_safe
- gem 安装: `gem install ruby_timeout_safe`
- Bundler: `gem "ruby_timeout_safe"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/ruby_timeout_safe-1.0.1.gem
- 版本锁定: `gem "ruby_timeout_safe", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
