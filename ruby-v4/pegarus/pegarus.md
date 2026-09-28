# pegarus

**Tag**: tooling

## 简介

Pegarus is, broadly, an implementation of LPEG on Rubinius. LPEG implements a
Parsing Expression Grammar using a parsing machine rather than the Packrat
algorithm. (See "A Text Pattern-Matching Tool based on Parsing Expression
Grammars" by Roberto Ierusalimschy.)

Pegarus actually implements an abstract syntax tree (AST) for the PEG. There
are various options to execute the AST against a subject string. One option is
a simple AST-walking evaluator. A second option is an implementation of the
LPEG parsing machine. A third option is a compiler that targets Rubinius
bytecode.

## 官网

- 主页: http://github.com/brixen/pegarus
- RubyGems: https://rubygems.org/gems/pegarus

## 历史版本号

- 0.2.0 (2010-10-25)
- 0.1.0 (2010-10-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/pegarus
- gem 安装: `gem install pegarus`
- Bundler: `gem "pegarus"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/pegarus-0.2.0.gem
- 版本锁定: `gem "pegarus", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
