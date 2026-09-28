# need

**Tag**: testing, filesystem

## 简介

== DESCRIPTION:  Need makes ruby relative requires just work. Simply need a file with a relative path and the file will always be required correctly, regardless of what file your application is being launched through. Typically, ruby projects would unshift lib onto $PATH or use the File.dirname(__FILE__) trick. Using need means you don't have to worry about either of these.  Assume you have two files, one directly in lib and the other in lib/extensions. Let's assume that file_a in lib requires file_b, in lib/extensions. Previously, you would doing some crazy load path unshifting or use the __FILE__ trick to make these requires flexible enough to work when your app is being accessed by rake, through a test suite, or required as a gem. Now, just use need.  In file_a: need{&quot;extensions/file_b&quot;} need &quot;extensions/file_b&quot;

## 官网

- 主页: http://need.rubyforge.org
- RubyGems: https://rubygems.org/gems/need

## 历史版本号

- 1.1.0 (2009-07-25)
- 1.0.3 (2009-07-25)
- 1.0.2 (2009-07-25)
- 1.0.1 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/need
- gem 安装: `gem install need`
- Bundler: `gem "need"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/need-1.1.0.gem
- 版本锁定: `gem "need", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
