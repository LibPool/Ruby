# heredoc_unindent

**Tag**: testing, tooling

## 简介

This gem removes common margin from indented strings, such as the ones
produced by indented heredocs. In other words, it strips out leading whitespace
chars at the beggining of each line, but only as much as the line with the
smallest margin.

It is acknowledged that many strings defined by heredocs are just code and fact
is that most parsers are insensitive to indentation. If, however, the strings
are to be used otherwise, be it for printing or testing, the extra indentation
will probably be an issue and hence this gem.

## 官网

- 主页: https://github.com/adrianomitre/heredoc_unindent
- 文档: https://www.rubydoc.info/gems/heredoc_unindent/1.2.0
- 问题追踪: https://github.com/adrianomitre/heredoc_unindent/issues
- RubyGems: https://rubygems.org/gems/heredoc_unindent

## 历史版本号

- 1.2.0 (2015-04-15)
- 1.1.2 (2011-02-07)
- 1.1.1 (2011-01-29)
- 1.1.0 (2011-01-29)
- 1.0.6 (2011-01-27)
- 1.0.5 (2011-01-27)
- 1.0.4 (2011-01-27)
- 1.0.3 (2011-01-27)
- 1.0.2 (2011-01-26)
- 1.0.1 (2011-01-26)
- 1.0.0 (2011-01-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/heredoc_unindent
- gem 安装: `gem install heredoc_unindent`
- Bundler: `gem "heredoc_unindent"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/heredoc_unindent-1.2.0.gem
- 版本锁定: `gem "heredoc_unindent", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
