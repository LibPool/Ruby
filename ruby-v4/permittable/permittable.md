# permittable

**Tag**: database, template, devops, data

## 简介

Strong parameters answer only which keys may pass. A Permittable contract also says what each field should be: it casts the value to a declared type, validates bounds and formats, applies defaults, and renders every failure as a 422 that names the offending parameter. Because a contract is class-level data rather than code inside the action, it can also be checked against the database when the controller loads, so a column dropped by a migration fails the deploy instead of the request. activesupport is the only runtime dependency.

## 官网

- 主页: https://github.com/VSN2015/permittable
- 更新日志: https://github.com/VSN2015/permittable/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/permittable

## 历史版本号

- 0.9.0 (2026-09-27)
- 0.8.0 (2026-09-19)
- 0.7.0 (2026-09-16)
- 0.6.0 (2026-09-07)
- 0.5.2 (2026-09-06)
- 0.5.1 (2026-09-02)
- 0.5.0 (2026-09-02)
- 0.4.0 (2026-09-01)
- 0.3.0 (2026-09-01)
- 0.2.0 (2026-08-18)
- 0.1.2 (2026-08-16)
- 0.1.1 (2026-08-16)
- 0.1.0 (2026-08-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/permittable
- gem 安装: `gem install permittable`
- Bundler: `gem "permittable"`
- 最新版本: 0.9.0
- 最新版归档: https://rubygems.org/downloads/permittable-0.9.0.gem
- 版本锁定: `gem "permittable", "~> 0.9.0"`
- 中央仓库: https://rubygems.org/
