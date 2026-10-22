# valid_email_checker

**Tag**: web, networking

## 简介

valid_email_checker embeds the Rust crate check-if-email-exists and exposes
it to Ruby as a native extension. It validates syntax, looks up MX records,
holds an SMTP conversation with the recipient's mail exchanger, and reports
disposable, role-based and catch-all addresses -- all in-process, with no
HTTP service to run and no mail actually sent.

## 官网

- 主页: https://github.com/johncallahan/valid_email_checker
- 更新日志: https://github.com/johncallahan/valid_email_checker/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/johncallahan/valid_email_checker/issues
- RubyGems: https://rubygems.org/gems/valid_email_checker

## 历史版本号

- 0.1.0 (2026-09-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/valid_email_checker
- gem 安装: `gem install valid_email_checker`
- Bundler: `gem "valid_email_checker"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/valid_email_checker-0.1.0.gem
- 版本锁定: `gem "valid_email_checker", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
