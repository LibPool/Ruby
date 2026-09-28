# hitch-rails

**Tag**: web, cli, database, testing, security, filesystem, data

## 简介

Hitch lets MCP clients -- Claude, ChatGPT, Cursor -- call your Rails
app's tools as a specific signed-in user, with access you can revoke.

You do not stand up a separate auth server, add Redis, or adopt a new
sign-in system. Hitch uses the authentication your app already has
(current_user or Current.user) and your configured cache store.

Underneath it is a full OAuth 2.1 authorization server implementing the
MCP 2026-07-28 authorization profile: PKCE (S256), audience-bound tokens
(RFC 8707), discovery metadata (RFC 8414 + RFC 9728), revocation
(RFC 7009), Client ID Metadata Documents, and optional Dynamic Client
Registration (RFC 7591). It adds an authenticated /mcp endpoint backed by
the official Ruby MCP SDK and a deny-default tool registry with schema
validation and size caps. SQLite and PostgreSQL supported.

## 官网

- 主页: https://hitch-rails.com
- 源码仓库: https://github.com/tylerklose/hitch-rails
- 文档: https://github.com/tylerklose/hitch-rails/blob/v0.5.0/docs/public_api/0.5.0.md
- 更新日志: https://github.com/tylerklose/hitch-rails/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/tylerklose/hitch-rails/issues
- RubyGems: https://rubygems.org/gems/hitch-rails

## 历史版本号

- 0.5.0 (2026-09-05)
- 0.4.0 (2026-08-25)
- 0.3.0 (2026-08-22)
- 0.2.0 (2026-08-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/hitch-rails
- gem 安装: `gem install hitch-rails`
- Bundler: `gem "hitch-rails"`
- 最新版本: 0.5.0
- 最新版归档: https://rubygems.org/downloads/hitch-rails-0.5.0.gem
- 版本锁定: `gem "hitch-rails", "~> 0.5.0"`
- 中央仓库: https://rubygems.org/
