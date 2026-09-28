# autogui

**Tag**: web, testing

## 简介

AutoGUI controls the mouse and keyboard, takes screenshots, finds images on
the screen, shows message boxes, and inspects application windows. It is a
Ruby port of Python PyAutoGUI with snake_case methods and CamelCase aliases.

Windows talks to the Win32 API through Ruby's standard-library Fiddle
(no extra gems). macOS uses osascript and screencapture. Linux uses
xdotool plus scrot, ImageMagick, or grim.

Fail-safe: moving the cursor into a screen corner raises FailSafeException.

## 官网

- 主页: https://github.com/pardeep2690/autogui
- 文档: https://github.com/pardeep2690/autogui#readme
- 更新日志: https://github.com/pardeep2690/autogui/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/pardeep2690/autogui/issues
- RubyGems: https://rubygems.org/gems/autogui

## 历史版本号

- 1.0.1 (2026-09-04)
- 1.0.0 (2026-09-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/autogui
- gem 安装: `gem install autogui`
- Bundler: `gem "autogui"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/autogui-1.0.1.gem
- 版本锁定: `gem "autogui", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
