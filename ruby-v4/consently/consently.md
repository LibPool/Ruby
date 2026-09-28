# consently

**Tag**: web, cli, database, template, tooling, data

## 简介

Most Rails cookie banners ask for consent and then load Google Analytics anyway. Consently is the other half: declare your tags once - GA4, Google Tag Manager, Google Ads, Microsoft Clarity, Meta Pixel, Hotjar, Plausible or anything custom - and it renders every non-essential one as an inert script the browser will not even fetch, then turns them into live scripts the instant the visitor agrees, with no page reload. Embedded YouTube, Vimeo and Google Maps iframes wait behind a placeholder of the same size and appear on consent too, because an iframe sets cookies with no script of yours. Google Consent Mode v2 defaults are emitted before any Google tag and updated on the click, in basic mode or in advanced mode where Google's own tags load denied so Ads can model refused conversions. GA4 ecommerce events are built from your own line items rather than by hand. The banner and its preferences panel ship translated into ten European languages, styled in plain CSS with no Tailwind and no build step. Your cookie policy page is generated from the same configuration - every vendor, every cookie it sets and for how long - so it cannot drift out of date. Multi-tenant applications get per-domain or per-shop tag sets from a single initializer, one consent can span subdomains, and an optional consent log stores proof of each decision in your own database, with no third-party service and nothing leaving your infrastructure.

## 官网

- 主页: https://github.com/Xeross99/consently
- 文档: https://xeross99.github.io/consently/
- 更新日志: https://github.com/Xeross99/consently/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/Xeross99/consently/issues
- RubyGems: https://rubygems.org/gems/consently

## 历史版本号

- 1.0.0 (2026-09-04)
- 0.2.1 (2026-08-13)
- 0.2.0 (2026-08-13)
- 0.1.0 (2026-08-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/consently
- gem 安装: `gem install consently`
- Bundler: `gem "consently"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/consently-1.0.0.gem
- 版本锁定: `gem "consently", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
