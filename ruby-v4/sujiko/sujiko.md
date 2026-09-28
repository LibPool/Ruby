# sujiko

**Tag**: web, template, tooling, devops

## 简介

Sujiko is a joke / toy Ruby gem: a small TCP server for local development, not for serious or
production use. It serves one page: a venue floor plan where
a meetup point is shown. Open GET / with optional query parameters shape, x, and y—the same
contract as a Rails Spots-style app and iOS: shape selects the room (e.g. roomA, with
normalization to internal ids like room_a); x and y are normalized coordinates from 0.0 to 1.0
(top-left of the white floor, independent of device pixels). Use it to preview map UI and to
build or verify share URLs (Safari, copy, etc.) before deploying.

## 官网

- 主页: https://github.com/tutuitakumi/sujiko
- RubyGems: https://rubygems.org/gems/sujiko

## 历史版本号

- 0.1.0 (2026-04-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/sujiko
- gem 安装: `gem install sujiko`
- Bundler: `gem "sujiko"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/sujiko-0.1.0.gem
- 版本锁定: `gem "sujiko", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
