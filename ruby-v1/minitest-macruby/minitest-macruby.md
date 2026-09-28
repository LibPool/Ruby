# minitest-macruby

**Tag**: testing, filesystem

## 简介

minitest-macruby provides extensions to minitest for macruby UI
testing. It provides a framework to test GUI apps in a live instance.
Documentation and examples are light at the moment as I've just thrown
this together. Suggestions for extensions are very welcome!

Currently it provides the following methods in minitest's assertions:

* self.run_macruby_tests
* find_ui_menu(*path)
* find_ui_menu_items menu
* assert_ui_menu menu, *items
* find_ui_menu_item(*path)
* assert_ui_action obj, target, action, key = nil
* assert_ui_binding item, binding_name, target, path

## 官网

- 主页: https://github.com/seattlerb/minitest-macruby
- RubyGems: https://rubygems.org/gems/minitest-macruby

## 历史版本号

- 1.0.1 (2013-04-23)
- 1.0.0 (2010-07-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/minitest-macruby
- gem 安装: `gem install minitest-macruby`
- Bundler: `gem "minitest-macruby"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/minitest-macruby-1.0.1.gem
- 版本锁定: `gem "minitest-macruby", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
