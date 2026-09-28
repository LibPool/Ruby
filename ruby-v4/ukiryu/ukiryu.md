# ukiryu

**Tag**: web, cli, serialization, filesystem

## 简介

Ukiryu is a platform-adaptive command execution framework that transforms CLI tools
into declarative APIs. It provides the "OpenAPI" for command-line interfaces,
enabling cross-platform tool integration with type safety and structured results.

Key features:

* Declarative YAML profiles define tool behavior, eliminating hardcoded command strings
* Platform-adaptive execution across macOS, Linux, and Windows
* Shell-aware command formatting for bash, zsh, fish, PowerShell, and cmd
* Type-safe parameter validation with automatic coercion
* Version routing support with semantic version matching (via Versionian)
* Interface contracts allow multiple tools to implement the same abstract API
* Structured Result objects with success/failure information instead of parsing stdout
* Comprehensive error handling under Ukiryu::Errors namespace

The Ukiryu ecosystem consists of:

* ukiryu gem - The runtime framework
* ukiryu/register - Collection of YAML tool profiles
* ukiryu/schemas - JSON Schema for validation

Use Ukiryu to integrate command-line tools like ImageMagick, FFmpeg, Inkscape,
Ghostscript, and more into your Ruby applications with consistent,
predictable interfaces.

## 官网

- 主页: https://github.com/ukiryu/ukiryu
- 文档: https://www.rubydoc.info/gems/ukiryu/0.3.0
- RubyGems: https://rubygems.org/gems/ukiryu

## 历史版本号

- 0.3.0 (2026-05-04)
- 0.2.4 (2026-02-22)
- 0.2.3 (2026-02-20)
- 0.2.2 (2026-02-19)
- 0.2.1 (2026-02-19)
- 0.2.0 (2026-02-19)
- 0.1.7 (2026-02-13)
- 0.1.6 (2026-02-12)
- 0.1.4 (2026-01-26)
- 0.1.3 (2026-01-25)
- 0.1.1 (2026-01-23)
- 0.1.0 (2026-01-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/ukiryu
- gem 安装: `gem install ukiryu`
- Bundler: `gem "ukiryu"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/ukiryu-0.3.0.gem
- 版本锁定: `gem "ukiryu", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
