# lockally

**Tag**: web, testing, security, serialization, networking, data

## 简介

The lockally control plane lets integrators and direct customers manage everything except actual mail data flow (which uses standard JMAP / IMAP / SMTP-submission against the data plane endpoints).  **Authentication.** All `/v1/*` endpoints require a Bearer API key in the `Authorization` header. Keys are formatted `lk_live_<8-char-prefix>_<32-char-secret>`. Generate the first key for a tenant via `cmd/seed`; subsequent keys via `POST /v1/api-keys`.  **Errors.** Failures return [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457) `application/problem+json` documents.  **Scopes.** Each endpoint requires a specific scope on the presented key. Insufficient scope returns `403` with the required scope name in `detail`.

## 官网

- 主页: https://lockally.com
- 文档: https://www.rubydoc.info/gems/lockally/0.1.0
- RubyGems: https://rubygems.org/gems/lockally

## 历史版本号

- 0.1.0 (2026-08-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/lockally
- gem 安装: `gem install lockally`
- Bundler: `gem "lockally"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/lockally-0.1.0.gem
- 版本锁定: `gem "lockally", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
