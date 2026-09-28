# static_embeddings

**Tag**: filesystem

## 简介

A small C-extension runtime for Model2Vec and Sentence Transformers static WordPiece embedding models. Models are converted offline into a flat mmap-able .semb file; at runtime the gem tokenizes (BERT WordPiece), looks up rows and mean-pools them. Releases the GVL on large native work, rejects internal thread fan-out, and links nothing but libc.

## 官网

- 主页: https://github.com/roman-haidarov/static_embeddings
- 更新日志: https://github.com/roman-haidarov/static_embeddings/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/static_embeddings

## 历史版本号

- 1.5.6 (2026-09-16)
- 0.1.5 (2026-09-01)
- 0.1.4 (2026-08-31)
- 0.1.3 (2026-08-30)
- 0.1.2 (2026-08-29)
- 0.1.1 (2026-08-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/static_embeddings
- gem 安装: `gem install static_embeddings`
- Bundler: `gem "static_embeddings"`
- 最新版本: 1.5.6
- 最新版归档: https://rubygems.org/downloads/static_embeddings-1.5.6.gem
- 版本锁定: `gem "static_embeddings", "~> 1.5.6"`
- 中央仓库: https://rubygems.org/
