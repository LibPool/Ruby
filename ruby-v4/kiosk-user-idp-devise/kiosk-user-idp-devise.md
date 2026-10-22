# kiosk-user-idp-devise

**Tag**: web, database, security, filesystem, data

## 简介

kiosk-user-idp-devise is the opt-in user-IdP adapter for Rails
providers that authenticate principals through Devise. Add it to your
Gemfile explicitly — the kiosk-all meta-gem pulls in only kiosk-core
and kiosk-server, so IdP adapters are chosen per provider.

It reads the signed-in user from the request's Warden proxy
(`request.env["warden"].user`) passed by kiosk-server and returns a
{Kiosk::Identity} value object. Covers both Devise paths —
`database_authenticatable` and `omniauthable` — since both populate the
Warden user, so the adapter is agnostic to how the user logged in.

Lockable / confirmable handling comes for free: Devise's
`active_for_authentication?` already gates the Warden user, so a locked
or unconfirmed user yields no signed-in user and the request fails as
unauthenticated with no extra code.

No hard runtime dependency on Devise itself — the adapter only reads the
request's Warden user, so the provider's already-installed Devise
satisfies the requirement.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-user-idp-devise/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-user-idp-devise

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-user-idp-devise
- gem 安装: `gem install kiosk-user-idp-devise`
- Bundler: `gem "kiosk-user-idp-devise"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-user-idp-devise-0.6.1.gem
- 版本锁定: `gem "kiosk-user-idp-devise", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
