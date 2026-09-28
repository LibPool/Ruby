# vcvars

**Tag**: web, tooling

## 简介

vcvars locates a Visual Studio / Build Tools install via vswhere and loads the
MSVC toolchain (vcvars*.bat) into the current process, so C extensions build
under an mswin Ruby without first opening a "Developer Command Prompt".

It provides a library API (Vcvars.activate!), a Rake integration
(require "vcvars/rake"), a `vcvars exec -- <cmd>` runner, a `vcvars doctor`
that diagnoses the classic MSVC extension-build failures, a `vcvars env`
shell-env emitter, and a `vcvars new` scaffolder for MSVC-ready extension gems.
It is "ridk enable", but for MSVC. Pure Ruby, no compiler required to install.

## 官网

- 主页: https://github.com/main-path/vcvars
- 更新日志: https://github.com/main-path/vcvars/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/vcvars/issues
- RubyGems: https://rubygems.org/gems/vcvars

## 历史版本号

- 0.1.1 (2026-05-30)
- 0.1.0 (2026-05-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/vcvars
- gem 安装: `gem install vcvars`
- Bundler: `gem "vcvars"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/vcvars-0.1.1.gem
- 版本锁定: `gem "vcvars", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
