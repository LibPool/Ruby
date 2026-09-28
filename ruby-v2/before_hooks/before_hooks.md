# before_hooks

**Tag**: testing

## 简介

Adds `before_extended`, `before_included`, and `before_prepended` methods hooks which would be called before the standard `extended`, `included`, and `prepended` Ruby hooks, respectively. Especially useful when you require to "do" something just before the module gets `extended` or `included` to a module/class. In particular, in my specific case, I needed to "do" something if a specific method already exists in the `base` class.

## 官网

- 主页: https://github.com/jrpolidario/before_hooks
- 文档: https://www.rubydoc.info/gems/before_hooks/0.1.4
- RubyGems: https://rubygems.org/gems/before_hooks

## 历史版本号

- 0.1.4 (2019-03-06)
- 0.1.3 (2019-02-23)
- 0.1.2 (2019-02-23)
- 0.1.1 (2019-02-23)
- 0.1.0 (2019-02-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/before_hooks
- gem 安装: `gem install before_hooks`
- Bundler: `gem "before_hooks"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/before_hooks-0.1.4.gem
- 版本锁定: `gem "before_hooks", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
