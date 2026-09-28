# zippendo

**Tag**: web, cli, security, filesystem

## 简介

Public API documentation for Zippendo. Authenticate using your API token (Bearer token prefixed with zipp_).  **Brands (sub-accounts).** An organization can be split into brands, each keeping its own orders, shipments and configuration separate. There are two ways to scope requests to one brand, and NEITHER changes any request body:  1. **Bind the token.** Create an API token with a `brandId` and every request it makes is confined    to that brand — reads filtered, writes stamped. This is the recommended way to give a single    brand's team its own credential. 2. **Send the `X-Zippendo-Brand` header.** An organization-wide token can scope an individual    request by sending the brand's id or slug in this header. Most SDKs let you set it once on the    client so every call inherits it.  A brand-bound token that receives an `X-Zippendo-Brand` header naming a different brand is rejected with `403 BRAND_ACCESS_DENIED` — the binding is never widened. Omit both and requests cover the whole organization, which is the behaviour of every existing token.  Records that belong to no brand carry `brandId: null`. Configuration (carriers, shipping rules, addresses) with a null brand is organization-wide and remains visible inside every brand; orders and shipments with a null brand are only visible organization-wide.  List endpoints additionally take a `?brandScope=own|shared|both` parameter to narrow further within whichever brand context already applies. `own` returns only rows assigned to that brand, and requires a brand context — a brand-bound token, a resolved brand session, or the `X-Zippendo-Brand` header above — otherwise `400`. `shared` returns only the organization-wide rows (equivalent to filtering `brandId=none`). The default, `both`, keeps the existing behaviour: a brand context sees its own rows plus the organization-wide ones. Set `X-Zippendo-Brand-Scope` as a client default to apply the same choice to every request instead of repeating the query parameter on each call — an explicit `brandScope` query parameter always wins over the header, and a blank header value is ignored.  Brands themselves are managed under the **Brands** tag. Retiring a brand is done with `POST /orgs/{orgId}/brands/{brandId}/archive` — permanent deletion is a dashboard-only action, since it is refused while any order, shipment, member or token still references the brand. Brands require a plan that includes them; creating one beyond your plan's limit returns `403`.

## 官网

- 主页: https://www.zippendo.com
- 文档: https://www.rubydoc.info/gems/zippendo/1.3.4
- RubyGems: https://rubygems.org/gems/zippendo

## 历史版本号

- 1.3.4 (2026-09-22)
- 1.3.3 (2026-09-21)
- 1.3.2 (2026-09-16)
- 1.3.1 (2026-09-15)
- 1.3.0 (2026-09-14)
- 1.2.7 (2026-09-10)
- 1.2.6 (2026-09-09)
- 1.2.5 (2026-09-02)
- 1.2.4 (2026-08-31)
- 1.2.3 (2026-08-31)
- 1.2.2 (2026-08-29)
- 1.2.1 (2026-08-28)
- 1.2.0 (2026-08-27)
- 1.1.4 (2026-08-21)
- 1.1.3 (2026-08-16)
- 1.1.2 (2026-08-10)
- 1.1.0 (2026-08-08)
- 1.0.3 (2026-08-07)
- 1.0.2 (2026-08-04)
- 1.0.1 (2026-07-31)
- 1.0.0 (2026-07-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/zippendo
- gem 安装: `gem install zippendo`
- Bundler: `gem "zippendo"`
- 最新版本: 1.3.4
- 最新版归档: https://rubygems.org/downloads/zippendo-1.3.4.gem
- 版本锁定: `gem "zippendo", "~> 1.3.4"`
- 中央仓库: https://rubygems.org/
