# i18nize

**Tag**: web, cli, serialization, filesystem

## 简介

i18nize helps Ruby and Rails projects stay multilingual by automatically filling in 
missing translations in I18n YAML locale files. It scans for missing or empty keys 
across nested locale structures, and uses the DeepL API (Free or Pro) to translate 
them from a chosen source locale (default: en).

Features:
- Detects and lists missing translation keys
- Automatically translates and inserts values into the correct YAML files
- Supports nested directories and multiple locale files (e.g. config/locales/api/en.yml)
- Preserves I18n placeholders such as %{count}
- Handles pluralization branches (one, other, etc.)
- Source locale is treated as the single source of truth (conflicts are resolved by overwrite)
- Simple CLI: `i18nize <locale>` or `i18nize <locale> --missing`

This gem streamlines the translation workflow, making it easier to maintain 
consistent, up-to-date locale files across large Ruby on Rails applications.

## 官网

- 主页: https://github.com/nikolas2145/i18nize
- 更新日志: https://github.com/nikolas2145/i18nize/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/i18nize

## 历史版本号

- 0.6 (2025-09-11)
- 0.5.1 (2025-09-09)
- 0.5 (2025-09-08)
- 0.4.5 (2025-09-08)
- 0.4.4 (2025-09-08)
- 0.4.2.1 (2025-09-08)
- 0.4.2 (2025-09-08)
- 0.4.1 (2025-09-08)
- 0.4.0 (2025-08-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/i18nize
- gem 安装: `gem install i18nize`
- Bundler: `gem "i18nize"`
- 最新版本: 0.6
- 最新版归档: https://rubygems.org/downloads/i18nize-0.6.gem
- 版本锁定: `gem "i18nize", "~> 0.6"`
- 中央仓库: https://rubygems.org/
