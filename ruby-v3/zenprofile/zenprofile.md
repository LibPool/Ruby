# zenprofile

**Tag**: filesystem

## 简介

zenprofiler helps answer WHAT is being called the most. spy_on helps
answer WHERE those calls are being made. ZenProfiler provides a faster
version of the standard library ruby profiler. It is otherwise pretty
much the same as before. spy_on provides a clean way to redefine a
bottleneck method so you can account for and aggregate all the calls
to it.

    % ruby -Ilib bin/zenprofile misc/factorial.rb 50000
    Total time = 3.056884
    Total time = 2.390000
    
              total     self              self    total
    % time  seconds  seconds    calls  ms/call  ms/call  name
     50.70     1.64     1.64    50000     0.03     0.05 Integer#downto
     19.63     2.27     0.63   200000     0.00     0.00 Fixnum#*
     14.19     2.73     0.46    50000     0.01     0.05 Factorial#factorial
      9.93     3.05     0.32        1   320.36  3047.10 Range#each
      5.54     3.23     0.18        2    89.40   178.79 ZenProfiler#start_hook

Once you know that Integer#downto takes 50% of the entire run, you
can use spy_on to find it. (See misc/factorial.rb for the actual code):

    % SPY=1 ruby -Ilib misc/factorial.rb 50000
    Spying on Integer#downto
    
    Integer.downto
    
    50000: total
    50000: ./misc/factorial.rb:6:in `factorial' via 
           ./misc/factorial.rb:6:in `factorial'

## 官网

- 主页: http://rubyforge.org/projects/seattlerb
- RubyGems: https://rubygems.org/gems/zenprofile

## 历史版本号

- 1.3.2 (2012-04-07)
- 1.3.1 (2011-02-19)
- 1.3.0 (2010-09-02)
- 1.2.0 (2009-08-18)
- 1.1.0 (2009-08-05)
- 1.0.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/zenprofile
- gem 安装: `gem install zenprofile`
- Bundler: `gem "zenprofile"`
- 最新版本: 1.3.2
- 最新版归档: https://rubygems.org/downloads/zenprofile-1.3.2.gem
- 版本锁定: `gem "zenprofile", "~> 1.3.2"`
- 中央仓库: https://rubygems.org/
