# pikuri-extractors

**Tag**: cli, networking, devops, filesystem

## 简介

pikuri-extractors plugs additional document formats into
pikuri-core's +Pikuri::Extractor+ registry. The bundled
+Pikuri::Extractors::DOCUMENTS+ extractor converts office
documents (DOCX, ODT, XLSX, legacy XLS, PPTX, EPUB, RTF) to
Markdown by piping the bytes through pandoc / markitdown —
preferably inside a one-shot, networkless, locally-built docker
container (the untrusted bytes never touch the host filesystem or
network), falling back to a host-installed pandoc / markitdown
CLI when docker is absent.

Registration is explicit — +Pikuri::Extractors::DOCUMENTS.register+
— so requiring the gem changes nothing by itself; the host script
picks which extractors it wires in.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-extractors

## 历史版本号

- 0.1.0 (2026-08-30)
- 0.0.7 (2026-06-11)
- 0.0.6 (2026-06-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-extractors
- gem 安装: `gem install pikuri-extractors`
- Bundler: `gem "pikuri-extractors"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-extractors-0.1.0.gem
- 版本锁定: `gem "pikuri-extractors", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
