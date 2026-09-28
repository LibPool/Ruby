# session_keys

**Tag**: security

## 简介

SessionKeys is a cryptographic tool for the deterministic generation of
    NaCl compatible Curve25519 encryption and Ed25519 digital signature keys.

    The strength of the system is rooted in the fact that the keypairs are derived from
    passing an identifier, such as a username or email address, and a high-entropy
    passphrase through the SHA256 one-way hash and the scrypt key derivation
    functions. This means that no private key material need ever be writter to
    disk or transmitted. The generated keys are deterministic; for any given ID,
    password, and strength combination the same keys will always be returned.

## 官网

- 主页: https://github.com/grempe/session-keys-rb
- 文档: https://www.rubydoc.info/gems/session_keys/2.0.0
- RubyGems: https://rubygems.org/gems/session_keys

## 历史版本号

- 2.0.0 (2019-08-23)
- 1.0.0 (2016-09-08)
- 0.1.0 (2016-05-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/session_keys
- gem 安装: `gem install session_keys`
- Bundler: `gem "session_keys"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/session_keys-2.0.0.gem
- 版本锁定: `gem "session_keys", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
