# rabbit-slide-tikkss-rubykaigi-2026

**Tag**: testing

## 简介

When a library grows, its test suites become slow. This makes programmers unhappy. Parallel testing based on the multiprocess is a common practice to solve this. However, most testing frameworks and tools are not "portable" enough to support various environments. Because they depend on Unix specific features like `fork` or external libraries including other bundled gems like drb.

To address this, test-unit (as a bundled gem) now natively supports portable and fast parallel test running based on the multiprocess. It is designed to work in various environments (e.g. Windows) out of the box.

This talk describes the journey of implementing parallel running to a historical testing framework without breaking backward compatibility. If you are interested in speeding up your test suites, implementing portable parallel libraries or maintaining historical codebases, this talk will help you.

## 官网

- 主页: https://slide.rabbit-shocker.org/authors/tikkss/rubykaigi-2026/
- 文档: https://www.rubydoc.info/gems/rabbit-slide-tikkss-rubykaigi-2026/1.0.0
- RubyGems: https://rubygems.org/gems/rabbit-slide-tikkss-rubykaigi-2026

## 历史版本号

- 1.0.0 (2026-04-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/rabbit-slide-tikkss-rubykaigi-2026
- gem 安装: `gem install rabbit-slide-tikkss-rubykaigi-2026`
- Bundler: `gem "rabbit-slide-tikkss-rubykaigi-2026"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/rabbit-slide-tikkss-rubykaigi-2026-1.0.0.gem
- 版本锁定: `gem "rabbit-slide-tikkss-rubykaigi-2026", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
