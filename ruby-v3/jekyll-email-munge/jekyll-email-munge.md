# jekyll-email-munge

**Tag**: cli, security, tooling

## 简介

A Jekyll plugin for address munging — defending email addresses on public
sites against bulk harvesters. Stacks five independently-effective
techniques (AES-128-GCM encryption, JS conversion, click trigger,
CSS-hidden decoy, SVG noscript fallback) so scrapers see ciphertext while
humans see a normal mailto link. Drop in a Liquid tag —
`{% munge_email "user@example.com" %}` — and the plugin handles encryption
at build time, the decoder script, and the fallback markup.

## 官网

- 主页: https://github.com/framallo/jekyll-email-munge
- 文档: https://github.com/framallo/jekyll-email-munge#readme
- 更新日志: https://github.com/framallo/jekyll-email-munge/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/framallo/jekyll-email-munge/issues
- RubyGems: https://rubygems.org/gems/jekyll-email-munge

## 历史版本号

- 0.1.0 (2026-05-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/jekyll-email-munge
- gem 安装: `gem install jekyll-email-munge`
- Bundler: `gem "jekyll-email-munge"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/jekyll-email-munge-0.1.0.gem
- 版本锁定: `gem "jekyll-email-munge", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
