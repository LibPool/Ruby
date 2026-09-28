# portage-cli

**Tag**: web, cli, template

## 简介

Ships the `portage` executable. `portage buy <url>` tries native UCP discovery first (zero credentials, works on any store that's opted in), falls back to a portage-ucp-* platform adapter only when this process already has that platform's own credentials in env (i.e. it's your own store or one you're integrated with), and otherwise says so plainly — never scrapes or session-hijacks as an anonymous shopper. `portage find` covers the no-URL case: ask an allowlist, DuckDuckGo, Brave, or a Google Programmable Search engine which stores might sell something, keep the ones answering /.well-known/ucp, and search their catalogs — documented APIs only, no SERP scraping. Depends on portage-ucp (for platform detection via Resolver), portage-ucp-client (for the actual buy calls), and portage-ucp-journal (for `portage-console`'s read-only view of local purchase/transaction/order state); no single adapter gem is a hard dependency. Ranking, escalation and the spend-policy check use portage-ucp core's rules; portage-ucp-decision is optional and only the opt-in confidence gate needs it.

## 官网

- 主页: https://github.com/tomtom87/Portage/tree/main/portage-cli
- 更新日志: https://github.com/tomtom87/Portage/blob/main/portage-cli/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/portage-cli

## 历史版本号

- 0.7.5 (2026-09-25)
- 0.7.4 (2026-09-25)
- 0.7.3 (2026-09-25)
- 0.7.0 (2026-09-23)
- 0.6.4 (2026-09-22)
- 0.6.0 (2026-09-17)
- 0.5.1 (2026-09-16)
- 0.4.1 (2026-09-15)
- 0.4.0 (2026-09-14)
- 0.3.0 (2026-08-28)
- 0.2.0 (2026-08-21)
- 0.1.0 (2026-08-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/portage-cli
- gem 安装: `gem install portage-cli`
- Bundler: `gem "portage-cli"`
- 最新版本: 0.7.5
- 最新版归档: https://rubygems.org/downloads/portage-cli-0.7.5.gem
- 版本锁定: `gem "portage-cli", "~> 0.7.5"`
- 中央仓库: https://rubygems.org/
