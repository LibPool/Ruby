# svg_sentinel

**Tag**: cli, serialization, template, filesystem, data

## 简介

A small, dependency-light Ruby tool for untrusted SVG. It flags the things that make SVG dangerous to render or embed: scripts, event handlers, javascript: URIs, external references (including inside CSS), scriptable data: URIs, foreign objects, XXE via DOCTYPE or ENTITY declarations, and nested-<use> render bombs. It can also sanitize - rewrite an SVG into a safe one - and re-rates findings for the rendering context (inline vs <img>). Normalises encoding, caps size, and bounds structural shape on a streaming pass so it is safe to point at hostile input. Ships a strict allowlist profile for brand-mark logos (BIMI-style), a general profile, YAML config, and a CLI with CI-friendly exit codes and SARIF output. Pure Ruby, parses with REXML, no native extensions.

## 官网

- 主页: https://github.com/msuliq/svg_sentinel
- 更新日志: https://github.com/msuliq/svg_sentinel/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/msuliq/svg_sentinel/issues
- RubyGems: https://rubygems.org/gems/svg_sentinel

## 历史版本号

- 0.1.0 (2026-07-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/svg_sentinel
- gem 安装: `gem install svg_sentinel`
- Bundler: `gem "svg_sentinel"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/svg_sentinel-0.1.0.gem
- 版本锁定: `gem "svg_sentinel", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
