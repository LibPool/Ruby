# chats

**Tag**: web, testing, security, template, tooling

## 简介

chats is a drop-in gem to add chat messaging to your Rails app. It implements a real-time messaging engine for Ruby on Rails 8+ apps: direct messages (DMs), group chats, image attachments, emoji reactions, read receipts, unread badges, and typing indicators. All rendered server-side and updated live with Hotwire (Turbo Streams over Action Cable), so it ships with zero custom JavaScript build steps and works with importmaps out of the box. Any model can converse via a single `acts_as_messager` macro (users, organizations, support agents — participants are polymorphic), conversations can be optionally attached to any domain record via `acts_as_chat_subject` (so users can chat about a specific order, a listing, a booking), and the whole inbox UI is overridable view-by-view like Devise. It exposes small adapter seams a blocked-users lookup, a `can_message` policy, and a notifier hook; so it snaps onto the `moderate` gem for Trust & Safety (report/block/filter, DSA + app-store compliance) and onto any notification system (like the `noticed` gem) without any hard dependencies. Messages support soft deletion, editing, system messages posted by your app, per-sender rate limiting, and optional encryption at rest.

## 官网

- 主页: https://github.com/rameerez/chats
- 文档: https://github.com/rameerez/chats#readme
- 更新日志: https://github.com/rameerez/chats/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/rameerez/chats/issues
- RubyGems: https://rubygems.org/gems/chats

## 历史版本号

- 0.3.2 (2026-09-17)
- 0.3.1 (2026-09-16)
- 0.2.0 (2026-09-16)
- 0.1.1 (2026-06-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/chats
- gem 安装: `gem install chats`
- Bundler: `gem "chats"`
- 最新版本: 0.3.2
- 最新版归档: https://rubygems.org/downloads/chats-0.3.2.gem
- 版本锁定: `gem "chats", "~> 0.3.2"`
- 中央仓库: https://rubygems.org/
