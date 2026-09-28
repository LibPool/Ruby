# google-map-static-image-generator

**Tag**: web, tooling, filesystem

## 简介

google-map-static-image-generator is a Ruby wrapper around the Google Maps Static
API that generates PNG map images on the fly — no JavaScript required.

Features:
- Add custom markers at any coordinates
- Draw paths with custom weight and colour
- Apply map styles (hide labels, change colours, etc.)
- Set center + zoom for marker-free maps
- Choose map type: roadmap, satellite, terrain, or hybrid
- Default 1024x1024 at scale 2 (retina-friendly)
- Raises GoogleMapStaticImage::ApiError on non-200 responses (invalid key, quota exceeded, etc.)

Useful for generating map thumbnails in emails, PDFs, admin dashboards, and anywhere
an interactive JavaScript map is not practical.

## 官网

- 主页: https://github.com/abhsss96/google-map-static-image-generator
- 更新日志: https://github.com/abhsss96/google-map-static-image-generator/releases
- 问题追踪: https://github.com/abhsss96/google-map-static-image-generator/issues
- RubyGems: https://rubygems.org/gems/google-map-static-image-generator

## 历史版本号

- 0.0.4 (2026-05-31)
- 0.0.3 (2026-05-31)
- 0.0.2 (2026-05-31)
- 0.0.1 (2014-10-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/google-map-static-image-generator
- gem 安装: `gem install google-map-static-image-generator`
- Bundler: `gem "google-map-static-image-generator"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/google-map-static-image-generator-0.0.4.gem
- 版本锁定: `gem "google-map-static-image-generator", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
