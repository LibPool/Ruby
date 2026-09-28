# peggy

**Tag**: testing, tooling

## 简介

This is a parsing library and language specifier. It uses packrat parsing, as opposed to LL(k) or LR(k) parsing. Packrat parsing uses memoization in a recursive decent parser. By storing the production results from each significant point it speeds up the parse. PEG is a formalized grammar specification optimized for packrat parsing. Peggy also allows user to specfy their grammar in pure Ruby as methods or using a Builder. And the default Peggy grammar is a  varitaion on PEG, with support for full regular expressions and for simplifed grammars which automatically ignore a set of productions.

## 官网

- 主页: http://rubyforge.org/projects/peggy/
- RubyGems: https://rubygems.org/gems/peggy

## 历史版本号

- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/peggy
- gem 安装: `gem install peggy`
- Bundler: `gem "peggy"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/peggy-0.1.0.gem
- 版本锁定: `gem "peggy", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
