# rspec_multi_matchers

**Tag**: web, testing, security, networking, template, filesystem

## 简介

= rspec-multi-matchers

== Summary
* test collection using each or other enumerable methods
* makes testing more natural and have a friendlier failure message

== HomePage
* http://github.com/gregwebs/rspec-multi-matchers

== DESCRIPTION:

    require 'rubygems'
    require 'spec'
    require 'rspec_multi_matchers'

    describe 'array of ones' do
      it 'should be all ones' do
        [1,2,3].should each { |n| 
          n.should == 1
        }
      end

      # this is a new shortcut for a smaller use case
      it 'should be all ones' do
        [1,1,1].should each be_eql(1)
      end
    end

    =begin output
    'array of ones should fail on 2' FAILED
        line: 14
      item 1: 2
    expected: 1,
         got: 2 (using ==)
    =end

As expected, the output shows expected and got fields
line is the line number of the expectiation inside the block
the item line gives the index of the item being yielded to the block, and the item itself


=== Warning

Note the use of brackets  '{ ... }' instead of 'do ... end'
this is necessary because 'do .. end' does not bind strongly enough

== RELATED ARTICLES:

* http://blog.thoughtfolder.com/2008-11-05-rspec-should-each-matcher.html

== INSTALL:

* gem install rspec_multi_matchers

== LICENSE:

(The MIT License)

Copyright (c) 2010 Greg Weber

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 官网

- 主页: https://github.com/gregwebs/rspec-multi-matchers
- RubyGems: https://rubygems.org/gems/rspec_multi_matchers

## 历史版本号

- 1.2.1 (2011-08-24)
- 1.2.0 (2011-08-24)
- 1.1.0 (2011-03-31)
- 1.0.8 (2011-03-31)
- 1.0.6 (2010-07-17)
- 1.0.4 (2010-04-16)
- 1.0.3 (2010-04-16)
- 1.0.2 (2010-04-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/rspec_multi_matchers
- gem 安装: `gem install rspec_multi_matchers`
- Bundler: `gem "rspec_multi_matchers"`
- 最新版本: 1.2.1
- 最新版归档: https://rubygems.org/downloads/rspec_multi_matchers-1.2.1.gem
- 版本锁定: `gem "rspec_multi_matchers", "~> 1.2.1"`
- 中央仓库: https://rubygems.org/
