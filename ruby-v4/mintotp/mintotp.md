# mintotp

**Tag**: web, security

## 简介

TOTP stands for Time-Based One-Time Password. Many websites and services require two-factor authentication (2FA) or multi-factor authentication (MFA) where the user is required to present two or more pieces of evidence:  Something only the user knows, e.g., password, passphrase, etc.  Something only the user has, e.g., hardware token, mobile phone, etc.   Something only the user is, e.g., biometrics.  TOTP stands for Time-Based One-Time Password. Many websites and services require two-factor authentication (2FA) or multi-factor authentication (MFA) where the user is required to present two or more pieces of evidence. A TOTP value serves as the second factor, i.e., it proves that the user is in possession of a device (e.g., mobile phone) that contains a TOTP secret key from which the TOTP value is generated. Usually the service provider that provides a user's account also issues a secret key encoded either as a Base32 string or as a QR code. This secret key is added to an authenticator app (e.g., Google Authenticator) on a mobile device. The app can then generate TOTP values based on the current time. By default, it generates a new TOTP value every 30 seconds.

## 官网

- 主页: https://github.com/winhtaikaung/mintotp-ruby
- 更新日志: https://github.com/winhtaikaung/mintotp-ruby/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/mintotp

## 历史版本号

- 0.1.0 (2022-06-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/mintotp
- gem 安装: `gem install mintotp`
- Bundler: `gem "mintotp"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/mintotp-0.1.0.gem
- 版本锁定: `gem "mintotp", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
