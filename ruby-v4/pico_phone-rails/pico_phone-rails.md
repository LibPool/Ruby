# pico_phone-rails

**Tag**: web, serialization

## 简介

pico_phone-rails wires the pico_phone gem into Rails: a :phone_number ActiveRecord attribute type, a PhoneValidator for ActiveModel validations, a normalize_phone class macro that rewrites phone attributes to E.164 before validation, extract_phone_numbers_from for pulling phone numbers out of free text (with an optional persisted backend for cross-record search), maintain_phone_search_index for keeping search columns in sync on an existing phone-number table, pico_phone_field_tag/f.pico_phone_field form helpers that display national format for a valid number without discarding what the user typed, live: true on those same helpers for debounced Stimulus-driven validation and reformatting via a mountable engine, and an ActiveJob serializer so a PhoneNumber survives being passed as a job argument.

## 官网

- 主页: https://github.com/gjack/pico_phone-rails
- 文档: https://rubydoc.info/gems/pico_phone-rails
- 更新日志: https://github.com/gjack/pico_phone-rails/releases
- 问题追踪: https://github.com/gjack/pico_phone-rails/issues
- RubyGems: https://rubygems.org/gems/pico_phone-rails

## 历史版本号

- 0.6.0 (2026-08-08)
- 0.5.0 (2026-08-02)
- 0.4.0 (2026-08-01)
- 0.3.0 (2026-07-26)
- 0.2.1 (2026-07-25)
- 0.2.0 (2026-07-25)
- 0.1.0 (2026-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/pico_phone-rails
- gem 安装: `gem install pico_phone-rails`
- Bundler: `gem "pico_phone-rails"`
- 最新版本: 0.6.0
- 最新版归档: https://rubygems.org/downloads/pico_phone-rails-0.6.0.gem
- 版本锁定: `gem "pico_phone-rails", "~> 0.6.0"`
- 中央仓库: https://rubygems.org/
