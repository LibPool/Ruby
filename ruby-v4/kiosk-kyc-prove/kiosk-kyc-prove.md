# kiosk-kyc-prove

**Tag**: web, testing

## 简介

kiosk-kyc-prove implements Kiosk::KycProviders::Base against the Prove
anonymizing KYC broker: it opens a verification at the broker's intake,
and accepts only attestations the broker minted for this operator.
Assign an instance to Kiosk.configuration.kyc_provider and kiosk-server
serves request_kyc and the broker's callback.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-kyc-prove/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-kyc-prove

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-kyc-prove
- gem 安装: `gem install kiosk-kyc-prove`
- Bundler: `gem "kiosk-kyc-prove"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-kyc-prove-0.6.1.gem
- 版本锁定: `gem "kiosk-kyc-prove", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
