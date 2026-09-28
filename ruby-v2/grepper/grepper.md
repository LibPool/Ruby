# grepper

**Tag**: filesystem

## 简介

The Grepper class greps through files, and returns a result set of Grepper::Result objects. Each Result object represents the matches found in a single file. The Result contains a set of Grepper::Match objects. Each Match object represents a line (the line that matched) and before- and after-context arrays. If no before or after lines were requested, those context values will be nil.   To use, you prepare a Grepper object; call &lt;tt&gt;run&lt;/tt&gt; on it; and walk through the result set. This distribution comes with the Grepper::Formatter class, which is built on top of Grepper and provides fairly canonical-looking output by walking through Grepper objects.  (See &lt;tt&gt;lib/formatter.rb&lt;/tt&gt;.) Meanwhile, here are the details.

## 官网

- 文档: https://www.rubydoc.info/gems/grepper/0.9.3
- RubyGems: https://rubygems.org/gems/grepper

## 历史版本号

- 0.9.3 (2009-07-25)
- 0.9.2 (2009-07-25)
- 0.9.1 (2009-07-25)
- 0.9.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/grepper
- gem 安装: `gem install grepper`
- Bundler: `gem "grepper"`
- 最新版本: 0.9.3
- 最新版归档: https://rubygems.org/downloads/grepper-0.9.3.gem
- 版本锁定: `gem "grepper", "~> 0.9.3"`
- 中央仓库: https://rubygems.org/
