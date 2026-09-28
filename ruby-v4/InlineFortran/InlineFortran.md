# InlineFortran

**Tag**: tooling

## 简介

== FEATURES/PROBLEMS:  * Very rudimentary right now. Needs some love.  == SYNOPSYS:  inline :Fortran do |builder| builder.subroutine('print_integer', [&quot;void&quot;, &quot;int&quot;], &lt;&lt;-END) subroutine print_integer( integer ) integer, intent(in) :: integer print *, 'integer: ', integer end END end  == REQUIREMENTS:

## 官网

- 主页: http://www.rubyforge.org/projects/rubyinline
- RubyGems: https://rubygems.org/gems/InlineFortran

## 历史版本号

- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/InlineFortran
- gem 安装: `gem install InlineFortran`
- Bundler: `gem "InlineFortran"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/InlineFortran-1.0.0.gem
- 版本锁定: `gem "InlineFortran", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
