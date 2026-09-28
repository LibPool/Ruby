# norbelys

**Tag**: web, security, serialization, networking, filesystem, data

## 简介

The **Norbelys API** is a single, predictable REST surface for cold email and outreach — people, senders, programs, and sending all live behind the five patterns below. Developer-first and AI-first: every name is either already invented (Schema.org) or obvious.  ## Authentication  Every request authenticates with an **org-scoped API key**. Create one in **Settings → API keys** and send it as a bearer token:  ```http GET https://api.norbelys.com/v1/people Authorization: Bearer ak_live_… ```  Interactive agents may instead use OAuth 2.1 (see `/auth.md` and the `/.well-known/oauth-protected-resource` metadata).  ## Conventions  - **Base URL** — `https://api.norbelys.com/v1`. - **JSON in, JSON out.** Timestamps are ISO-8601 in UTC. - **Cursor pagination.** List endpoints take `limit` + `cursor` and return   `{ data, hasMore, nextCursor }` (offset-paged tables add `page` + `total`). - **Expansions.** Detail GETs take an `expand[]` query param to inline related   data (e.g. `GET /people/{id}?expand[]=timeline`) instead of extra calls. - **Soft deletes.** Anything that has been used is archived, never hard-deleted —   `DELETE` archives the resource and returns it.  ## Errors  Failures return the same envelope on every 4xx/5xx, with the matching HTTP status:  ```json { "error": { "type": "invalid_request", "code": "invalid_param",             "message": "…", "hint": "…", "doc_url": "…" } } ```  `type` is a broad, machine-routable category derived from the status; `code` is the stable machine contract you branch on (never the human `message`). See the `ApiError` schema.  ## Idempotency  Every `POST` accepts an optional **`Idempotency-Key`** header. Reuse the same key to replay the original result for 24h instead of re-executing — so a retried create can never double-charge or duplicate a record.  ## Rate limits & versioning  Abuse control is enforced at the edge; responses advertise the policy via the `RateLimit-Policy` header, and a `429` carries `Retry-After`. The API is versioned in the URL path (`/v1`). Breaking changes ship under a new version; a retiring surface is announced with `Deprecation` + `Sunset` response headers at least 90 days ahead.

## 官网

- 主页: https://norbelys.com
- 文档: https://www.rubydoc.info/gems/norbelys/0.1.0
- RubyGems: https://rubygems.org/gems/norbelys

## 历史版本号

- 0.1.0 (2026-07-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/norbelys
- gem 安装: `gem install norbelys`
- Bundler: `gem "norbelys"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/norbelys-0.1.0.gem
- 版本锁定: `gem "norbelys", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
