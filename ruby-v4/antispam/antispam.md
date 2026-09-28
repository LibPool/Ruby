# antispam

**Tag**: web, database, data

## 简介

Antispam helps prevent spam in your Rails applications by checking against DNS blacklists and spam-prevention databases. It has two core features: (1) IP-based spam detection using Project Honey Pot to block known spammers automatically, and (2) content-based spam detection using Defendium’s machine learning API, which is free for up to 1,000 checks per day. Blacklist lookups are cached for 24 hours to minimize performance impact. The gem integrates seamlessly with Rails, allowing you to block spam at the request level and redirect flagged users to a captcha page.

## 官网

- 主页: https://ryankopf.com
- 源码仓库: https://github.com/ryankopf/antispam
- 更新日志: https://github.com/ryankopf/antispam/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/antispam

## 历史版本号

- 0.3.3 (2025-02-23)
- 0.3.2 (2025-02-23)
- 0.3.1 (2025-02-23)
- 0.3.0 (2025-02-23)
- 0.2.11 (2024-10-29)
- 0.2.10 (2024-10-29)
- 0.2.8 (2024-10-29)
- 0.2.6 (2024-10-29)
- 0.2.5 (2024-10-28)
- 0.2.4 (2024-10-28)
- 0.2.3 (2024-10-28)
- 0.2.0 (2023-01-25)
- 0.1.7 (2023-01-25)
- 0.1.5 (2021-06-26)
- 0.1.4 (2021-01-31)
- 0.1.3 (2021-01-31)
- 0.1.2 (2021-01-31)
- 0.1.1 (2021-01-31)
- 0.1.0 (2021-01-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/antispam
- gem 安装: `gem install antispam`
- Bundler: `gem "antispam"`
- 最新版本: 0.3.3
- 最新版归档: https://rubygems.org/downloads/antispam-0.3.3.gem
- 版本锁定: `gem "antispam", "~> 0.3.3"`
- 中央仓库: https://rubygems.org/
