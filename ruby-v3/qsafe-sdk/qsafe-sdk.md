# qsafe-sdk

**Tag**: web, security, data

## 简介

Post-quantum cryptography SaaS API supporting ML-KEM (Kyber) and ML-DSA (Dilithium) algorithms. Provides keypair management and cryptographic operations (encrypt, decrypt, sign, verify).  ## Authentication - **JWT Bearer Token** — user-based auth, obtained from `/auth/login` or `/auth/register` - **API Key (header)** — programmatic access via `X-API-Key` header - **API Key (query)** — programmatic access via `?api_key=` query parameter  ## Quick Start 1. Register → `POST /auth/register` 2. Login → `POST /auth/login` → copy `data.token` 3. Generate keypair → `POST /generate-keypair` 4. Encrypt / Sign with the keypair ID

## 官网

- 主页: https://openapi-generator.tech
- 文档: https://www.rubydoc.info/gems/qsafe-sdk/1.0.4
- RubyGems: https://rubygems.org/gems/qsafe-sdk

## 历史版本号

- 1.0.4 (2026-05-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/qsafe-sdk
- gem 安装: `gem install qsafe-sdk`
- Bundler: `gem "qsafe-sdk"`
- 最新版本: 1.0.4
- 最新版归档: https://rubygems.org/downloads/qsafe-sdk-1.0.4.gem
- 版本锁定: `gem "qsafe-sdk", "~> 1.0.4"`
- 中央仓库: https://rubygems.org/
