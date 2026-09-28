# filter

**Tag**: library

## 简介

== Synopsys
<code>Enumerable#filter</code> - extended <code>Enumerable#select</code>

== Examples
String filter (acts like <code>Enumerable#grep</code>):
  [1, 2, 3, 'ab'].filter(/a/)              # => ['ab']
  [1, 2, 3, '3'].filter('3')               # => ['3']

You can pass a <code>Proc</code> or <code>Symbol</code>. Methods and blocks are allowed too:
  [1, 2, 3].filter(&:even?)                # => [2]
  [1, 2, 3].filter(:even?)                 # => [2]
  [1, 2, 4].filter { |num| num.even? }     # => [2, 4]

<code>Enumerable#filter</code> can match against enumerable items attributes. Like this:
  [1, 2, 3, 4.2].filter :to_i => :even?    # => [2, 4]

If the block is supplied, each matching element is passed to it, and the block's result is stored in the output array.
  [1, 2, 4].filter(&:even?) { |n| n + 1 }  # => [3, 5]

<code>Enumerable#filter</code> also accepts <code>true</code> or <code>false</code> as argument:
  [0, false, 2, nil].filter(true)          # => [0, 2]
  [0, false, 2, nil].filter(false)         # => [false, nil]

<code>Enumerable#filter</code> also supports <code>OR</code> operator!
Just pass many patterns, they will be joined together with <code>OR</code> operator.
  [0, 2, 3, 4].filter(:zero?, :odd?)       # => [0, 3]

## 官网

- 主页: https://github.com/take-five/filter
- RubyGems: https://rubygems.org/gems/filter

## 历史版本号

- 0.0.6 (2011-12-12)
- 0.0.5 (2011-12-12)
- 0.0.4 (2011-12-12)
- 0.0.3 (2011-12-11)
- 0.0.2 (2011-12-11)
- 0.0.1 (2011-12-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/filter
- gem 安装: `gem install filter`
- Bundler: `gem "filter"`
- 最新版本: 0.0.6
- 最新版归档: https://rubygems.org/downloads/filter-0.0.6.gem
- 版本锁定: `gem "filter", "~> 0.0.6"`
- 中央仓库: https://rubygems.org/
