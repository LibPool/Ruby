# pry-hack

**Tag**: tooling

## 简介

Using a lexical parser, this gem allows you to add hacks to your REPL session allowing you to
have shortcut syntax. Things such as
[0] pry(main)> object.@ivar
=> :im_the_return_of_an_instance_variable

Or

[0] pry(main)> %S{hello symbol world}
=> [:hello, :symbol, :world]

And even the most desired ruby syntax of all is planned to come, that's right. Increment and decrement operators.

[0] pry(main)> i++
=> 1
[1] pry(main)> i--
=> 0

## 官网

- 主页: https://github.com/swarley/pry-hack
- RubyGems: https://rubygems.org/gems/pry-hack

## 历史版本号

- 0.1 (2012-11-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/pry-hack
- gem 安装: `gem install pry-hack`
- Bundler: `gem "pry-hack"`
- 最新版本: 0.1
- 最新版归档: https://rubygems.org/downloads/pry-hack-0.1.gem
- 版本锁定: `gem "pry-hack", "~> 0.1"`
- 中央仓库: https://rubygems.org/
