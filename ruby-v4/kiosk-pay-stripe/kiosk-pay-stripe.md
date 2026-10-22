# kiosk-pay-stripe

**Tag**: security, filesystem

## 简介

kiosk-pay-stripe is the open-source Stripe payment adapter for Kiosk. It
implements both halves of the provider-acquired, card-on-file model:

  - Card acquisition. `setup_url(user_id:, return_url:)` returns a hosted Stripe
    Checkout session in `mode: "setup"` that saves the buyer's card on the
    PROVIDER's own Stripe account (an existing open setup session is
    reused, so the url is stable across polls); `setup_required?` tells the
    wire whether a principal still has to complete it, backed by
    `saved_method?`, which asks Stripe whether the resolved Customer has a
    usable card.
  - Charging. This adapter's own `#capture` settles an AP2 cart
    mandate as an `off_session` (merchant-initiated) PaymentIntent against
    that saved card — the assistant authorizes the cart, it never presents
    a card.

The gem stays app-agnostic: the principal-to-Stripe-Customer mapping is
injected by the host through `customer_resolver:` / `customer_saver:`
callables, and no application table is read inside the gem.

Today only kiosk-pay-stripe ships; there is no default PSP
(Configuration#payment_provider is nil). A host that needs another PSP
subclasses Kiosk::PaymentProviders::Base and assigns the instance to
Kiosk.configuration.payment_provider.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-pay-stripe/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-pay-stripe

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-pay-stripe
- gem 安装: `gem install kiosk-pay-stripe`
- Bundler: `gem "kiosk-pay-stripe"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-pay-stripe-0.6.1.gem
- 版本锁定: `gem "kiosk-pay-stripe", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
