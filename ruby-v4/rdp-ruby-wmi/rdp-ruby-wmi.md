# rdp-ruby-wmi

**Tag**: web, security, networking, template, filesystem

## 简介

ruby-wmi
    by Gordon Thiesfeld
    http://ruby-wmi.rubyforge.org/
    gthiesfeld@gmail.com

== DESCRIPTION:

  ruby-wmi is an ActiveRecord style interface for Microsoft's Windows
  Management Instrumentation provider.

  Many of the methods in WMI::Base are borrowed directly, or with some
  modification from ActiveRecord.
    http://api.rubyonrails.org/classes/ActiveRecord/Base.html

  The major tool in this library is the #find method.  For more
  information, see WMI::Base.

  There is also a WMI.sublasses method included for reflection.

== SYNOPSIS:

  # The following code sample kills all processes of a given name
  # (in this case, Notepad), except the oldest.

    require 'ruby-wmi'

    procs = WMI::Win32_Process.find(:all,
                                    :conditions => { :name => 'Notepad.exe' }
                                   )
    morituri = procs.sort_by{|p| p.CreationDate } #those who are about to die
    morituri.shift
    morituri.each{|p| p.terminate }

== REQUIREMENTS:

    Windows 2000 or newer
    Ruby 1.8

== INSTALL:

  gem install ruby-wmi

== LICENSE:

(The MIT License)

Copyright (c) 2007 Gordon Thiesfeld

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

- 主页: http://rubyforge.org/projects/ruby-wmi/
- RubyGems: https://rubygems.org/gems/rdp-ruby-wmi

## 历史版本号

- 0.3.1 (2009-12-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/rdp-ruby-wmi
- gem 安装: `gem install rdp-ruby-wmi`
- Bundler: `gem "rdp-ruby-wmi"`
- 最新版本: 0.3.1
- 最新版归档: https://rubygems.org/downloads/rdp-ruby-wmi-0.3.1.gem
- 版本锁定: `gem "rdp-ruby-wmi", "~> 0.3.1"`
- 中央仓库: https://rubygems.org/
