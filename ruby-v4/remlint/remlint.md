# remlint

**Tag**: tooling, filesystem

## 简介

RemLint checks Remind reminder files for style, consistency and structure:
unbalanced IF/ENDIF blocks, mistyped $SysVars, wrong argument counts,
continuations that do not continue, and trailing whitespace that breaks
rem2ps. Its vocabulary is transcribed from Remind's own dispatch tables, so
keyword abbreviations and function arities match the interpreter exactly.

It reads Remind out of shell heredocs as well as .rem files, and reports
line numbers in the enclosing file.

## 官网

- 主页: https://dianne.skoll.ca/projects/remind/
- 文档: https://www.rubydoc.info/gems/remlint/0.1.0
- RubyGems: https://rubygems.org/gems/remlint

## 历史版本号

- 0.1.0 (2026-08-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/remlint
- gem 安装: `gem install remlint`
- Bundler: `gem "remlint"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/remlint-0.1.0.gem
- 版本锁定: `gem "remlint", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
