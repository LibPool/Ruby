# imap_processor

**Tag**: web, cli, testing, security, filesystem

## 简介

IMAPProcessor is a client for processing messages on an IMAP server.  It
provides some basic mechanisms for connecting to an IMAP server, determining
capabilities and handling messages.

IMAPProcessor ships with several executables which can query and
manipulate IMAP mailboxes in several different ways:

imap_archive  :: Archives old messages to a new dated mailbox.
imap_cleanse  :: Delete messages older than a certain age in specified mailboxes.
imap_tidy     :: Archive + Cleanse: Moves older messages to a dated mailbox.
imap_flag     :: Flag messages to/from certain people.
imap_idle     :: Shows new messages in a mailbox.
imap_keywords :: Queries an IMAP server for keywords set on messages
imap_learn    :: Flags messages based on what you've flagged before.
imap_mkdir    :: Ensures that certain mailboxes exist.

== Features/Problems:

* Connection toolkit
* Executable toolkit
* Only known to work with SASL/PLAIN authentication

## 官网

- 主页: https://github.com/seattlerb/imap_processor
- 文档: http://docs.seattlerb.org/imap_processor
- RubyGems: https://rubygems.org/gems/imap_processor

## 历史版本号

- 1.9.1 (2026-09-19)
- 1.9.0 (2025-09-09)
- 1.8.1 (2023-07-27)
- 1.8.0 (2023-01-09)
- 1.7 (2020-06-04)
- 1.6 (2014-10-17)
- 1.5 (2014-08-07)
- 1.3 (2009-08-05)
- 1.2 (2009-08-05)
- 1.1.1 (2009-07-25)
- 1.1 (2009-07-25)
- 1.0.1 (2009-07-25)
- 1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/imap_processor
- gem 安装: `gem install imap_processor`
- Bundler: `gem "imap_processor"`
- 最新版本: 1.9.1
- 最新版归档: https://rubygems.org/downloads/imap_processor-1.9.1.gem
- 版本锁定: `gem "imap_processor", "~> 1.9.1"`
- 中央仓库: https://rubygems.org/
