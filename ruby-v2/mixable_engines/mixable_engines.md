# mixable_engines

**Tag**: web

## 简介

In the old Engines plugin (used before the built-in engines arrived in rails 2.3), controller and helper classes were mixed together.  That is, if an engine had a FooController, and your application also had a FooController, you could use the actions in both controllers.  In the built-in Engines functionality in Rails 3, this does not occur.  Your application's FooController replaces the engine controller entirely.

  This gem restores the old functionality, allowing you to easily override parts of an engine in your application.

## 官网

- 主页: http://github.com/asee/mixable_engines
- RubyGems: https://rubygems.org/gems/mixable_engines

## 历史版本号

- 0.1.1 (2011-09-02)
- 0.1.0 (2011-09-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/mixable_engines
- gem 安装: `gem install mixable_engines`
- Bundler: `gem "mixable_engines"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/mixable_engines-0.1.1.gem
- 版本锁定: `gem "mixable_engines", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
