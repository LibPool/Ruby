# rodauth

**Tag**: web, database, security, serialization, template, data

## 简介

Rodauth is Ruby's most advanced authentication framework, designed
to work in all rack applications.  It's built using Roda and Sequel,
but it can be used as middleware in front of web applications that use
other web frameworks and database libraries.

Rodauth aims to provide strong security for password storage by
utilizing separate database accounts if possible on PostgreSQL,
MySQL, and Microsoft SQL Server.  Configuration is done via
a DSL that makes it easy to override any part of the authentication
process.

Rodauth supports typical authentication features: such as login and
logout, changing logins and passwords, and creating, verifying,
unlocking, and resetting passwords for accounts.  Rodauth also
supports many advanced authentication features:

* Secure password storage using security definer database functions
* Multiple primary multifactor authentication methods (WebAuthn and
  TOTP), as well as backup multifactor authentication methods (SMS
  and recovery codes).
* Passwordless authentication using email links and WebAuthn
  authenticators.
* Both standard HTML form and JSON API support for all features.

## 官网

- 主页: https://rodauth.jeremyevans.net
- 源码仓库: https://github.com/jeremyevans/rodauth
- 文档: https://rodauth.jeremyevans.net/documentation.html
- 更新日志: https://rodauth.jeremyevans.net/rdoc/files/CHANGELOG.html
- 问题追踪: https://github.com/jeremyevans/rodauth/issues
- RubyGems: https://rubygems.org/gems/rodauth

## 历史版本号

- 2.48.0 (2026-09-24)
- 2.47.0 (2026-08-24)
- 2.46.0 (2026-08-19)
- 2.45.0 (2026-07-24)
- 2.44.0 (2026-06-08)
- 2.43.0 (2026-03-20)
- 2.42.0 (2025-12-18)
- 2.41.0 (2025-10-08)
- 2.40.0 (2025-08-22)
- 2.39.0 (2025-05-22)
- 2.38.0 (2025-01-15)
- 2.37.0 (2024-11-19)
- 2.36.0 (2024-07-23)
- 2.35.0 (2024-05-28)
- 2.34.0 (2024-03-22)
- 2.33.0 (2023-12-21)
- 2.32.0 (2023-10-23)
- 2.31.0 (2023-08-22)
- 2.30.0 (2023-05-22)
- 2.29.0 (2023-03-22)
- 2.28.0 (2023-02-22)
- 2.27.0 (2023-01-24)
- 2.26.1 (2022-11-08)
- 2.26.0 (2022-10-21)
- 2.25.0 (2022-06-22)
- 2.24.0 (2022-05-24)
- 2.23.0 (2022-04-22)
- 2.22.0 (2022-03-22)
- 2.21.0 (2022-02-23)
- 2.20.0 (2022-01-24)
- 2.19.0 (2021-12-22)
- 2.18.0 (2021-11-23)
- 2.17.0 (2021-09-24)
- 2.16.0 (2021-08-23)
- 2.15.0 (2021-07-27)
- 2.14.0 (2021-06-22)
- 2.13.0 (2021-05-23)
- 2.12.0 (2021-04-22)
- 2.11.0 (2021-03-22)
- 2.10.0 (2021-02-22)
- 2.9.0 (2021-01-23)
- 2.8.0 (2021-01-06)
- 2.7.0 (2020-12-22)
- 2.6.0 (2020-11-20)
- 2.5.0 (2020-10-22)
- 2.4.0 (2020-09-21)
- 2.3.0 (2020-08-21)
- 2.2.0 (2020-07-20)
- 2.1.0 (2020-06-09)
- 2.0.0 (2020-05-06)
- 1.23.0 (2020-03-06)
- 1.22.0 (2019-10-29)
- 1.21.0 (2019-07-24)
- 1.20.0 (2019-06-07)
- 1.19.1 (2018-11-16)
- 1.19.0 (2018-11-16)
- 1.18.0 (2018-07-18)
- 1.17.0 (2018-06-11)
- 1.16.0 (2018-03-09)
- 1.15.0 (2018-01-29)
- 1.14.0 (2017-12-19)
- 1.13.0 (2017-11-21)
- 1.12.0 (2017-10-03)
- 1.11.0 (2017-04-24)
- 1.10.0 (2017-03-23)
- 1.9.0 (2017-02-23)
- 1.8.0 (2017-01-06)
- 1.7.0 (2016-11-22)
- 1.6.0 (2016-10-24)
- 1.5.0 (2016-09-22)
- 1.4.0 (2016-08-18)
- 1.3.0 (2016-07-19)
- 1.2.0 (2016-06-15)
- 1.1.0 (2016-05-13)
- 1.0.0 (2016-04-15)
- 0.10.0 (2016-02-17)
- 0.9.1 (2015-08-13)
- 0.9.0 (2015-08-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/rodauth
- gem 安装: `gem install rodauth`
- Bundler: `gem "rodauth"`
- 最新版本: 2.48.0
- 最新版归档: https://rubygems.org/downloads/rodauth-2.48.0.gem
- 版本锁定: `gem "rodauth", "~> 2.48.0"`
- 中央仓库: https://rubygems.org/
