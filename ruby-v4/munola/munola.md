# munola

**Tag**: web, networking, tooling, data

## 简介

The binary this gem fetches is not an enola-labs release. It is a build
cut from https://github.com/misabegovic/enola, a fork of enola, whose
release notes name what differs from upstream release by release; this
gem drives channel release 0.4.19.1, built on enola
0.4.19. Everything else is the enola gem's wrapper,
unchanged: fetched on first use, verified against the checksums the
release publishes, cached per user, every command and exit code
forwarded. Use the enola gem to run stock upstream instead.

What the fork adds: `munola init` writes the recipe catalogue the
enola-guides gem carries (Ember, data ownership, API boundaries,
background work, a tenant foreign key) into the project, binds the
recipes its tree justifies, and turns both Ruby providers on by default.
Under Rails it adds `rails generate munola:install`; the enola:* rake tasks come from enola-rb and drive munola's binary. Offered upstream where it fits;
no binary here, nothing compiled.

## 官网

- 主页: https://github.com/misabegovic/enola-rb
- 更新日志: https://github.com/misabegovic/enola-rb/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/munola

## 历史版本号

- 0.6.3 (2026-09-14)
- 0.6.2 (2026-08-30)
- 0.6.1 (2026-08-24)
- 0.6.0 (2026-08-24)
- 0.5.2 (2026-08-23)
- 0.5.1 (2026-08-23)
- 0.5.0 (2026-08-23)
- 0.4.4.1 (2026-08-23)
- 0.0.0 (2026-08-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/munola
- gem 安装: `gem install munola`
- Bundler: `gem "munola"`
- 最新版本: 0.6.3
- 最新版归档: https://rubygems.org/downloads/munola-0.6.3.gem
- 版本锁定: `gem "munola", "~> 0.6.3"`
- 中央仓库: https://rubygems.org/
