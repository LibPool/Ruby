# kiosk-server

**Tag**: web, cli, database, testing, security, serialization, tooling, filesystem

## 简介

kiosk-server is the host-side surface for Kiosk. The full surface ships:

  - The controllers — the per-verb wire (GET <endpoint>/<query-name>,
    POST <endpoint>/<action-name>) and the reserved endpoints
    (/kiosk/schema, /kiosk/pay), a derived OpenAPI description of both,
    OAuth client registration (RFC 7591) and the token endpoint
    (private_key_jwt client assertions, DPoP), JWKS, the KYC
    attestation endpoint, agents.txt / agents.json / kiosk.json
    discovery, and the account-binding ceremony (RFC 8628 device
    authorization and token poll, the verify and «Link an assistant»
    pages).
  - Kiosk::Server::Executor — dispatches a resolved command to the
    queries and actions the host registered.
  - Client registration and authentication, with a pluggable agent-IdP.
  - The PoW gate that enforces a kiosk-reputation policy's challenge
    (soft dependency; zero overhead when no policy is set).
  - A Rack middleware injecting the Kiosk-Server-Version /
    Kiosk-API-Version / Kiosk-Min-Client response headers, a pure-Ruby
    builder for the discovery documents, SQL generators for the
    canonical schema migrations, and a `kiosk:install` generator that
    lays down the initializer and the migrations.

The Rails engine serves that whole surface from one `kiosk` block in
config/routes.rb, which mounts it at Kiosk.configuration.mount_path —
drawing the wire/auth/JWKS/KYC/binding routes under the mount and
installing the root-relative discovery routes (agents.txt, .well-known)
into the host — then one route per query and action the block names. It
also auto-injects the headers middleware.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-server/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-server

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-server
- gem 安装: `gem install kiosk-server`
- Bundler: `gem "kiosk-server"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-server-0.6.1.gem
- 版本锁定: `gem "kiosk-server", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
