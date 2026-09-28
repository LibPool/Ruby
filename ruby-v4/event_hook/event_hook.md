# event_hook

**Tag**: library

## 简介

Wraps rb_add_event_hook so you can write fast ruby event hook
processors w/o the speed penalty that comes with set_trace_func (sooo
sloooow!). Calls back into ruby so you don't have to write C.

    % ruby demo.rb 
    # of iterations = 1000000
                              user     system      total        real
    null_time             0.120000   0.000000   0.120000 (  0.125279)
    ruby time             0.560000   0.000000   0.560000 (  0.562834)
    event hook            3.160000   0.010000   3.170000 (  3.175361)
    set_trace_func       34.530000   0.100000  34.630000 ( 34.942785)

## 官网

- 主页: http://rubyforge.org/projects/seattlerb
- RubyGems: https://rubygems.org/gems/event_hook

## 历史版本号

- 1.1.1 (2012-02-05)
- 1.0.2 (2010-09-02)
- 1.0.1 (2009-08-05)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/event_hook
- gem 安装: `gem install event_hook`
- Bundler: `gem "event_hook"`
- 最新版本: 1.1.1
- 最新版归档: https://rubygems.org/downloads/event_hook-1.1.1.gem
- 版本锁定: `gem "event_hook", "~> 1.1.1"`
- 中央仓库: https://rubygems.org/
