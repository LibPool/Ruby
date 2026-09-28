# rbx-require-relative

**Tag**: filesystem

## 简介

Ruby 1.9's require_relative for Rubinius and MRI 1.8. 

We also add abs_path which is like __FILE__ but __FILE__ can be fooled
by a sneaky "chdir" while abs_path can't. 

If you are running on Ruby 1.9 or greater, require_relative is the
pre-defined version.  The benefit we provide in this situation by this
package is the ability to write the same require_relative sequence in
Rubinius 1.8 and Ruby 1.9.

## 官网

- 主页: http://github.com/rocky/rbx-require-relative
- RubyGems: https://rubygems.org/gems/rbx-require-relative

## 历史版本号

- 0.0.9 (2012-02-28)
- 0.0.7-universal-ruby-1.8.7 (2012-02-27)
- 0.0.7-universal-ruby-1.9.3 (2012-02-27)
- 0.0.7 (2012-02-27)
- 0.0.7-universal-rubinius-1.2 (2012-02-27)
- 0.0.6 (2012-02-23)
- 0.0.6-universal-ruby-1.9.2 (2012-02-23)
- 0.0.6-universal-jruby-1.2 (2012-02-23)
- 0.0.6-universal-ruby-1.8.7 (2012-02-23)
- 0.0.6-universal-ruby-1.9.3 (2012-02-22)
- 0.0.5 (2011-06-12)
- 0.0.5-universal-ruby-1.9.2 (2011-06-12)
- 0.0.5-universal-ruby-1.8.7 (2011-06-12)
- 0.0.5-universal-rubinius-1.2 (2011-06-12)
- 0.0.4-universal-rubinius-1.2 (2011-04-22)
- 0.0.3 (2010-09-27)
- 0.0.2 (2010-09-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/rbx-require-relative
- gem 安装: `gem install rbx-require-relative`
- Bundler: `gem "rbx-require-relative"`
- 最新版本: 0.0.9
- 最新版归档: https://rubygems.org/downloads/rbx-require-relative-0.0.9.gem
- 版本锁定: `gem "rbx-require-relative", "~> 0.0.9"`
- 中央仓库: https://rubygems.org/
