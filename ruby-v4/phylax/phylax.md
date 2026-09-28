# phylax

**Tag**: web, security

## 简介

phylax (Greek "guardian") is a thin, safe-by-default binding to the Windows
Cryptography API: Next Generation (CNG / bcrypt.dll) and DPAPI. It does not
implement any cryptography of its own — it exposes the operating system's own
validated primitives through an ergonomic, hard-to-misuse Ruby API: a
cryptographically secure RNG, SHA-2 hashing and HMAC (one-shot and streaming),
PBKDF2 key derivation, authenticated AES-256-GCM encryption (SecretBox, with
nonces generated and framed automatically so reuse is impossible), a
constant-time comparison, and DPAPI protect/unprotect for secrets at rest.
Windows MSVC (mswin) Ruby only.

## 官网

- 主页: https://github.com/main-path/phylax
- 更新日志: https://github.com/main-path/phylax/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/phylax/issues
- RubyGems: https://rubygems.org/gems/phylax

## 历史版本号

- 0.1.0 (2026-06-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/phylax
- gem 安装: `gem install phylax`
- Bundler: `gem "phylax"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/phylax-0.1.0.gem
- 版本锁定: `gem "phylax", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
