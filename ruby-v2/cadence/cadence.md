# cadence

**Tag**: web

## 简介

Track counts and compute rate of iteration. Set up callbacks for various
    intervals such as every n increments or every n ticks.
    
    computer = Cadence::Computer.new do |c|
      c.every 5 do
        p [:completed_processing, n]
      end
    end
    
    computer.start do |c|
      1.upto(100) do |n|
        c.next
        # do magic here
      end
    end
    
    Mostly intended for providing intermitent feedback of the progress of tasks
    that will run for lengthy periods of time.
    
    Rudimentary support for time-based callbacks is possible through #ticks.

## 官网

- 主页: http://github.com/mtodd/cadence
- RubyGems: https://rubygems.org/gems/cadence

## 历史版本号

- 0.0.2 (2010-09-01)
- 0.0.1 (2010-09-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/cadence
- gem 安装: `gem install cadence`
- Bundler: `gem "cadence"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/cadence-0.0.2.gem
- 版本锁定: `gem "cadence", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
