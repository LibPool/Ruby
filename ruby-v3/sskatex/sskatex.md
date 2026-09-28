# sskatex

**Tag**: web, cli, template, filesystem

## 简介

This is a TeX-to-HTML+MathML+CSS converter class using the Javascript-based
KaTeX, interpreted by one of the Javascript engines supported by ExecJS.
The intended purpose is to eliminate the need for math-rendering Javascript
in the client's HTML browser. Therefore the name: SsKaTeX means Server-side
KaTeX.

Javascript execution context initialization can be done once and then reused
for formula renderings with the same general configuration. As a result, the
performance is reasonable.

The configuration supports arbitrary locations of the external file katex.min.js
as well as custom Javascript for pre- and postprocessing.
For that reason, the configuration must not be left to untrusted users.

## 官网

- 主页: https://github.com/ccorn/sskatex
- 文档: https://www.rubydoc.info/gems/sskatex/0.9.39
- RubyGems: https://rubygems.org/gems/sskatex

## 历史版本号

- 0.9.39 (2018-01-27)
- 0.9.38 (2018-01-26)
- 0.9.37 (2018-01-25)
- 0.9.36 (2017-12-05)
- 0.9.35 (2017-12-03)
- 0.9.30 (2017-11-30)
- 0.9.23 (2017-11-23)
- 0.9.20 (2017-11-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/sskatex
- gem 安装: `gem install sskatex`
- Bundler: `gem "sskatex"`
- 最新版本: 0.9.39
- 最新版归档: https://rubygems.org/downloads/sskatex-0.9.39.gem
- 版本锁定: `gem "sskatex", "~> 0.9.39"`
- 中央仓库: https://rubygems.org/
