# rem2ics

**Tag**: template, tooling, filesystem

## 简介

Rem2ics turns the reminder files used by Remind into iCalendar, the format
Outlook, Apple Calendar and Google Calendar import.

It does not parse the reminder language. Remind does: rem2ics is built on
the remind-rb bindings, so the trigger is parsed by ParseRem, the dates it
fires on come from ComputeTrigger, and the message is rendered by DoSubst
with its substitutions expanded. A recurring reminder becomes one event
with an RRULE -- but only when the RRULE has been expanded and checked
against the dates Remind gives; when the two disagree, as they do for a
reminder that skips holidays, the event carries Remind's dates instead.

## 官网

- 主页: https://dianne.skoll.ca/projects/remind/
- 文档: https://www.rubydoc.info/gems/rem2ics/0.1.0
- RubyGems: https://rubygems.org/gems/rem2ics

## 历史版本号

- 0.1.0 (2026-08-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/rem2ics
- gem 安装: `gem install rem2ics`
- Bundler: `gem "rem2ics"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/rem2ics-0.1.0.gem
- 版本锁定: `gem "rem2ics", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
