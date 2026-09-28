# ascii_pngfy

**Tag**: template

## 简介

AsciiPngfy is a Ruby Gem that enables you to render ASCII text into a PNG image up to a resolution of 3840(width) by 2160(height) using a 5x9 monospaced font. Configurable settings that influence   the result are font-color, background-color, font-height, horizontal-spacing, vertical-spacing, and text. The result includes the PNG containing the intended image with all the settings applied, a snapshot of the settings used, and render dimensions that define the size the generated png should be rendered at to reflect the font-height settings. The generated png is always the lowest possible resolution. Each monospaced character takes up a 5(width) by 9(height) space to take advantage of scaled rendering and avoid unnecessarily large images. For the best visual results, the resulting png should be rendered in the original dimensions or the render dimensions along with a NEAREST filter.

## 官网

- 主页: https://github.com/SvenGarson/ascii_pngfy
- 文档: https://www.rubydoc.info/gems/ascii_pngfy/0.2.0
- RubyGems: https://rubygems.org/gems/ascii_pngfy

## 历史版本号

- 0.2.0 (2021-02-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/ascii_pngfy
- gem 安装: `gem install ascii_pngfy`
- Bundler: `gem "ascii_pngfy"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/ascii_pngfy-0.2.0.gem
- 版本锁定: `gem "ascii_pngfy", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
