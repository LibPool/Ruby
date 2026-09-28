# mailmate

**Tag**: cli, testing, tooling, filesystem

## 简介

mailmate is a Ruby library and CLI for working with MailMate's on-disk
storage and AppleScript surface. It includes a smart-mailbox filter
engine (lexer/parser/evaluator over MailMate's filter language), readers
for the binary header indexes, and CLI tools for searching, reading,
modifying, and sending mail via MailMate.

Requires macOS with MailMate installed. Some library pieces (parser,
evaluator, fixture-driven tests) work on any platform; the integration
pieces (AppleScript driver, filesystem readers) raise Mailmate::PlatformError
on non-macOS hosts.

## 官网

- 主页: https://github.com/brianmd/mailmate
- 文档: https://github.com/brianmd/mailmate#readme
- 问题追踪: https://github.com/brianmd/mailmate/issues
- RubyGems: https://rubygems.org/gems/mailmate

## 历史版本号

- 2.2.0 (2026-09-05)
- 2.1.0 (2026-08-29)
- 2.0.0 (2026-08-29)
- 1.9.0 (2026-08-19)
- 1.8.1 (2026-08-19)
- 1.8.0 (2026-08-14)
- 1.7.0 (2026-08-11)
- 1.6.0 (2026-07-13)
- 1.5.0 (2026-06-13)
- 1.4.0 (2026-06-06)
- 1.3.0 (2026-06-06)
- 1.2.0 (2026-05-19)
- 1.1.0 (2026-05-19)
- 1.0.0 (2026-05-19)
- 0.2.0 (2026-05-18)
- 0.1.0 (2026-05-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/mailmate
- gem 安装: `gem install mailmate`
- Bundler: `gem "mailmate"`
- 最新版本: 2.2.0
- 最新版归档: https://rubygems.org/downloads/mailmate-2.2.0.gem
- 版本锁定: `gem "mailmate", "~> 2.2.0"`
- 中央仓库: https://rubygems.org/
