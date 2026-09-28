# fastlane-plugin-pharen

**Tag**: web, cli, networking, tooling

## 简介

Fastlane plugin for Pharen (https://pharen.ai): a thin wrapper over the `pharen` CLI that adds one zero-argument action, pharen_release, after build_app — it registers the release, uploads every dSYM, uploads the build, and returns the OTA install link. Warn-don't-fail by default, so a telemetry step never fails your release build; `strict: true` opts a lane into hard failure where an unsymbolicated release must be a stop.

## 官网

- 主页: https://pharen.ai
- RubyGems: https://rubygems.org/gems/fastlane-plugin-pharen

## 历史版本号

- 0.1.0 (2026-07-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/fastlane-plugin-pharen
- gem 安装: `gem install fastlane-plugin-pharen`
- Bundler: `gem "fastlane-plugin-pharen"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/fastlane-plugin-pharen-0.1.0.gem
- 版本锁定: `gem "fastlane-plugin-pharen", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
