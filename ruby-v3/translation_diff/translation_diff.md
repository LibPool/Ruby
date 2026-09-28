# translation_diff

**Tag**: template

## 简介

TranslationDiff extracts translatable text from HTML, splits it into
sentences, and caches each sentence by content hash. Only the sentences
missing from the cache are sent to whichever translation provider you plug
in through a small provider contract, so re-translating a long text after a
small edit costs the price of the edit, not the whole text.

## 官网

- 主页: https://github.com/Halvanhelv/translation_diff
- RubyGems: https://rubygems.org/gems/translation_diff

## 历史版本号

- 1.0.0 (2026-09-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/translation_diff
- gem 安装: `gem install translation_diff`
- Bundler: `gem "translation_diff"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/translation_diff-1.0.0.gem
- 版本锁定: `gem "translation_diff", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
