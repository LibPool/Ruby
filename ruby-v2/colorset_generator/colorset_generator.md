# colorset_generator

**Tag**: web, serialization, networking, tooling, filesystem

## 简介

Generates Xcode .xcassets ColorSet JSON files from color palette URLs.

Extracts hex color codes embedded in URLs from palette tools such as:
  - Huemint  (https://huemint.com)
  - RealtimeColors (https://realtimecolors.com)
  - Coolors  (https://coolors.co)

Any URL that encodes hex codes in its path or query string is supported.
Dark mode variants are automatically calculated by inverting the HSL
lightness of each light color — no manual dark palette needed.

The generated Colors.xcassets folder can be dragged and dropped directly
into Xcode's Assets catalog to use the colors in Swift/SwiftUI projects.

Usage:
  colorset_generator "https://huemint.com/brand-2/#palette=2a3031-fafdfc-a19985"
  colorset_generator "https://coolors.co/c4f1be-a2c3a4-869d96-525b76-201e50" --output MyPalette.xcassets
  colorset_generator "https://www.realtimecolors.com/?colors=14140f-f8f8f6-9a9e79-aec4bd-8ea7ad" --no-dark

## 官网

- 文档: https://www.rubydoc.info/gems/colorset_generator/0.1.0
- RubyGems: https://rubygems.org/gems/colorset_generator

## 历史版本号

- 0.1.0 (2026-04-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/colorset_generator
- gem 安装: `gem install colorset_generator`
- Bundler: `gem "colorset_generator"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/colorset_generator-0.1.0.gem
- 版本锁定: `gem "colorset_generator", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
