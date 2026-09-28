# octave-ruby

**Tag**: testing, tooling

## 简介

== USAGE:  require 'octave'  engine = Octave::Engine.new engine.eval "123.456 * 789.101112" engine.rand(10)  matrix = Octave::Matrix.new(20, 400) 20.times { |m| 400.times { |n| matrix[m, n] = rand } } engine.put_variable("m", matrix)  engine.save "/tmp/20_x_400_matrix"  == REQUIREMENTS:  * Octave * GCC or some other compiler to build the included extension * Mocha (For testing only)

## 官网

- 主页: http://octave-ruby.rubyforge.org/
- RubyGems: https://rubygems.org/gems/octave-ruby

## 历史版本号

- 2.0.3 (2013-01-29)
- 2.0.2 (2013-01-21)
- 2.0.1 (2012-11-09)
- 2.0.0 (2012-11-08)
- 1.0.0 (2009-07-25)
- 1.0.9 (2009-07-25)
- 1.0.8 (2009-07-25)
- 1.0.7 (2009-07-25)
- 1.0.6 (2009-07-25)
- 1.0.5 (2009-07-25)
- 1.0.4 (2009-07-25)
- 1.0.3 (2009-07-25)
- 1.0.2 (2009-07-25)
- 1.0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/octave-ruby
- gem 安装: `gem install octave-ruby`
- Bundler: `gem "octave-ruby"`
- 最新版本: 2.0.3
- 最新版归档: https://rubygems.org/downloads/octave-ruby-2.0.3.gem
- 版本锁定: `gem "octave-ruby", "~> 2.0.3"`
- 中央仓库: https://rubygems.org/
