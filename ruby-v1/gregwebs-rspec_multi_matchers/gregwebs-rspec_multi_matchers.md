# gregwebs-rspec_multi_matchers

**Tag**: web, testing

## 简介

* match_each * match_enum * match_in_order  require 'rubygems' require 'spec' require 'gregwebs-rspec_multi_matchers'  describe 'array of ones' do it 'should be all ones' do [1,2,3].should each { |n|  n.should == 1 } end end  =begin output 'array of ones should fail on 2' FAILED line: 14 item 1: 2 expected: 1, got: 2 (using ==) =end  As expected, the output shows expected and got fields line is the line number of the expectiation inside the block the item line gives the index of the item being yielded to the block, and the item itself

## 官网

- 主页: http://github.com/gregwebs/rspec-multi-matchers
- 文档: https://www.rubydoc.info/gems/gregwebs-rspec_multi_matchers/1.0.2
- RubyGems: https://rubygems.org/gems/gregwebs-rspec_multi_matchers

## 历史版本号

- 1.0.0 (2014-08-11)
- 1.0.1 (2014-08-11)
- 1.0.2 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/gregwebs-rspec_multi_matchers
- gem 安装: `gem install gregwebs-rspec_multi_matchers`
- Bundler: `gem "gregwebs-rspec_multi_matchers"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/gregwebs-rspec_multi_matchers-1.0.2.gem
- 版本锁定: `gem "gregwebs-rspec_multi_matchers", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
