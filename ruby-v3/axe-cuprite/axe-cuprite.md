# axe-cuprite

**Tag**: web, testing, template

## 简介

axe-cuprite runs the axe-core accessibility engine against pages rendered in
Capybara system/feature tests and exposes the results as RSpec matchers
(be_axe_clean / be_accessible). Unlike Deque's official axe-core-capybara gem,
it never touches Selenium-specific driver internals: axe is driven entirely
through Capybara's driver-neutral JavaScript API, which is what makes it work
on Cuprite. Cuprite is the only supported and tested driver.

## 官网

- 主页: https://github.com/Guided-Rails/axe-cuprite
- 文档: https://github.com/Guided-Rails/axe-cuprite/blob/main/README.md
- 更新日志: https://github.com/Guided-Rails/axe-cuprite/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/Guided-Rails/axe-cuprite/issues
- RubyGems: https://rubygems.org/gems/axe-cuprite

## 历史版本号

- 1.0.0 (2026-06-16)
- 0.2.0 (2026-06-10)
- 0.1.1 (2026-06-09)
- 0.1.0 (2026-06-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/axe-cuprite
- gem 安装: `gem install axe-cuprite`
- Bundler: `gem "axe-cuprite"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/axe-cuprite-1.0.0.gem
- 版本锁定: `gem "axe-cuprite", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
