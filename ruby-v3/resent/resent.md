# resent

**Tag**: web, cli, serialization, networking, template, filesystem

## 简介

Resent is the official Ruby client for resent.one — a transactional email API built for product and platform teams.

Install with: gem install resent  (or add gem "resent" to your Gemfile).

Create an API key in the Resent dashboard, set RESENT_API_KEY, then send mail with a few lines of Ruby:

  require "resent"
  resent = Resent.new(ENV.fetch("RESENT_API_KEY"))
  resent.emails.send(
    from: "Acme <noreply@yourdomain.com>",
    to: "you@example.com",
    subject: "Hello World",
    html: "<strong>It works!</strong>"
  )

Uses only Ruby stdlib (Net::HTTP + JSON) — no extra runtime gems. Supports html and/or text bodies, plus cc, bcc, and reply_to.

Docs: https://developers.resent.one/sdks/ruby
Dashboard: https://resent.one
Source: https://github.com/resentmail/resent-ruby

## 官网

- 主页: https://resent.one
- 源码仓库: https://github.com/resentmail/resent-ruby
- 文档: https://developers.resent.one/sdks/ruby
- 问题追踪: https://github.com/resentmail/resent-ruby/issues
- RubyGems: https://rubygems.org/gems/resent

## 历史版本号

- 0.1.3 (2026-07-26)
- 0.1.2 (2026-07-26)
- 0.1.1 (2026-07-26)
- 0.1.0 (2026-07-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/resent
- gem 安装: `gem install resent`
- Bundler: `gem "resent"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/resent-0.1.3.gem
- 版本锁定: `gem "resent", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
