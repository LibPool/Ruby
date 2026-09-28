# sessions

**Tag**: web, cli, security, template, filesystem

## 简介

sessions gives any Rails 8+ app a GitHub-style "your devices" page (list every active session, log out of one device, sign out everywhere else) plus an admin-grade, append-only trail of every login attempt — successful and failed — with parsed device intelligence ("Chrome on macOS", "MyApp 2.4.1 on Pixel 8 (Android 16)"), IP geolocation (via the trackdown gem, soft dependency), and the auth method that started each session (password, OAuth provider, passkey, magic link…). It decorates the session storage your app already has instead of replacing it: on Rails 8 omakase auth (`rails generate authentication`) it enriches the generated sessions table with zero app-code changes, and on Devise it generalizes the proven session_limitable mechanism into true per-device remote revocation via Warden hooks. It detects Hotwire Native apps (platform, OS version, app version, device model), never breaks login (every tracking path is error-isolated), ships privacy-first defaults (bounded retention with a sweep job, optional IP truncation, no browser fingerprinting or invasive client-side probing — device continuity is one signed first-party cookie, minted only at login), and includes a mountable, i18n'd devices page you can restyle or eject view-by-view like Devise.

## 官网

- 主页: https://github.com/rameerez/sessions
- 文档: https://github.com/rameerez/sessions#readme
- 更新日志: https://github.com/rameerez/sessions/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/rameerez/sessions/issues
- RubyGems: https://rubygems.org/gems/sessions

## 历史版本号

- 0.2.2 (2026-07-06)
- 0.2.0 (2026-06-21)
- 0.1.3 (2026-06-21)
- 0.1.2 (2026-06-16)
- 0.1.1 (2026-06-12)
- 0.1.0 (2026-06-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/sessions
- gem 安装: `gem install sessions`
- Bundler: `gem "sessions"`
- 最新版本: 0.2.2
- 最新版归档: https://rubygems.org/downloads/sessions-0.2.2.gem
- 版本锁定: `gem "sessions", "~> 0.2.2"`
- 中央仓库: https://rubygems.org/
