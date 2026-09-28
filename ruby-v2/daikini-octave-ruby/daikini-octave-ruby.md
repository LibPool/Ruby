# daikini-octave-ruby

**Tag**: testing, tooling

## 简介

== USAGE:  require 'octave'  engine = Octave::Engine.new engine.eval "123.456 * 789.101112" engine.rand(10)  matrix = Octave::Matrix.new(20, 400) 20.times { |m| 400.times { |n| matrix[m, n] = rand } } engine.put_variable("m", matrix)  engine.save "/tmp/20_x_400_matrix"  == REQUIREMENTS:  * Octave * GCC or some other compiler to build the included extension * Mocha (For testing only)

## 官网

- 主页: http://octave-ruby.rubyforge.org/
- 文档: https://www.rubydoc.info/gems/daikini-octave-ruby/1.0.9
- RubyGems: https://rubygems.org/gems/daikini-octave-ruby

## 历史版本号

- 1.0.9 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/daikini-octave-ruby
- gem 安装: `gem install daikini-octave-ruby`
- Bundler: `gem "daikini-octave-ruby"`
- 最新版本: 1.0.9
- 最新版归档: https://rubygems.org/downloads/daikini-octave-ruby-1.0.9.gem
- 版本锁定: `gem "daikini-octave-ruby", "~> 1.0.9"`
- 中央仓库: https://rubygems.org/
