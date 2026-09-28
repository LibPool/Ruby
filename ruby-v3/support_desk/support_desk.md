# support_desk

**Tag**: web, cli, template, tooling

## 简介

support_desk adds a customer support desk to any Rails app: tickets that are conversations. A requester asks for help about something in your app (a ride, an order, a withdrawal) or about nothing in particular, your desk answers, humans sign the answers, and your team works a queue — alongside AI agents that are first-class citizens of the desk: an assistant has a seat, a name, a turn budget and a level (observe, draft, reply, resolve) enforced inside every transition; she proposes replies a person sends, or answers herself where you let her, hands off when unsure, and can never touch a human-held case, a capped topic or a customer who asked for a person. The gem ships the policy, the drafts and review, the turn that makes a late model answer harmless, disclosure and the two exits — and no LLM: any provider, any prompt, in a ten-line job. It is a product gem on the `chats` kernel: chats owns the transcript, realtime, attachments, read state and moderation; support_desk owns cases, topics, assignment, routing and the console API. One macro makes a model ask for help (`has_support_tickets`), one makes a domain record something to ask about (`supportable`), one makes a person answer (`acts_as_support_agent`). Topics are a tree defined in code that drives the wizard, the picker, routing and metrics; assignment is a history, not a column; every transition writes an append-only event row and emits an error-isolated event your app can subscribe to. Batteries included on the user side (a mountable engine with ejectable views), bring-your-own-UI on the agent side (query objects, presenters, a controller concern and a console generator), with no runtime dependency on any admin framework.

## 官网

- 主页: https://github.com/rameerez/support_desk
- 文档: https://github.com/rameerez/support_desk#readme
- 更新日志: https://github.com/rameerez/support_desk/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/rameerez/support_desk/issues
- RubyGems: https://rubygems.org/gems/support_desk

## 历史版本号

- 0.3.2 (2026-09-24)
- 0.3.0 (2026-09-19)
- 0.2.0 (2026-09-18)
- 0.1.3 (2026-09-17)
- 0.1.2 (2026-09-16)
- 0.1.1 (2026-09-16)
- 0.1.0 (2026-09-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/support_desk
- gem 安装: `gem install support_desk`
- Bundler: `gem "support_desk"`
- 最新版本: 0.3.2
- 最新版归档: https://rubygems.org/downloads/support_desk-0.3.2.gem
- 版本锁定: `gem "support_desk", "~> 0.3.2"`
- 中央仓库: https://rubygems.org/
