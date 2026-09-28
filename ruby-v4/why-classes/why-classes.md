# why-classes

**Tag**: web, tooling, filesystem, data

## 简介

why-classes is a linter and refactoring tool inspired by Dave Thomas's talk on the
over-use of classes in Ruby. It scans a Ruby/Rails codebase (or a single file) for
"class smells" -- stateless singleton-method classes, function buckets, invalid
initial state, fat-base inheritance, and data buckets -- and reports each one with a
concrete refactoring suggestion toward modules, composition, Struct or Data. The
mechanically-safe refactorings (notably data bucket -> Struct/Data) can be applied
automatically with --fix.

## 官网

- 主页: https://github.com/joaoGabriel55/why-classes
- RubyGems: https://rubygems.org/gems/why-classes

## 历史版本号

- 0.2.1 (2026-07-21)
- 0.1.1 (2026-07-21)
- 0.1.0 (2026-07-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/why-classes
- gem 安装: `gem install why-classes`
- Bundler: `gem "why-classes"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/why-classes-0.2.1.gem
- 版本锁定: `gem "why-classes", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
