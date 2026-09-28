# irb_callbacks

**Tag**: web, cli, security, networking, filesystem

## 简介

* http://rubysideshow.rubyforge.org/irb_callbacks  == DESCRIPTION:  This gem adds callbacks to irb, intended for you to override at your discretion.  == FEATURES:  irb's control flow looks like this:  loop: * prompt * eval * output  This gem adds three callbacks to each phase.  module IRB:  * self.before_prompt * self.around_prompt (call yield) * self.after_prompt  * self.before_eval * self.around_eval (call yield) * self.after_eval  * self.before_output * self.around_output (call yield) * self.after_output  == SYNOPSIS:  # Here's my ~/.irbrc file (which is run at irb startup)  require 'rubygems' require 'irb_callbacks' require 'benchmark'  # This little snippet will time each command run via the console.  module IRB def self.around_eval(&amp;block) @timing = Benchmark.realtime do block.call end end  def self.after_output puts &quot;=&gt; #{'%.3f' % @timing} seconds&quot; end end  # And a sample irb session:  $ irb irb(main):001:0&gt; 1_000_000.times { |x| x + 1 } =&gt; 1000000 =&gt; 0.330 seconds  == CAVEATS:  The three around_* callbacks all require you to call the block that's passed in.  If you don't do it, undefined  behavior may occur.  == INSTALL:  * sudo gem install irb_callbacks  == LICENSE:  (The MIT License)  Copyright (c) 2008 Mike Judge  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 官网

- 主页: http://rubysideshow.rubyforge.org/irb_callbacks
- RubyGems: https://rubygems.org/gems/irb_callbacks

## 历史版本号

- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/irb_callbacks
- gem 安装: `gem install irb_callbacks`
- Bundler: `gem "irb_callbacks"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/irb_callbacks-0.1.0.gem
- 版本锁定: `gem "irb_callbacks", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
