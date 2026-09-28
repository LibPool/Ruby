# guard-entangle

**Tag**: tooling, filesystem

## 简介

This gem leverages Guard's watch ability to insert files inline within another file. When the parser incounters a //= path/to/file, it then gets the content of that file and then inserts the content replacing the comment. Optionally that file can then be passed through Uglifier. Files with no insertions will just be copied over.

## 官网

- 主页: http://rubygems.org/gems/guard-entangle
- 源码仓库: https://github.com/deshiknaves/guard-entangle
- 问题追踪: https://github.com/deshiknaves/guard-entangle/issues
- RubyGems: https://rubygems.org/gems/guard-entangle

## 历史版本号

- 0.0.5.2 (2014-08-08)
- 0.0.5.1 (2014-08-07)
- 0.0.5.0 (2014-08-07)
- 0.0.4.4 (2014-04-02)
- 0.0.4.3 (2014-03-14)
- 0.0.4.2 (2014-03-14)
- 0.0.4.1 (2014-03-12)
- 0.0.4 (2014-03-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/guard-entangle
- gem 安装: `gem install guard-entangle`
- Bundler: `gem "guard-entangle"`
- 最新版本: 0.0.5.2
- 最新版归档: https://rubygems.org/downloads/guard-entangle-0.0.5.2.gem
- 版本锁定: `gem "guard-entangle", "~> 0.0.5.2"`
- 中央仓库: https://rubygems.org/
