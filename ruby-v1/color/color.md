# color

**Tag**: template, tooling, filesystem, data

## 简介

Color is a Ruby library to provide RGB, CMYK, HSL, and other color space
manipulation support to applications that require it. It provides optional named
RGB colors that are commonly supported in HTML, SVG, and X11 applications.

The Color library performs purely mathematical manipulation of the colors based
on color theory without reference to device color profiles (such as sRGB or
Adobe RGB). For most purposes, when working with RGB and HSL color spaces, this
won't matter. Absolute color spaces (like CIE LAB and CIE XYZ) cannot be
reliably converted to relative color spaces (like RGB) without color profiles.
When necessary for conversions, Color provides D65 and D50 reference white
values in Color::XYZ.

Color 2.2 adds a minor feature where an RGB color created from values can
silently inherit the `#name` of a predefined color if `color/rgb/colors` has
already been loaded. It builds on the Color 2.0 major release, dropping support
for all versions of Ruby prior to 3.2 as well as removing or renaming a number
of features. The main breaking changes are:

- Color classes are immutable Data objects; they are no longer mutable.
- RGB named colors are no longer loaded on gem startup, but must be required
  explicitly (this is _not_ done via `autoload` because there are more than 100
  named colors with spelling variations) with `require "color/rgb/colors"`.
- Color palettes have been removed.
- `Color::CSS` and `Color::CSS#[]` have been removed.

## 官网

- 主页: https://github.com/halostatue/color
- 文档: https://halostatue.github.io/color/
- 更新日志: https://github.com/halostatue/color/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/halostatue/color/issues
- RubyGems: https://rubygems.org/gems/color

## 历史版本号

- 2.2.0 (2026-01-22)
- 2.1.2 (2025-12-30)
- 2.1.1 (2025-08-08)
- 2.1.0 (2025-07-20)
- 2.0.1 (2025-07-05)
- 2.0.0 (2025-07-05)
- 2.0.0.pre.2 (2025-06-26)
- 2.0.0.pre.1 (2025-06-16)
- 2.0.0.pre.0 (2025-06-15)
- 1.8 (2015-10-26)
- 1.7.1 (2014-07-17)
- 1.7 (2014-06-13)
- 1.6 (2014-05-20)
- 1.5.1 (2014-01-28)
- 1.4.2 (2013-07-01)
- 1.4.1 (2010-02-07)
- 1.4.0 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/color
- gem 安装: `gem install color`
- Bundler: `gem "color"`
- 最新版本: 2.2.0
- 最新版归档: https://rubygems.org/downloads/color-2.2.0.gem
- 版本锁定: `gem "color", "~> 2.2.0"`
- 中央仓库: https://rubygems.org/
