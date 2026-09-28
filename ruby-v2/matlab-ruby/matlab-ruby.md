# matlab-ruby

**Tag**: testing, tooling

## 简介

== USAGE:  require 'matlab'  engine = Matlab::Engine.new engine.put_variable &quot;x&quot;, 123.456 engine.put_variable &quot;y&quot;, 789.101112 engine.eval &quot;z = x * y&quot; engine.get_variable &quot;z&quot;  matrix = Matlab::Matrix.new(20, 400) 20.times { |m| 400.times { |n| matrix[m, n] = rand } } engine.put_variable &quot;m&quot;, matrix  engine.save &quot;/tmp/20_x_400_matrix&quot; engine.close  # May also use block syntax for new Matlab::Engine.new do |engine| engine.put_variable &quot;x&quot;, 123.456 engine.get_variable &quot;x&quot; end  == REQUIREMENTS:  * MATLAB * GCC or some other compiler to build the included extension * SWIG (If you want to recompile the SWIG wrapper) * Mocha (For testing only)

## 官网

- 主页: http://matlab-ruby.rubyforge.org/
- RubyGems: https://rubygems.org/gems/matlab-ruby

## 历史版本号

- 2.0.3 (2009-07-25)
- 2.0.2 (2009-07-25)
- 2.0.1 (2009-07-25)
- 2.0.0 (2009-07-25)
- 1.0.1 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/matlab-ruby
- gem 安装: `gem install matlab-ruby`
- Bundler: `gem "matlab-ruby"`
- 最新版本: 2.0.3
- 最新版归档: https://rubygems.org/downloads/matlab-ruby-2.0.3.gem
- 版本锁定: `gem "matlab-ruby", "~> 2.0.3"`
- 中央仓库: https://rubygems.org/
