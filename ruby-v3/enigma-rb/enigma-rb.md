# enigma-rb

**Tag**: web, security

## 简介

Enigma is a lightweight Ruby gem designed to verify passwords hashed using Firebase's custom scrypt-based algorithm, making it ideal for seamless integrations and migrations involving Firebase authentication systems. It provides a secure, efficient way to compare a user-provided password against a stored hash without exposing sensitive details, ensuring constant-time comparisons to mitigate timing attacks.

Key features include:
- Full compatibility with Firebase Authentication's password hashing logic, combining scrypt with AES-256-CTR encryption for signing.
- Configurable parameters for scrypt (rounds, memory cost), signer keys, and salt separators.
- Secure practices using OpenSSL's fixed-length comparisons.
- Support for custom logging, with easy integration into Rails or other frameworks.
- Minimal dependencies, relying on the 'scrypt' gem alongside Ruby's standard library.

A common use case is migrating users from Firebase to systems like Devise in Ruby on Rails. During migration, extract the user's base64-encoded salt and stored hash from Firebase, then use Enigma to verify the input password. If it matches, set the raw password in Devise to generate a new hash, avoiding forced resets and ensuring a smooth transition.

Whether for custom auth systems, password audits, or hybrid setups, Enigma simplifies secure verification while prioritizing ease of use.

## 官网

- 主页: https://github.com/y-dashev/enigma
- 更新日志: https://github.com/y-dashev/enigma/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/enigma-rb

## 历史版本号

- 0.1.0 (2025-11-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/enigma-rb
- gem 安装: `gem install enigma-rb`
- Bundler: `gem "enigma-rb"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/enigma-rb-0.1.0.gem
- 版本锁定: `gem "enigma-rb", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
